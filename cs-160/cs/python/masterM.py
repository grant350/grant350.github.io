import random;
hot_spot=0;
colors = ['R','G','B','O','P']
other_colors =['RED','GREEN','BLUE','ORANGE','PURPLE']
guesser_array=[]


def code_maker():
    code_maker_array=[]
    for i in range(4):
        ran = random.randint(0,4)
        print (ran)
        code_maker_array.append(colors[ran])
        print(code_maker_array)
    return code_maker_array
x = code_maker()


def code_breaker():
    trys = 0;
    cbi = input('please put in r,g,b,o,p or red,green,blue,orange,purple_ ')
    cbi = cbi.upper()
    if ( isinstance(cbi,str) == True):
        print ('it is a string')
        print (cbi)
        for i in range(4):
            if (len(cbi)>=3):
                a = other_colors[i].find(cbi)
            else:
                b = colors[i].find(cbi)
            if (a >= 0 or b >= 0):
                print ('yummmeiabui aebfiahfu dsdsde')

y = code_breaker()


"""
def code_checker(x):
    print (x)

code_checker(x)
"""
