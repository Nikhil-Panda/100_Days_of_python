#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

total_bill = input('Welcome to the tip calculator.\nWhat was the total bill? ')

tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

no_people = int(input('How many people to split the bill? '))

total_cost = float(total_bill) + float(total_bill)*(tip/100)

per_person = "{:.2f}".format(total_cost/no_people,2)
print(f"Each person should pay: ${per_person}")