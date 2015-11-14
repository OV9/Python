import random

Again = 'y'
while Again == 'y':

    Iterations = 1
    Turn = input('Who should guess (1 = You ; 2 = PC (default)): \n')
    Start = int(input('What\'s the lower limit number of the challenge:' + '\n'))
    End = int(input('What\'s the higher limit number of the challenge:' + '\n'))
    Low = Start
    High = End
    Current_Number = random.randint(Start, End)
# code for user guessing starts here
    if Turn == '1':
        print('OK. I thought of a number and you will guess it')
        Userguess = int(input('What is your first guess: \n'))
        while Userguess != Current_Number:
            if Userguess > End or Userguess < Start:
                 print('The number has to be between {0} and {1} remember?'.format(Start, End))
            elif Userguess > Current_Number:
                print ('The number is lower')
            elif Userguess < Current_Number:
                print ('The number is higher')
            Userguess = int(input('Guess again: \n'))
            Iterations += 1
        else:
            print ('you got it in {0} guesses, my number was indeed {1}'.format(Iterations, Userguess))
        Again = input('Do you want to restart the game (y/n): \n')
# code for PC guessing starts here
    else:
        input('OK. Think of a number and I will guess it. Press Enter when you are ready ...')
        Answer = input('is your number {0}? (y/up/down): \n'.format(Current_Number))
        while Answer != 'y':
            if Answer == 'up':
                Low = Current_Number + 1
                if Low > End:
                    print("The number can't be higher than {0}".format(End))
                    break
                else:
                   Current_Number = random.randint(Low, High)
            if Answer == 'down':
                High = Current_Number - 1
                if High < Start:
                    print('The number can\'t be lower than {0}'.format(Start))
                    break
                else:
                    Current_Number = random.randint(Low, High)
            if Answer == 'y':
                print('Got You! I knew your number was {0}. I did it in {1} guesses'.format(Current_Number, Iterations))
                break
            if High == Low or Answer == 'y':
                print('Got You! I knew your number was {0}. I did it in {1} guesses'.format(Current_Number, Iterations))
                break
            Answer = input('is your number {0}? (y/up/down): \n'.format(Current_Number))
            Iterations += 1
        else:
            print('I am that good! I knew your number was {0}. I did it in one guess'.format(Current_Number))
    Again = input('Do you want to restart the game (y/n): \n')