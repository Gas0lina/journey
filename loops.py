name = 'Yogesh'
age = '20'
help = 'help'
while True:
    U_in = input('>')
    if name == U_in:
        print('Welcome Yogesh')
        break
    elif name != U_in:
        print('WHO are u')
        print('Please Enter your age')
        U_in = input('>')
        if U_in == age:
            print('Enter corect name,Yogesh!')
            break
        else:
            print('Please Exit')
            break
    else:
        if U_in == help:
            print("ENTER YOUR NAME")
