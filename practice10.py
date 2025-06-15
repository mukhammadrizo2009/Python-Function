<<<<<<< HEAD
def is_strong_password(password: str):
    """Parolni tekshirishrish funksiyasi!
    
    Bu funksiyada foydalanuvchi parol kiritadi
     agar parol sakkiz(8) va undan ko'p raqam ishlatilgan 
      bo'lishi kerak bu shuni tekshiradi!
       
        
    ARGS:
        password (str) = foydalavunchi raqam bilan kiritsaham string qiymatda qabul qiladi!
        
        
    Errors:
        Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin """

    if password.isdigit() and len(password) >= 8 :
=======
def is_valid_phone_number(phone):

    if phone.isdigit() and len(phone) >= 8 :
>>>>>>> 266bf3531177991d13d3339de3d6d1eca571087a
        return print("Parol to'g'ri kiritildi!")
    
    else:
        return print("Parol yetarli emas!")
    

def main():
<<<<<<< HEAD
    password = input("Parolingizni kiriting: ")

    is_strong_password(password)
    
=======
    phone = input("Parolingizni kiriting: ")

    is_valid_phone_number(phone)
>>>>>>> 266bf3531177991d13d3339de3d6d1eca571087a

main()