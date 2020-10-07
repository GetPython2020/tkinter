import random

x = random.randint(1,100)
num = int(input('enter your guess: '))
count = 0
while x != num:
    if num > x:
        print('Guess too big')
    else:
        print('Guess too small')
    print('Please try again')
    num = int(input('guess again: '))
    count +=1
print('guess correct')
print(f'your total guess is {count} times')

