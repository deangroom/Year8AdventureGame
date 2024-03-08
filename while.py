while True:
    choice=input('press Y or N to continue')
    #convert the choice to lower case
    choice=choice.lower()

    if choice=='y':
        print('You chose to continue')
        break
    elif choice=='n':
        print('You chose to quit')
        break
    else:
        print('I do not understand that choice')

print("Game over!")

