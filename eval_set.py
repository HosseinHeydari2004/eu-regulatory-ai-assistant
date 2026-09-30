evaluation_questions = [
    {
        "question": "What kinds of AI practices are prohibited?",
        "expected_chunk_id": 0,
        "answerable": True
    },
    {
        "question": "What kind of AI manipulation can cause significant harm to people?",
        "expected_chunk_id": 1,
        "answerable": True
    },
    {
        "question": "How can AI take advantage of a person's vulnerabilities and cause harm?",
        "expected_chunk_id": 2,
        "answerable": True
    },
    {
        "question": "How can AI systems use people's social behavior to evaluate or score them?",
        "expected_chunk_id": 3,
        "answerable": True
    },
    {
        "question": "How can a social score lead to unfair treatment of people?",
        "expected_chunk_id": 3,
        "answerable": True
    },
    {
        "question": "Can AI be used to predict whether someone will commit a crime based only on their personality?",
        "expected_chunk_id": 4,
        "answerable": True
    },
    {
        "question": "Can AI systems collect people's faces from the internet to build facial recognition databases?",
        "expected_chunk_id": 5,
        "answerable": True
    },
    {
        "question": "Can AI be used to detect people's emotions at work or in education?",
        "expected_chunk_id": 6,
        "answerable": True
    },
    {
        "question": "Can AI infer sensitive personal characteristics from someone's biometric data?",
        "expected_chunk_id": 7,
        "answerable": True
    },
    {
        "question": "When can law enforcement use real-time biometric identification in public places?",
        "expected_chunk_id": 8,
        "answerable": True
    },
    {
        "question": "What situations can justify the use of real-time biometric identification by law enforcement?",
        "expected_chunk_id": 8,
        "answerable": True
    },
    {
        "question": "What factors should be considered before using real-time biometric identification in a public place?",
        "expected_chunk_id": 8,
        "answerable": True
    },
    {
        "question": "What should authorities consider about the potential harm before using a biometric identification system?",
        "expected_chunk_id": 8,
        "answerable": True
    },
    {
        "question": "What approval is needed before law enforcement can use real-time biometric identification in public places?",
        "expected_chunk_id": 8,
        "answerable": True
    },
    {
        "question": "What happens if the use of a real-time biometric identification system is not authorised?",
        "expected_chunk_id": 8,
        "answerable": True
    }
]





unanswerable_questions = [
    {
        "question": "What is the capital of Germany?",
        "expected_chunk_id": None,
        "answerable": False
    },
    {
        "question": "What penalties can companies face for using prohibited AI systems?",
        "expected_chunk_id": None,
        "answerable": False
    },
    {
        "question": "What fines can companies receive for violating AI regulations?",
        "expected_chunk_id": None,
        "answerable": False
    },
    {
        "question": "What rights do individuals have when an AI system causes them harm?",
        "expected_chunk_id": None,
        "answerable": False
    },
    {
        "question": "Who is responsible for monitoring companies that use AI systems?",
        "expected_chunk_id": None,
        "answerable": False
    }
]

eval_set = evaluation_questions + unanswerable_questions