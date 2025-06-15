def add (a: int ,b: int):
    """Bu funksiya amallarni bir-biriga qo'shadi (+)!
    
    Siz bu funksiyada ikkita butun sonni kiritasiz
    bu sizga ikkalasing yeg'indisini topib beradi
    
    
    ARGS:
        a (int) = Birinchi butun sonni kiritasiz!
        b (int) = Ikkinchi butun sonni kiritasiz!
        
    Errors:
        Bu sizga "AnyError"lar berishi mumkin!"""
    
    result = a + b
    return result

def subtract(a: int, b: int):
    """Bu funksiya amallarni bir-biridan ayiradi (-)!
    
    Siz bu funksiyada ikkita butun sonni kiritasiz
    bu sizga ikkalasing summasini topib beradi
    
    
    ARGS:
        a (int) = Birinchi butun sonni kiritasiz!
        b (int) = Ikkinchi butun sonni kiritasiz!
        
    Errors:
        Bu sizga "AnyError"lar berishi mumkin!"""
    
    result = a - b
    return result

def multiply(a: int, b: int):
    """Bu funksiya amallarni bir-biriga ko'paytiradi (*)!
    
    Siz bu funksiyada ikkita butun sonni kiritasiz
    bu sizga ikkalasing ko'paytmasini topib beradi
    
    
    ARGS:
        a (int) = Birinchi butun sonni kiritasiz!
        b (int) = Ikkinchi butun sonni kiritasiz!
        
    Errors:
        Bu sizga "AnyError"lar berishi mumkin!"""
    
    result = a * b
    return result

def divide(a:int , b:int):
    """Bu funksiya amallarni bir-biridan bo'ladi(/)!
    
    Siz bu funksiyada ikkita butun sonni kiritasiz
    bu sizga ikkalasing bo'linmasini topib beradi
    
    
    ARGS:
        a (int) = Birinchi butun sonni kiritasiz!
        b (int) = Ikkinchi butun sonni kiritasiz!
        
    Errors:
        Bu sizga "AnyError"lar berishi mumkin!"""
    
    result = a / b
    return result

def main():

    a = int(input("A-ga qiymat bering: "))
    op = input("Qaysi amalda ishlasin! +,-,*,/ : ")
    b = int(input("B-ga qiymat bering: "))

    if op == "+":
        print(add(a , b ))

    elif op == '-':
        print(subtract(a , b ))

    elif op == '*':
        print(multiply(a , b ))

    elif op == '/':
        print(divide(a , b ))

    else:
        print("Noto'g'ri amal kiritildi!")

main()