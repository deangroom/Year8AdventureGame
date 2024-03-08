This is a modified verions of Getting User input

Here, a function is created to manage the user input.

The first code block is responsible for displaying the possible actions that a player can take in the game.
The actions list contains the available actions that the player can choose from.
The for loop iterates over each action in the actions list and prints it out.

print("You can do the following actions: ")
for action in actions:
    print(action)

This code block is used to get the user's input in the game.
It calls the get_user_input() function to retrieve the user's input and assigns it to the user_input variable.

The user's input is then printed as a debug message for testing purposes.

#get the user input
user_input = get_user_input()
print(f"DEBUG: This is the action returned from the function {user_input}")

This means we can now call a fuction for the whole user_input routine and not have to keep re-making it. All that happens is the fuction returns the input to the mainline of the program using RETURN and then the variable. Ie, the function RETURNS the answer or it could be a decision or calculation if we wanted. RETURNing values after a function has been run is a common method.