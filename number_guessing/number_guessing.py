from random import randint

low,high = 1,10
random_no: int = randint(low,high)
print(f'Guess a number from {low} to {high} : ')

while True:
    try:
        user_guess: int = int(input('Guess: '))
        if user_guess < 1 or user_guess > 10:
            raise ValueError("Number out of range:")
    except ValueError as e:
        print('Please enter a valid number')
        continue

    if user_guess > random_no:
        print('The number is lower')
    elif user_guess < random_no:
        print('The number is higher')
    else:
        print('Guessed right')
        break