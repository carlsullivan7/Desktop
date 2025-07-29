# budget.py

class Budget:
    def __init__(self, total_funds):
        # Step 3: Create instance variables
        self.total_funds = total_funds
        self.budgets = {}  # dictionary to store items and their allocated amounts

    def add_item(self, item_name, amount):
        # Add a budget item
        self.budgets[item_name] = amount

    def get_total_budgeted(self):
        # Return total amount budgeted
        return sum(self.budgets.values())

    def get_remaining_funds(self):
        # Return remaining funds after budgeting
        return self.total_funds - self.get_total_budgeted()

    def show_budget(self):
        # Print all budget items and amounts
        print("Your budget breakdown:")
        for item, amount in self.budgets.items():
            print(f"{item}: ${amount}")
        print(f"Total Budgeted: ${self.get_total_budgeted()}")
        print(f"Remaining Funds: ${self.get_remaining_funds()}")


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

