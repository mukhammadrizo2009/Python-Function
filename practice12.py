def calculate_bmi(weight: int , height: float):
    """Semizlikni aniqlovchi funksiya
    
  Bu funksiya vazningizni kiritasiz bu kirilgan formulada
  Sizning qay qolatda ekanligingizni aniqlaydi!
  
  ARGS:
      weight (int) = Foydalanuvchi o'z vaznini butun son ko'rinishida kiritadi!
      height (float) = Foydalanuvchi o'z bo'yini kiritadi!
      
  Errors:
   Agar funksiyada mavjud bo'lmagan narsalarni kiritsangiz
        bir qancha xatoliklar berishi mumkin!
        
        """
    return round(weight / (height ** 2), 2)

def bmi_status(bmi):
    
    if bmi < 18.5:
        return "Ozg'in"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Semiz"
    
def main():
    weight = float(input("Vazningizni kiriting (kg): "))
    height = float(input("Bo'yingizni kiriting (metrlarda): "))
    
    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)

    print(f"\nBMI: {bmi}")
    print(f"Holati: {status}")

main()
