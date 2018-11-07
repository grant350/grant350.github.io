import random;
import os;
import turtle;
rpsg = ['rock','paper','scissors','gun']

print ('you will begin by picking numbers 0-3')
print (rpsg[0] + ' 0 ', rpsg[1] + ' 1 ', rpsg[2] + ' 2 ',rpsg[3] + ' 3 ')



def computer(answer):
    print(answer)
    random_num = random.randint(0,3)
    if (random_num < answer):
        print ('you have won the game')
    elif(random_num == answer):
        print('tie breaker')
    else:
        print('you have lost the game')




def start():
    value = 0
    corrected_value = 0
    user_input=input('please put your guess here:')
    if  (isinstance(user_input,str) == True and user_input.isdigit() != True ):
        user_input.lower();
        print('its a string ' + user_input)
        for i in range(len(rpsg)):
            if (rpsg[i] == user_input):
                value=i
                corrected_value = value
                print(value)
                print(corrected_value)
                return value;

    if (isinstance(user_input,int) == True or user_input.isdigit() == True):
        print('its an int ' + str(user_input))
        value = int(user_input)
        user_input = int(user_input)
        if (value <= 3 and value >=0):
            print('correct')
            corrected_value = user_input
            print (value)
            print(corrected_value)
            return value;
            return computer(corrected_value)
            

start()
