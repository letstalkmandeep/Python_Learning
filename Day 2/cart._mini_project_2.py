# Create a e-commerce cart that takes what items customers wants to buy, Ask for their name, How many quantity they want to buy, at what price the are buying , total cart using dollar sign
print("Welcome to our Store \nIf you wants to buy something let's get started")

name = str(input("What's your name sir :"))
product = str(input("What do you wish to buy :"))
price = float(input("What price are you willing to give for that :"))
quantity = int(input("How much do you wish to buy :"))


# Cart
print(f"\n\nCustomer Name = {name} \nProduct = {product} \nPrice = ${price} \nQuantity = {quantity} \nTotal Cart Value = ${quantity*price}\n\nThank's Alot for purchasing from our Store\nPlease Come Again")

