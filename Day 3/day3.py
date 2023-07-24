'''
#conditional statements
height = int(input("enter your height in cm? :"))
bill = 0
if height>120:
    age = int(input("how old are you? :"))
    #if_block-1
    if age<12:
        bill = 5
        # print("please pay $5")
    elif age<=18:
        bill = 7
        # print("please pay $7")
    else:
        bill = 12
        # print("please pay $12")
    #end
    want_photo = input("want a photo taken for $3?(Y or N):")
    #if_block-2
    if want_photo.lower() == 'y':
        bill += 3
    #end
    print(f"your total bill is ${bill}")
else:
    print("sorry, but it is dangerous for you to ride on the roller coaster")



#leap year
year= int(input('what year do you want to check?:'))
if year%4 ==0:
    if year%100 == 0:
        if year%400 == 0 :
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")



# pizza deliveries
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size.lower() == 's':
    bill = 15
elif size.lower() == 'm':
    bill = 20
else: 
    bill = 25
if add_pepperoni.lower() == 'y':
    if size.lower() == 's':
        bill += 2
    else:
        bill += 3
if extra_cheese.lower() == 'y':
    bill += 1
print(f"Your final bill is: ${bill}")


##count function
count_a = "angela".count('a')
print(count_a)
'''

combined_lower_name = "kanye westkim kardashian"
true_score = combined_lower_name.count('l') + combined_lower_name.count('o') + combined_lower_name.count('v') + combined_lower_name.count('e')
print(true_score)


#love score calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
combined_lower_name = combined_name.lower()

true_score = combined_lower_name.count('t')+combined_lower_name.count('r')+combined_lower_name.count('u')+ combined_lower_name.count('e')
love_score = combined_lower_name.count('l')+ combined_lower_name.count('o') + combined_lower_name.count('v') + combined_lower_name.count('e')

total_score = int(str(true_score)+str(love_score))
if total_score <10 or total_score>90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score>=40 and total_score<50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")










#in the code line     
'''if age<12:
        print("please pay $5")
    elif age<=18:
        print("please pay $7")
the elif statement filters out values less than 18 but greater than 12
'''
'''
Leap year if :

on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400
'''