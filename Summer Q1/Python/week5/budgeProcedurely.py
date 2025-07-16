def PrintBudget():
    totalBudgeted = 0
    totalSpent = 0
    totalRemaining = 0

    print("----------------------------------------------------")
    print(f'{"Category":15s} {"Budgeted":10s} {"Spent":10s} {"Remaining":10s}')
    
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
