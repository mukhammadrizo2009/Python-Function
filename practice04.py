score = int(input("Natijangizni kiriting: "))


def get_grade(score: int):

    """Bu Natajangiz haqida ma'lumot beradi
    
Foydalanuvchi bu funkisa yaga o'z natijasi kiritadi
funksiya qaysi darajaga to'gri kelishini ko'rsatadi
              "A' "B" "C "D" "F" 
              
ARGS:
    score (int) = Natijani butun sonda kiritamiz!
    
Errors:
    Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!"""
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print(get_grade(score))

    