def is_valid_phone_number(phone):

    if phone.isdigit() and len(phone) == 9 :
        return print("Raqam to'g'ri kiritildi!")
    
    else:
        return print("Raqam hato kiritildi!")
    

def main():
    phone = input("Telefon raqamingizni kiriting: ")

    is_valid_phone_number(phone)

main()