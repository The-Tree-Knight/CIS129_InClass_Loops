    
def get_integer(message):
    while True:
        try:
            user_input= int(input(message))
            return user_input
        except ValueError:
            print('Incorrect data entered, please re-attempt')

def main():
    while True:
        userNumber= get_integer('Enter a num: ')
        if (userNumber % 2) == 0:
            print('The number is even!')
        else:
            print('The number is odd!')
        print('Do you want to do it again?')
        again= input('Enter \'y\' to loop again: ')
        if again != 'y':
            break
        
main()
