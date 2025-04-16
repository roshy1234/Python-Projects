import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    rolls: list[int] = []
    for i in range(amount):
        rand: int = random.randint(1,6)
        rolls.append(rand)
    return rolls

while True:
    try:
        n = input('How many times do you want to roll dice? ')
        if n.lower() == 'exit':
            print('Thanks for playing')
            break
        a = int(n)
        l = roll_dice(a)
        print(*l)
        print('Total : ',sum(l))
    except ValueError:
        print('Please enter a valid number')

