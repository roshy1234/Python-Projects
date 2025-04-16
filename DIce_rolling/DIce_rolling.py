from random import randint
while True:
    n = input('How many times do you want to roll dice? ')
    a = int(n)
    if n == 'exit':
        print('Thanks for playing')
        break
    i = 0
    while i<a:
        rand = randint(1,6)
        if(i == a-1):
            print(rand)
            break
        print(rand,end=', ')
        i=i+1
