# Sample initialization
budgets = {}
expenses = {}
funds = 5000  # total available funds

def AddBudget(category, amount):
    global budgets, expenses, funds
    budgets[category] = amount
    expenses[category] = 0
    funds -= amount

def Spend(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        print(f"Category '{category}' does not exist.")

def PrintBudget():
    print("----------------------------------------------------")
    print(f'{"Category":15s} {"Budgeted":10s} {"Spent":10s} {"Remaining":10s}')
    
    totalBudgeted = 0
    totalSpent = 0
    totalRemaining = 0 

    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingBudget = budgeted - spent

        print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} {remainingBudget:10.2f}')

        totalBudgeted += budgeted
        totalSpent += spent
        totalRemaining += remainingBudget

    print("----------------------------------------------------")
    print(f'{"Total":15s} {totalBudgeted:10.2f} {totalSpent:10.2f} {totalRemaining:10.2f}')
    print(f'Remaining unallocated funds: {funds:.2f}')
    print("----------------------------------------------------")


print("Total funds: ", funds)
AddBudget("Clothes", 1000)
AddBudget("Rent", 1600)

Spend("Clothes", 500)
Spend("Rent", 1500)  

PrintBudget()
