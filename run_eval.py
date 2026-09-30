from eval_set import eval_set
from rag import build_index, retrieve, generate_answer, verify_answer


build_index()

retrieval_results = []

for case in eval_set:

    question = case['question']

    retrieved = retrieve(question)

    chunk_ids = [
        chunk_id
        for chunk_id, document, distance in retrieved
    ]

    if case["answerable"]:

        expected_chunk_id = case["expected_chunk_id"]

        expected_chunk = f"chunk_{expected_chunk_id}"

        retrieval_success = expected_chunk in chunk_ids

    else:

        expected_chunk = None

        retrieval_success = None

    retrieval_results.append({
        "question": question,
        "expected_chunk": expected_chunk,
        "retrieved_chunks": chunk_ids,
        "retrieval_success": retrieval_success,
        "answerable": case["answerable"],
    })



answerable_retrieval = [
    r
    for r in retrieval_results
    if r["answerable"]
]

successful_retrievals = sum(
    r["retrieval_success"] == True
    for r in answerable_retrieval
)





retrieval_accuracy = (
    successful_retrievals / len(answerable_retrieval)
) * 100

print(f"Retrieval Accuracy: {retrieval_accuracy:.2f}%")




generation_results = []

for case in eval_set:

    question = case["question"]

    answer, context = generate_answer(question)

    verdict, explanation = verify_answer(answer, context)

    generation_results.append({
        "question": question,
        "answerable": case["answerable"],
        "answer": answer,
        "verdict": verdict,
        "explanation": explanation
    })




unanswerable_generation = [
    g
    for g in generation_results
    if not g["answerable"]
]

correct_refusals = sum(
    "don't know" in g["answer"].lower()
    for g in unanswerable_generation
)

refusal_accuracy = (
    correct_refusals / len(unanswerable_generation)
) * 100

print(f"Refusal Accuracy: {refusal_accuracy:.2f}%")




grounded_count = sum(
    g["verdict"] == "GROUNDED"
    for g in generation_results
)

groundedness_rate = (
    grounded_count / len(generation_results)
) * 100

print(f"Groundedness Rate: {groundedness_rate:.2f}%")