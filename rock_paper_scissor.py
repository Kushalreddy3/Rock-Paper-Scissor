import random
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

game_images = [rock,paper,scissors]

my_choice = int(input("what do you choose 0 = rock, 1 = paper, 2 = scissors \n "))

if my_choice >=0 and my_choice <3:
    print("You choosed :")
    print(game_images[my_choice])

computer_choice = random.randint(0, 2)
print("computer choosed :")
print(game_images[computer_choice])

if my_choice >=3 and my_choice >0:
    print("wrong input")
    exit()
elif my_choice == 0 and computer_choice == 2:
    print("You won")
elif my_choice == 2 and computer_choice == 0:
    print("You lost")
elif my_choice > computer_choice:
    print("Youu won")
elif my_choice < computer_choice:
    print("You lost")
elif my_choice == computer_choice:
    print("It is a Draw")