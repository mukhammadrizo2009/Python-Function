def is_valid_phone_number(phone):

    if phone.isdigit() and len(phone) >= 8 :
        return print("Parol to'g'ri kiritildi!")
    
    else:
        return print("Parol yetarli emas!")
    

def main():
    phone = input("Parolingizni kiriting: ")

    is_valid_phone_number(phone)

main()