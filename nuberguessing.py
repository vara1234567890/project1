import random as rand
import random as rand

print('Welcome to number guessing game'.title().rjust(70,' '))

print()
print('Game Rules:')
print('1.Computer select a random number within 1 to 10')
print('2.to win the game Player Need to guess a number within 3 attempts.'.capitalize())
print()

while True:
    print("""1.Start Game\n2.Cancel """)
    opt=input('Select Option (1 or 2):')
    print()
    if opt=='1':
        DEVICE_GUESS=rand.randrange(1,10)
        print("Device selected a number start guessing !!!")
        print()
        ATTEMPTS=3
        for i in range(ATTEMPTS,0,-1):
            print(f'Remaing Attempts : {i}')
            print()
            GUESS=int(input('Your Guess : '))
            if GUESS == DEVICE_GUESS :
                print('Your Guess Is Correct')
                print('You Won The Game')
                break
            else:
                print('Incorrect Guess Try Again....')
        else:
            print()
            print(f'Device guess : {DEVICE_GUESS}')
            if i==0:
                print('You Lost the Game.....')
                print('Better Luck Next Time...')
        print()
    else:
        break
print('Game Cancelled...')
    