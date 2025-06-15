def ask_question(question: str): 
    """To'g'ri javobni topish!
    
    Bu funksida savollar kiritiladi foydalanuvchi
    o'z javobini kiritadi agar javob noto'g'ri bo'lsa
        to'gri javobni ham aytish mumkin
        
    ARGS:
        question (str) = Dasturchi savolni kiritadi bu yerga string metodida
        
        
    Errors:
        Agar foydalanuvchi int,bool,real sonlar kiritsa xatolik beriladi!
        Va Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar ham berishi mumkin!"""
    user_answer = input(f"{question}").strip()
    return user_answer

def check_answer(user_answer: str, correct_answer: str):
    """Javobni solish terish!
    
    Bu funksiyada foydalanuvchi kiritgan javobni kompyuter
    biladigan javob bilan solish teriladi. Agar to'gri bo'lsa
    "To'g'ri" agar noto'g'ri bo'lasa "Noto'g'ri" deb chiqaradi!
    
    ARGS:
        question (str) = Savol beriladi!
        user_answer (str) = Foydalanuvchi javobi!
        correct_answer (str) = To'g'ri javob!
        
    Errors:
         Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!"""
    
    result = user_answer.lower() == correct_answer.lower()
    return result

def main():
    question = "Tojikiston poytahti qayer?: "
    correct_answer = "Dushanbe"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer , correct_answer)

    if is_correct:
        print("To'g'ri javob!")

    else:
        print(f"Noto'g'ri, to'g'ri javob \"{correct_answer}\"")

    question = "Tojikistonda nechta viloyat bor?: "
    correct_answer = "4"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer , correct_answer)

    if is_correct:
        print("To'g'ri javob!")

    else:
        print(f"Noto'g'ri, to'g'ri javob \"{correct_answer}\"")
    
    question = "Tojikiston pul berligi nima?: "
    correct_answer = "Somoni"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer , correct_answer)

    if is_correct:
        print("To'g'ri javob!")

    else:
        print(f"Noto'g'ri, to'g'ri javob \"{correct_answer}\"")

    question = "Tojikistonning eng katta ikkita shaharlari bu?: "
    correct_answer = "Dushanbe va Hujand"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer , correct_answer)

    if is_correct:
        print("To'g'ri javob!")

    else:
        print(f"Noto'g'ri, to'g'ri javob \"{correct_answer}\"")

    question = "Tojikiston qaysi davlatlar bilan chegaradosh?: " 
    correct_answer = "O'zbekiston , Qirg'iziston , Afg'oniston , Xitoy"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer , correct_answer)

    if is_correct:
        print("To'g'ri javob!")

    else:
        print(f"Noto'g'ri, to'g'ri javob \"{correct_answer}\"")

main()
