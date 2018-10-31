import random as rd
import os

def start():
  while True:
    try:
      user_input = raw_input('please enter a string, Rock, Paper,Scizors,Gun:');
      user_input.lower();
      c = isinstance(user_input, str)
      print(c)
      if (c == True):
          print("your input is " + user_input)
          return user_input
          print('is a string')
    except Exception:
      print('sorry bad input,you must type  cap or lower with  correct spelling.    Try Again')
start();
value=int(0);


def fix(user_input):
  user_input =start();
  if (user_input == 'rock'):
    value = 0;
    return value;
    print('your value was rock which is == 0')
  elif (user_input == 'paper'):
    value = 1
    return value
    print('your value was paper which is == 1')
  elif (user_input == 'scissors'):
    value = 2
    return value
    print('your value was scizors which is == 2')
  elif (user_input == 'gun'):
    value = 3
    return value
    print('your value was gun which is == 3')

def random():
    random_num = random.ranint(0,3)
    if random_num <= user_input:
        print('you have one the game!!!!!')
