from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages = self.sum_overages + item
    def __len__(self):
        return self.expenses.len() + self.overages.len()

def main():
    myBudgetList = BudgetList(1200)