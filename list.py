num = []
add = 'add'
del_ = 'delete'
dup = 'duplicate'
di = 'display'



while True:
    ip =  input('>')
    ip = ip.lower()
    
    if ip == add:
        a_num = int(input('Enter a number to input :'))
        num.append(a_num)
    
    elif ip == del_:
        a_num = int(input('Enter a number to delete :'))
        if a_num not in num:
            print('Number not present')
        else:
            num.pop(a_num)
    
    elif ip == dup:
        dis = input('Do you need a copy (y/n):')
        if len(dis)>1:
            print('Enter a valid input!!')
        elif dis == 'y':
            num_copy = num.copy()
            print('New list num_copy created')
        else:
            print(f"exiting")
    
    elif ip == di:
        print(num)
    
    else:
        print('Enter a valid input')


