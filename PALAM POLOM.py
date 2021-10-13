import random
import sys
print(' !Lets go play palam polom pilish !')
while True:
    comp1 = random.randint(1, 2)
    comp2 = random.randint(1, 2)
    user = int(input('your choose :'))
    if comp1==comp2 and comp1!=user :
        print('user lose!!')
    elif comp1==user and comp1!=comp2 :
        print('computer 2 lose ')
    elif comp2==user and comp2!=comp1 :
        print('computer 1 lose ')
    elif comp1==comp2==user:
        print('All the gamer same\nTry your luck again...!')
    elif user!=1 or user!=2 :
        print('please enter Only numbers 1 or 2')
        sys.exit(0)