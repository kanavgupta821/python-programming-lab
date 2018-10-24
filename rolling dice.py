import random
game_start = input("would you like to roll the dice?")
def dice_roll():
 print("your number is: " + str(random.randint(1,6)))
 global play_again
 play_again = input("would you like to play again?")
if game_start == "yes":
 dice_roll()
 while play_again == "yes":
  dice_roll()
elif game_start == "no":
 print("game over")
else:
 print("input not recognised")