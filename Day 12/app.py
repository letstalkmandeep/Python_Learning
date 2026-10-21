# mini project Personal Expenses Tracker
"""
Developing a personal expense tracker that 
allows users to add, 
view expenses
exit the function
"""

import csv
import os
from datetime import datetime

def add_expense(description,expense):
    with open('personal_expense.csv','a',newline='') as file:
        line = csv.writer(file)
        line.writerow([description,expense,datetime.now().strftime('%d\\%m\\%Y,%H:%M:%S')])
    print('All Expense have been recorded') 

def view_expense():
    if os.path.exists('personal_expense.csv'):
        with open('personal_expense.csv') as file:
            expense = csv.reader(file)
            for e in expense:
                print(f'Discription : {e[0]}; Expense : ${e[1]}; Date : {e[2]}')
    else:
        print("File haven't recorded any Expenses yet")

def main():
    while True:
        print('Welcome to the personal tracker by MANDEEP SINGH')
        print('1. Add Expense\n2. View Expense\n3. Exit\n4. Clear Transactions')
        choose = input('Enter which function you wants to perform :')

        if choose == '1':
            description = input('Expense Detials :')
            expense = input('Expense Amount $')
            add_expense(description,expense)
        elif choose == '2':
            view_expense()
        elif choose == '3':
            print('Thanks for using our tracker')
            break
        elif choose == '4':
            with open('personal_expense.csv','w') as file:
                pass
            print("Tracker is Empty now")
        else:
            print('Kindly enter the write details')

if __name__ == "__main__":
    main()






