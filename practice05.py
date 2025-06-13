def check_guess(secret, guess):
    result = secret == guess
    return result

def print_result(is_corect):
    if is_corect:
        print("To'g'ri javob!")

    else:
        print("Noto'g'ri javob!")

    secret = 65 
    guess = int(input("Sirli sonni toping: "))


    is_correct = check_guess(secret,guess)
    print_result(is_correct)