import random as r 

numbers = [1,2,3,4,5,6,7,8,9,0]
special_symbols = ["@","#","$","&","!"]
Lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def strong_password():
    password = str(r.choice(numbers)) + str(r.choice(numbers)) + r.choice(special_symbols) + r.choice(special_symbols) + r.choice(Lowercase) + r.choice(Uppercase) + str(r.choice(numbers)) + str(r.choice(numbers))
    print(password)

strong_password()