#https://www.higherlowergame.com/

from re import A
from art import logo, vs
from game_data import data
import random
from replit import clear
score = 0

# format the account data into printable format

def format_data(account):
  """Takes the account data and returns the printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess,a_followers,b_followers):
  """Checks followers against user's guess"""
  if a_followers > b_followers:  
    return guess == "a"
  else:
    return guess == "b"   


game_should_continue = True 
account_b = random.choice(data)
print(logo)

while game_should_continue:
  # generate a random choice
  account_a = account_b
  account_b = random.choice(data) 
  while account_a == account_b:
      account_b = random.choice(data)

  print(f"Compare A : {format_data(account_a)}")
  print(vs)
  print(f"Compare B : {format_data(account_b)}")

  # Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # check if the user is right or wrong
  ## get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count,b_follower_count)   # True, False


  clear()
  print(logo)
  # score Keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")







