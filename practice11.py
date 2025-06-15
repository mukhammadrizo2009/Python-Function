def calculate_tax(salary: float):

    """Taksi kalkulyatori
    
    Bu funksiya foydalanuvchi oylik maoshini kiritadi
    funksiya besh milliondan (5 000 000) dan yuqori bo'lsa
    va undan past bo'lsa ikki hil soliq foizida hisoblaydi!

    ARGS:
        salary (float) = Foydalanuvchi oylik maoshini kiritaldi!
                        Butun formatida kiritilishi kerak!

    Errors:
             Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!
    """
    if salary > 5_000_000:
        tax = salary*0.2
    else:
        tax = salary*0.13

    return tax



def calculate_net_salary(salary):
    pass


salary = 10_000_000
tax = calculate_tax(salary)
print(tax)

net_salary = calculate_net_salary(salary,tax)
print(net_salary)
