<<<<<<< HEAD
def deposit(balance: int, amount: int):
    """Hisob raqamga pul qo'shish!
    
    Bu funksiya foydalanuvchi hisob raqamiga 
    mablag' qo'shish uchun ishlatiladi!
    
    ARGS: 
        balance (int) = Foydalanuvchi hisobi!
        amount (int) = Foydalanuvchi qo'shmoqchi bo'lgan summa!
        new_balance = Hisobda qolgan summa!
        
        
    Errors:
            Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!  """
    
=======
def deposit(balance, amount):
>>>>>>> 266bf3531177991d13d3339de3d6d1eca571087a
    new_balance = balance + amount
    return new_balance


<<<<<<< HEAD
def withdraw(balance: int, amount: int):
    """Hisob raqamdan pul yechish!
    
    Bu funksiya foydalanuvchining hisobidan yechib olmoqchi
     bo'lgan summani yechadi. Agar balansda pul yetarli bo'lmasa
                    bu amal bajarilmaydi 
                     
    ARGS:
        balance (int) = Foydalanuvchi hisobi!
        amount (int) = Foydalanuvchi hisobdan yechib olmoqchi bo'lgan summa!
        new_balance = Hisobda qolgan summa!
         
    Errors:
        Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin """
    
=======
def withdraw(balance, amount):
>>>>>>> 266bf3531177991d13d3339de3d6d1eca571087a
    if amount <= balance:
        new_balance = balance - amount
    else:
        new_balance = balance

    return new_balance

def check_balance(balance):
<<<<<<< HEAD
    """Hisobda qolgan mablag'ni tekshiradi!
    
    Bu funksiya sizning hisobingizda qolgan mablag'ni ko'rish
                imkoniyatini beradi!
                
    ARGS:
        balance = Hisobbingizda qolgan mablag'!
        
    Errors:
        Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin"""
=======
>>>>>>> 266bf3531177991d13d3339de3d6d1eca571087a
    print(f"Sizning balansingiz = {balance}")


balance = 100.0

amount = float(input("Qancha depozit qilmoqchisiz!"))
balance = deposit(balance , amount)
check_balance(balance)


amount = float(input("Qanch pul chiqarmoqchsiz?: "))
balance = withdraw(balance,amount)
check_balance(balance)