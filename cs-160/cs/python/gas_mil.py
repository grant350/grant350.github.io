
def test():
    test_variable = ['stuff','is','cool']
    inp = input('Test a word: ')
    if (isinstance(inp,str) == True):
        print('is a string True')
    if inp in test_variable:
        print (inp)
        return True;
x = test()

if (x==True):
    print('true')
