n = int(input())
for i in range(n):
    x = int(input())
    if '21' in str(x):
        print('The streak is broken!')
    elif x%21==0:
        print('The streak is broken!')
    else:
        print('The streak lives still in our heart!')

