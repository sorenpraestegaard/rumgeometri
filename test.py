import random
def intervalTest(a,b,c):
    if a < b and b < c:
        return True
    else:
        return False

x = random.randint(0,10)
y = random.randint(0,10)
if intervalTest(y,x,5):
    print('What are the odds?!')
if intervalTest(5,y,x):
    print('Pretty small!')
