# Input a sentence from the users. Count number of words in the sentence. Make sure it doesn't count spaces

user = str(input("Write your Story :"))
x = user.strip()
y = x.split(" ")
print(f"Number of sentance in your story are {len(y)}")
