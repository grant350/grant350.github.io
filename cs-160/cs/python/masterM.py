import random ;
hot_spot=0;
trys = 0;
colors = ['R','G','B','O','P']
code_maker_array=[]
other_colors =['Red','Green','Blue','Orange','Purple']
user_color_array=[]





def code_maker():
    print ('code maker turn')

    for i in range(4):
        rand = colors[random.randint(0,4)];
        print rand;
        code_maker_array.append(rand)
        print code_maker_array


def code_breaker(colors,other_colors):
    print ('code breaker turn')

    while True:
          try:
               for i in range(4):
                   print(i)
                   breaker = raw_input('R for red G for green P for purple B for blue O for orange:')
                   user_color_array.append(breaker)
                   print (breaker)
                   print (user_color_array)
                   return breaker;
          if breaker.upper() not in (colors,other_colors):
                print("Not an appropriate choice.")
                print('you must use R for red G for green P for purple B for blue O for orange')
          else:
               break


def compare(code_maker_array):
    print ('nothing')

    if (trys == 8):
        print('Game Over')
    trys = trys +1;

code_maker()
code_breaker()
