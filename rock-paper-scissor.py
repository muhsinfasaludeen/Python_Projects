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
game_image=[rock,paper,scissors]
import random
user_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("user_choses")
if user_choice>2 or user_choice<0:
    print("invalid input")
else:
    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("Computers chooses")
    print(game_image[computer_choice])
    if user_choice == computer_choice:
        print("Draw")
    if user_choice == 1:
        if computer_choice == 0:
            
            print("You win")
        else:
            
            print("You lose")
    if user_choice == 0:
        
        if computer_choice == 1:
           
            print("You lose")
        else:
            
            print("You win")
    if user_choice == 2:
        
        if computer_choice == 0:
            
            print("You lose")
        else:
          
            print("You win")

    #another method
    # elif user_choice == 0 and computer_choice == 2:
    #   print("You win!")
    # elif computer_choice == 0 and user_choice == 2:
    #   print("You lose")
    # elif computer_choice > user_choice:
    #   print("You lose")
    # elif user_choice > computer_choice:
    #   print("You win!")
    # elif computer_choice == user_choice:
    #   print("It's a draw")
    