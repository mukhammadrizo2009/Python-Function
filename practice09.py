def deposit(balance, amount):
    new_balance = balance + amount
    return new_balance


def withdraw(balance, amount):
    if amount <= balance:
        new_balance = balance - amount
    else:
        new_balance = balance

    return new_balance

def check_balance(balance):
    print(f"Sizning balansingiz = {balance}")


balance = 100.0

amount = float(input("Qancha depozit qilmoqchisiz!"))
balance = deposit(balance , amount)
check_balance(balance)


amount = float(input("Qanch pul chiqarmoqchsiz?: "))
balance = withdraw(balance,amount)
check_balance(balance)