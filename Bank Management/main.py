import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []


    try:
        if Path(database).exists():
            with open(database,'r') as file:
                data = json.loads(file.read())
        else:
            print("Path doesn't Exists")
    except Exception as err:
        print(f"An exception occured as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @staticmethod
    def account_generate():
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        special = random.choices("!@#$%^&*",k=1)
        id = alpha+num+special
        random.shuffle(id)
        return "".join(id)
        


    def create_account(self):
        info = {
            "name": input("What is your name :"),
            "age" : int(input("What is your age :")),
            "email": input("Write your email :"),
            "pin": int(input("Write your 4 digit pin number :")),
            "account_no" : Bank.account_generate(),
            "balance" : 0
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("You can not create your account")
        else:
            print("Your account has been successfully created")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Kindly note down your account number")

            Bank.data.append(info)
            Bank.update()

    def deposit_money(self):
        acc_number = input("Enter your account number :-")
        pin = int(input("Enter your 4 digit pin :-"))

        userdata = [i for i in Bank.data if i['account_no'] == acc_number and i['pin'] == pin]

        if userdata == []:
            print("Account not Exists")
        else:
            deposit = int(input("Enter the amount you wants to deposit :-"))
            if deposit > 10000 and deposit <= 0:
                print("You can only deposit amount between 0 to 10000")
            else:
                userdata[0]["balance"] += deposit
                Bank.update()
                print(f"Your amount : {deposit} has been successfully deposited")
                print(f"Current Balance : {userdata[0]['balance']}")

    def withdraw_money(self):
        acc_number = input("Enter your account number :-")
        pin = int(input("Enter your account pin :-"))

        userdata = [i for i in Bank.data if i['account_no'] == acc_number and i['pin'] == pin]
        if userdata == []:
            print("No account exists")
        elif userdata[0]['balance'] == 0:
            print("Insufficient Balance you can not withdraw money")
        else:
            withdraw = int(input("Enter the amount you wants to withdraw :-"))
            if withdraw < 0 or withdraw > userdata[0]['balance']:
                print(f"Invalid amount entered\nCurrent Balance : {userdata[0]['balance']}")
            else:
                userdata[0]['balance'] -= withdraw
                Bank.update()
                print(f"Your amount {withdraw} has been successfully withdrawn")
                print(f"Current Balance : {userdata[0]['balance']}")

    def account_details(self):
        acc_number = input("Enter your account number :-")
        pin = int(input("Enter your Account Pin :-"))

        userdata = [i for i in Bank.data if i['account_no'] == acc_number and i['pin'] == pin]
        if userdata == []:
            print("Account not exists")
        else:
            my_dict = userdata[0]
            print("Your Account Details are :--\n\n\n")
            for x, y in my_dict.items():
                print(f"{x} : {y}")

    def update_details(self):
        acc_number = input("Enter your account number :-")
        pin = int(input("Enter your account 4 digit pin :-"))

        userdata = [i for i in Bank.data if i['account_no'] == acc_number and i['pin'] == pin]
        if userdata == []:
            print("Account not Exists")
        else:
            print("You can only update 3 details :-")
            print("1. Name\n2. Email\n3. Pin\n4. All of them")
            select = int(input("Kindly select the one which you wish to update :-"))
            if select == 1:
                new_name = input("Write your new name :-")
                userdata[0]['name'] = new_name
                Bank.update()
                print("Your name has been updated")
                for x, y in userdata[0].items():
                    print(f"{x} : {y}")
            elif select == 2:
                new_email = input("Write your new E-mail :-")
                userdata[0]['email'] = new_email
                Bank.update()
                print("Your E-mail has been updated")
                for x, y in userdata[0].items():
                    print(f"{x} : {y}")
            elif select == 3:
                new_pin = int(input("Write your new pin :-"))
                if len(str(new_pin)) == 4:
                    userdata[0]['pin'] = new_pin
                    Bank.update()
                    print("Your name has been updated")
                    for x, y in userdata[0].items():
                        print(f"{x} : {y}")
                else:
                    print("Kindly enter a 4 digit pin")
            elif select == 4:
                new_name = input("Write your new name :-")
                new_email = input("Write your new E-mail :-")
                new_pin = int(input("Write your new pin :-"))
                if len(str(new_pin)) == 4:
                    userdata[0]['name'] = new_name
                    userdata[0]['email'] = new_email
                    userdata[0]['pin'] = new_pin
                    Bank.update()
                    print("Your details have been updated")
                    for x, y in userdata[0].items():
                        print(f"{x} : {y}")
                else:
                    print("Kindly enter a valid pin")
            else:
                print("Kindly select valid details")


    def delete_account(self):
        acc_number = input("Enter your account number :-")
        pin = int(input("Enter your account 4 digit pin :-"))
        userdata = [i for i in Bank.data if i['account_no'] == acc_number and i['pin'] == pin]
        if userdata == []:
            print("Account not Exists")
        else:    
            print("Do you really wish to delete your account.")
            print("1. Yes\n2. No")
            Validation = int(input("Select :-"))
            if Validation == 1:
                del userdata[0]
                Bank.update()
                print("Your account has been successfully deleted")
            elif Validation == 2:
                print("Thanks for visiting")
            else:
                print("Kindly select valid information")
                
                
user = Bank()

print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Details")
print("5. Update Details")
print("6. Delete Account")


check = int(input("Tell your response :-"))

if check == 1:
    user.create_account()
elif check == 2:
    user.deposit_money()
elif check == 3:
    user.withdraw_money()
elif check == 4:
    user.account_details()
elif check == 5:
    user.update_details()
elif check == 6:
    user.delete_account()