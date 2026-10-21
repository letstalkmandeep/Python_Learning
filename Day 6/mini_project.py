"""
Mini Project
Shopping Discount System:
Ask user the product name, ask the price and quantity check if the total is more than certail threshold offer x amount of on the total cart 
and print discounted amount and net amount to be paid!
"""

#conditions

top_bracket = 1000
dis_top_bracket = 0.25
mid_bracket = 500
dis_mid_bracket = 0.1
ex_qty = 3
additional_dis = 0.05

# purchase
print(f'Welcome to our store if you Purchase more then the amount of {top_bracket} you will get {dis_top_bracket*100}% Discount\nIf you purchase more than {mid_bracket} you will get {dis_mid_bracket*100}% Discount\nIf you purchase more than {ex_qty} items you will get additional discount of {additional_dis}%')
user = input("Mention the Product which you with price and quantity like (Product_name,Price,Quantity) -").strip()

# cleaning and striping and spliting
cleaned = [item.strip() for item in user.split(",")]

# calculations
price = int(cleaned[1])
qty = int(cleaned[2])
total_price = price*qty

if total_price > top_bracket:
    if qty > ex_qty :
        print(f"Product - {cleaned[0]}\nPrice - {price}\nQuantity - {qty}\nTotal Discount Rate - @{(dis_top_bracket+additional_dis)*100}%\nDiscounted Amount - {total_price*(dis_top_bracket+additional_dis)}\nTotal Amount - {total_price - total_price*(dis_top_bracket+additional_dis)}")
    else :
        print(f"Product - {cleaned[0]}\nPrice - {price}\nQuantity - {qty}\nTotal Discount Rate - @{dis_top_bracket*100}%\nDiscounted Amount - {total_price*dis_top_bracket}\nTotal Amount - {total_price - total_price*dis_top_bracket}")
elif total_price > mid_bracket :
    if qty > ex_qty :
            print(f"Product - {cleaned[0]}\nPrice - {price}\nQuantity - {qty}\nTotal Discount Rate - @{(dis_mid_bracket+additional_dis)*100}%\nDiscounted Amount - {total_price*(dis_mid_bracket+additional_dis)}\nTotal Amount - {total_price - total_price*(dis_mid_bracket+additional_dis)}")
    else :
            print(f"Product - {cleaned[0]}\nPrice - {price}\nQuantity - {qty}\nTotal Discount Rate - @{dis_mid_bracket*100}%\nDiscounted Amount - {total_price*dis_mid_bracket}\nTotal Amount - {total_price - (total_price*dis_mid_bracket)}")
elif qty > ex_qty :
     print(f"Product - {cleaned[0]}\nPrice - {price}\nQuantity - {qty}\nTotal Discount Rate - @{additional_dis*100}%\nDiscounted Amount - {total_price*additional_dis}\nTotal Amount - {total_price - total_price*additional_dis}")
else :
     print(f"Product - {cleaned[0]}\nPrice - {price}\nQuantity - {qty}\nTotal Discount Rate - @0%\nTotal Amount - {total_price}")

