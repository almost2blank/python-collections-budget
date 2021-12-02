from . import Expense
import matplotlib.pyplot as plt

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if not divided_set_comp == divided_for_loop:
        print('Sets or NOT equal by == test')

    for a,b in zip(divided_for_loop, divided_set_comp):
        pass


if __name__ == "__main__":
    main()