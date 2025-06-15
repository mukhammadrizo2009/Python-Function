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
    
    new_balance = balance + amount
    return new_balance


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
    
    if amount <= balance:
        new_balance = balance - amount
    else:
        new_balance = balance

    return new_balance

def check_balance(balance):
    """Hisobda qolgan mablag'ni tekshiradi!
    
    Bu funksiya sizning hisobingizda qolgan mablag'ni ko'rish
                imkoniyatini beradi!
                
    ARGS:
        balance = Hisobbingizda qolgan mablag'!
        
    Errors:
        Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin"""
    print(f"Sizning balansingiz = {balance}")


balance = 100.0

amount = float(input("Qancha depozit qilmoqchisiz!"))
balance = deposit(balance , amount)
check_balance(balance)


amount = float(input("Qanch pul chiqarmoqchsiz?: "))
balance = withdraw(balance,amount)
check_balance(balance)