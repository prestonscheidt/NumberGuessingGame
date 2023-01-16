
import random
from art import logo


easy_turns = 10
hard_turns = 5

def check_answer(guess,answer,turns):
  if guess > answer:
    print("Guess too high")
    return turns -1
  if guess < answer:
    print("Guess is too low")
    return turns -1
  else:
    print("You guessed it right!")
    turns == 0

def set_difficulty():
  level = input("Choose 'hard' or 'easy'\n")
  if level == "easy":
    return easy_turns
  else:
    return hard_turns

def game():
  print(logo)
  print("Welcome to Guessing game. The answer is between 1 and 100")
  answer = random.randint(1,100)
  print(f"Testing, answer is {answer}")
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} left")
    guess = int(input("Make a guess\n"))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("No more guesses")
      return
    elif guess != answer:
      print("guess again")

game()
  

