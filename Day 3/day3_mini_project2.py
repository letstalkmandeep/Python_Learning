# Take the users first input and last input generate a email- id by concating the first 3 letters of the first name
#last three letter of the last name with domain @gmail.com 
#email must be in lowercase and has no spaces

first_name = str(input("First Name :")).strip()
last_name = str(input("Last Name :")).strip()

first_three_of_first = first_name[:3]

last_three_of_last = last_name[-3:]

print(f"Email : {first_three_of_first.lower()+last_three_of_last.lower()}@gmail.com")

