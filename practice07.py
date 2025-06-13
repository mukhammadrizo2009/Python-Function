def ask_question(question): 
    user_answer = input(f"{question}").strip()
    return user_answer

def check_answer(user_answer, correct_answer):
    result = user_answer.lower() == correct_answer.lower()
    return result

def main():
    question = "Tojikiston poytahti qayer?"
    correct_answer = "Dushanbe"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer , correct_answer)

    if is_correct:
        print("To'g'ri javob!")

    else:
        print(f"Noto'g'ri, to'g'ri javob \"{correct_answer}\"")

main()
