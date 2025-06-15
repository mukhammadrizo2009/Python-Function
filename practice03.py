number = int(input("Raqam kiriting: "))

def iseven(number: int):
    """Bu juft yoki toqlik aniqlaydi!
    
    Bu funksiya foydalanuvchi raqam kiritadi agar
    raqam toq bo'lsa = False agar juft bo'lsa = True
                    chiqaradi!
                    
    ARGS:
        number (int) = Siz bu yerga butun son kritishingiz kerak!
        
        
    Errors:
        Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!   """
    
    return number % 2 == 0

print(iseven(number))
    