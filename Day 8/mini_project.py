def calculator(num1,num2,operator):
    if operator == "add":
        result = num1 + num2
    elif operator == "sub":
        result = num1 - num2
    elif operator == "mul":
        result = num1*num2
    elif operator == "div":
        result = num1/num2
    else:
        result = "Enter right operator as : add, sub, mul, div"
    return print(f"{num1} {operator} {num2} = {result}")

# call user 

if __name__ == "__main__":
    num1 = int(input("Please enter your first number :"))
    num2 = int(input("Please enter your second number :"))
    operator = input("Enter your operator as add, sub, mul, div :")
    print(f"{calculator(num1,num2,operator)}")
    
