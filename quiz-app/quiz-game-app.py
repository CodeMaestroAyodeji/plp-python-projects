# Simple Quiz Game
def quiz_app():
    result = 0

    questions = [
        {"question": "What is the capital of Nigeria?", "options": ["A. Lagos", "B. Kogi", "C. Abuja"], "answer": "C" },

        {"question": "Who is the current president of Nigeria?", "options": ["A. President Atiku", "B. President Tinubu", "C. President Fashola"], "answer": "B"},

        {"question": "Who is the governor of Ogun State?", "options": ["A. Mike Adenuga", "B. Dapo Abiodun", "c. Aliko Dangote"], "answer": "B"}
    ]

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: " ).upper()
        if answer == q["answer"]:
            result += 1
            print("Correct!")
        else:
            print("Wrong answer!")

    print(f"\nYou scored {result}/{len(questions)}")
quiz_app()