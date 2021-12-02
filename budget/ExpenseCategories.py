from . import Expense
import matplotlib.pyplot as plt

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if divided_for_loop != divided_set_comp:
        print('Sets or NOT equal by == test')


if __name__ == "__main__":
    main()