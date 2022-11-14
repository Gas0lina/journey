def add():
    sum = num1 + num2
    print(f'{num1}+{num2}={sum}')
def sub():
    dif = num1 - num2
    print(f'{num1}+{num2}={dif}')
def mull():
    mul = num1 * num2
    print(f'{num1}+{num2}={mul}')
def div():
    dv = num1 / num2
    print(f'{num1}+{num2}={dv}')
      
num1 = int(input('i] Enter variable :'))
num2 = int(input('ii]Enter variable :'))
while True:

    ip = input('>')
    if ip == '+':
        add()
    elif ip =='-':
        sub()
    elif ip == '*':
        mull()
    elif ip == '/':
        div()
    elif ip == 'quit' or ip == 'exit':
        print(f'Quiting')
        break
    else:
        print('Enter a valid input')
    
    
    
    
