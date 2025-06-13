def check_answer(user_answer, correct_answer):

  return user_answer.strip().lower() == correct_answer.strip().lower()


def ask_question(question: str, correct_answer: str):
    
    user_answer = input("Savolni kiriting: " ,question + " ")

    if check_answer(user_answer, correct_answer):
        print("To'g'ri javob!")
    else:
        print(f"Noto'g'ri. To'g'ri javob: {correct_answer}")

def main():
    ask_question("1.8+8=?" , "16")
