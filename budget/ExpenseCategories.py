from datetime import time
import timeit
from . import Expense
import matplotlib.pyplot as plt


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if not divided_set_comp == divided_for_loop:
        print("Sets are NOT equal by == test")

    for a,b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")

    print(timeit.timeit(stmt = "expenses.categorize_for_loop()",
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''',
                        number=100000,
                        globals=globals()))       
print(timeit.timeit(stmt = "expenses.categorize_set_comprehension()",
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''',
                        number=100000,
                        globals=globals())) 

fig,ax=plt.subplots()
if __name__ == "__main__":
    main()