# detect floating point number
n = input()
if n.count('.') == 1:
    n = n.split('.')
    if n[0].isdigit() and n[1].isdigit():
        print('True')
    else:
        print('False')
else:
    print('False')