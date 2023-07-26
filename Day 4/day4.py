# #randomization and Lists
import random
import my_module

print(random.randint(1,100))
print(my_module.pi)

print(round(random.random(),2))  #print a random float between 0 and 1



#prnt a float between 0 and 5 
random_number = random.randint(0,5)
random_float = random.random()

random_float *= random_number
print(round(random_float,2), "between 0 and 5")


#heads or tails
toss_value = random.randint(0,1)
if toss_value == 1:
    print("Heads")
else:
    print("Tails")
    

#random choice from a list
names_line = input("Enter names in a row seperated by commas: ")
names = names_line.split(', ')

print(random.choice(names), "is the choice")



# splitting a number into individual digits
#for 3-digit - 100, 4-digit - 1000 and so on.
number = 2345
digit1 = number // 1000 #thousand's place
digit2 = (number //100) % 10 #hundred's place
digit3 = (number // 10) % 10 #ten's place
digit4 = number % 10 #one's place

print(digit1,digit2, digit3, digit4)





# Some condition to check and exit the program.
import sys
condition = True

if condition:
    print("Condition is satisfied. Exiting the program.")
    sys.exit()

# Code beyond this point won't be executed if the condition is True
print("This line won't be printed if the condition is satisfied.")




