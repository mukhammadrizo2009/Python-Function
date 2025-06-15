def is_valid_phone_number(phone: int):
    """Kirilgan son 9 harfdan iboratmi!
    
    Bu funksiya foydalanuvchi kiritgan sonlarni tekshiradi
    Bu birinchi butun sonligini aniqlaydi va 9 raqamdan iboratligini
                    tekshiradi!
                    
    ARGS:
        phone (int) = 9 ta butun son kiritilish kerak
                      
    Errors:   
         Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!           """

    if phone.isdigit() and len(phone) == 9 :
        return print("Raqam to'g'ri kiritildi!")
    
    else:
        return print("Raqam hato kiritildi!")
    

def main():
    phone = input("Telefon raqamingizni kiriting: ")

    is_valid_phone_number(phone)

main()