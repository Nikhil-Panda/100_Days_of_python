import random
import sys
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices_images =[rock, paper, scissors]

a_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if a_choice >= 3 or a_choice < 0: 
  print("You typed an invalid number")
  sys.exit()
  #to exit the program if user entry is invalid
else:
  print(choices_images[a_choice])

comp_choice = random.randint(0,2)
print("Computer chose:\n",choices_images[comp_choice])

if a_choice >= 3 or a_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif a_choice == 0 and comp_choice == 2:
  print("You win!")
elif a_choice == 2 and comp_choice == 0:
  print("You lose")
elif a_choice < comp_choice:
  print("You lose")
elif a_choice > comp_choice:
  print("You win!")
elif a_choice == comp_choice:
   print("It's a draw")



