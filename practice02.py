
current_year = 2025

def calculate_age( current_year):
    """Funksiya yoshni aniqlaydi!
    
    Bu funksiyada foydalanuvchi o'zyoshini kiritadi funksiya 
    quyidagi amallar bilan foydalanuvchi yoshini chiqaradi.
    
    ARGS:
        current_year (2025) = Funksiya hozirgi yilni o'zi aniqlaydi
        birt_year (int) = Tug'ulgan yilingizni kiritasiz

    Errors:
        Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!
    """

    birth_year = int(input("Tug'ulgan yilingizni kiriting: "))
    result = current_year - birth_year
    return result

age = calculate_age( current_year)

print("Sizning yoshingiz", age ,"da")

if age >= 16:
    print("Siz balog'at yoshiga yetgansiz!")
else:
    print("Siz balog'atga yoshiga etmagansiz")
