import random
user = input("What do you want to choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n")
computer = random.randint(0,2)
if user == "0":
  print(rock)
  print("computer choose")
  if computer == 0:
    print(rock)
    print("It's a draw.")
  elif computer == 1:
    print(paper)
    print("You lose.")
  elif computer == 2:
    print(scissors)
    print("You win.")
elif user == "1":
  print(paper)
  print("computer choose")
  if computer == 0:
    print(rock)
    print("You win.")
  elif computer == 1:
    print(paper)
    print("It's a draw.")
  elif computer == 2:
    print(scissors)
    print("You lose.")
elif user == "2":
  print(scissors)
  print("computer choose")
  if computer == 0:
    print(rock)
    print("You lose.")
  elif computer == 1:
    print(paper)
    print("You win.")
  elif computer == 2:
    print(scissors)
    print("It's a draw.")
else:
  print("Invalid choice.")