from rag import build_index, generate_answer, verify_answer

question = "What counts as manipulating someone's behavior?"

build_index()

answer, context = generate_answer(question)

verdict, explanation = verify_answer(answer, context)

print("Answer:")
print(answer)

print("\nVerdict:")
print(verdict)