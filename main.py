total_income = []
total_expense = []
final_balance = 0


def _total_income(final_balance):
    salary = float(input("Enter your salary: "))
    bonus = float(input("Enter your bonus: "))

    total_income.append(salary)
    total_income.append(bonus)

    for item in total_income:
        final_balance += item

    print(f"Your total income is: ${final_balance:.2f}")

def _total_expense(final_balance):
    while True:
        expense_name = str(input("Enter your name expense: ")).strip().lower()
        expense = float(input("Enter your expense: "))
        total_expense.append(expense_name)
        total_expense.append(expense)

        for item in total_expense:
            print(f"{expense_name} -- ${expense:.2f}")







def _final_balance():
    pass

def main():
    _total_income(final_balance)
    _total_expense(final_balance)
    _final_balance()







if __name__ == '__main__':
    main()
