n = int(input())
for i in range(n):
    s = input()
    x=s.count('SUVO')
    y=s.count('SUVOJIT')
    print('SUVO = {}, SUVOJIT = {}'.format(x-y,y))
