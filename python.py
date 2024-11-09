import random as r

damtxveva = False
cda = 0
while damtxveva == False:
    l_n = []
    ch_n = []
    while len(l_n) < 7:
        x = r.randint(1, 36)
        if x not in l_n:
            l_n.append(x)
    while len(ch_n) < 7:
        x = r.randint(1, 36)
        if x not in ch_n:
            ch_n.append(x)
    if l_n == ch_n:
        damtxveva = True
        print('daemtxva')
    cda+=1

    print(l_n)
    print(ch_n)
    print( cda)