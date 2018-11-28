import random
from math import sqrt

done = False
v = 0
while not done:
    msg = input('Skriv her >')

    if msg.startswith('quit'):
        done = True
    elif msg.startswith('hjælp'):
        print('Dette program kan arbejde med en enkelt talværdi')
        print('For at ændre talværdien skriver man "værdi x". Så gemmes værdien "x".')
        print('Andre kommandoer:')
        print('  vis')
        print('  dobbel')
        print('  mindre end x')
        print('  større end x')
        print('  tilfældig')
        print('  lige')
        print('  ulige')
        print('  dividerer x')
        print('  primtal')

    elif msg.startswith('vis'):
        print('Værdien er nu {}'.format(v))

    elif msg.startswith('værdi'):
        m = msg.split(' ')
        v = float(m[1])
        print('Værdien er nu {}'.format(v))

    elif msg.startswith('dobbel'):
        v = v * 2
        print('Værdien er nu {}'.format(v))

    elif msg.startswith('mindre end'):
        m = msg.split(' ')
        x = float(m[2])
        if v < x:
            print('Værdien {} er mindre end {}'.format(v, x))
        else:
            print('Værdien {} er ikke mindre end {}'.format(v, x))

    elif msg.startswith('større end'):
        m = msg.split(' ')
        x = float(m[2])
        if v > x:
            print('Værdien {} er større end {}'.format(v, x))
        else:
            print('Værdien {} er ikke større end {}'.format(v, x))

    elif msg.startswith('tilfældig'):
        v = random.random()*10
        print('Værdien er nu {}'.format(v))

    elif msg.startswith('lige'):
        t = int(v)
        if t % 2 == 0:
            print('{} er et lige tal'.format(t))
        else:
            print('{} er ikke et lige tal'.format(t))
    elif msg.startswith('ulige'):
        t = int(v)
        if t % 2 == 1:
            print('{} er et ulige tal'.format(t))
        else:
            print('{} er ikke et ulige tal'.format(t))

    elif msg.startswith('dividerer'):
        m = msg.split(' ')
        x = int(m[1])
        if int(x) % int(v) == 0:
            print('{} går op i {}'.format(v,x))
        else:
            print('{} går ikke op i {}'.format(v,x))

    elif msg.startswith('primtal'):
        prim = True
        t = int(v)
        if t < 2 or t % 2 == 0:
            print('{} er ikke et primtal'.format(t))
            prim = False
        else:
            for x in range(2, int(sqrt(t)) + 1):
                if t % x == 0:
                    print('{} er ikke et primtal'.format(t))
                    prim = False
                    break
            if prim:
                print('{} er et primtal'.format(t))
