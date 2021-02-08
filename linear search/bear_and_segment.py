n = int(input())
for _ in range(n):
    s = input()
    s=list(s)

    if '1' in s:
        x = s.index('1')
        #print('x = {}'.format(x))
    else:
        print('NO')
        continue
    
    if '0' in s[x:]:
        y = s[x:].index('0')+x
        #print('y = {}'.format(y))
    else:
        print('YES')
        continue

    if '1' in s[y:]:
        print('NO')
    else:
        print('YES')
    