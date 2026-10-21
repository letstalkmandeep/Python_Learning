"""
Project: eCommerce Product Lookup System (No Loops) 
Scenario: You are managing an eCommerce store with three products in different categories. 
Each product has attributes like Product ID, Name, Price, and Stock. 
The project focuses on dictionary manipulation and string operations to retrieve and modify product data.
"""

ecommerce_data = {"Electronics" : {
        101 : {"name" : "Iphone", "price" : 80000,"stock" : 2},
        102 : {"name" : "Laptop", "price" : 40000,"stock" : 3}
    },
    "Clothing" :{
        201 : {"name" : "T-Shirt", "price" : 1000,"stock" : 5}
    }}

"""
Tasks: Access a specific product by category and ID: Manually access the Laptop in the Electronics category.

Add a new product to the store: Use the new_product tuple to add the Book to the Clothing category.

Convert a product name to uppercase: Change the name of the T-shirt product to uppercase using string functions.

Check if a product exists in the store: Use the get() method to check if Smartphone exists in the Electronics category.
"""

# Task 1
print("Access the Product",ecommerce_data["Electronics"][102]["name"],"manually -",ecommerce_data["Electronics"][102])

#task 2 -  208,    books   , 4200   , 5

new_product = input("Add your new product use separateer (,) - ").strip()
cleaned = [item.strip() for item in new_product.split(",")]
cleaned[0] = int(cleaned[0])


ecommerce_data["Clothing"][cleaned[0]] = {
                                            "name" : cleaned[1],
                                            "price" : int(cleaned[2]),
                                            "stock" : int(cleaned[3])
}

print(f"New Product have been added {cleaned[1]} with stock of {cleaned[3]}")
print(f"There is your final list - {ecommerce_data}")






