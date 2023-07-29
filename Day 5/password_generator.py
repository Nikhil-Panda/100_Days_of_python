#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password1=[]
password2=[]


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(1, nr_letters+1):
  password1.append(random.choice(letters))
for i in range(1, nr_symbols+1):
  password1.append(random.choice(symbols))
for i in range(1, nr_numbers+1):
  password1.append(random.choice(numbers))  
  
result = "".join(str(item) for item in password1)
print(result)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for i in range(1, nr_letters+1):
  password2.append(random.choice(letters))
for i in range(1, nr_symbols+1):
  password2.append(random.choice(symbols))
for i in range(1, nr_numbers+1):
  password2.append(random.choice(numbers))


random.shuffle(password2)
result = "".join(str(item) for item in password2)
print(result)