def check_guess(secret, guess):
<<<<<<< HEAD
    """Kompuyuter yashirgan sonni topadigan funksiya!
    
    Bu funksiya kiritilgan son kompuyuter o'ylagan son bilan bir hil
    bo'lsa gina ishliydi 

    Errors:
           Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!
    
    """
=======
>>>>>>> 266bf3531177991d13d3339de3d6d1eca571087a
    result = secret == guess
    return result

def print_result(is_corect):
<<<<<<< HEAD

=======
>>>>>>> 266bf3531177991d13d3339de3d6d1eca571087a
    if is_corect:
        print("To'g'ri javob!")

    else:
        print("Noto'g'ri javob!")

    secret = 65 
    guess = int(input("Sirli sonni toping: "))


    is_correct = check_guess(secret,guess)
    print_result(is_correct)