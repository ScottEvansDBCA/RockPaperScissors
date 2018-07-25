'''This is a Rock Paper Scissors game.
You select your option, the computer has theirs at the ready and see who wins!'''

def initial_input():
    user_choice = input("Rock... Paper... Scissors...\nChoose r, p or s to make your choice\nYou're going with: ")
    return user_choice

def check_who_won(comp_choice, usr_choice):
    if usr_choice == 'R':
        if comp_choice == 1:
            return "D"
        if comp_choice == 2:
            return "L"
        if comp_choice == 3:
            return "W"
    elif usr_choice == 'P':
        if comp_choice == 1:
            return "W"
        if comp_choice == 2:
            return "D"
        if comp_choice == 3:
            return "L"
    elif usr_choice == "S":
        if comp_choice == 1:
            return "L"
        if comp_choice == 2:
            return "W"
        if comp_choice == 3:
            return "D"
    else:
        return "ERROR"

total_score = 0
computer_score = 0

def main_logic():
    import random
    computer_choice = random.randint(1,3)
    global computer_score
    global total_score
    user_choice = initial_input().upper()
    result = check_who_won(computer_choice, user_choice)
    if result == "ERROR":
        print("You have not made a valid selection, please try again.")
    elif result == "W":
        total_score += 1
        print("Congratulations, you win!")
    elif result == "D":
        print("Well at least you didn't lose this time!")
    elif result == "L":
        computer_score += 1
        print("Unlucky! You lose.")
    print("Your score is: {}\nThe computer is on: {}" .format(total_score, computer_score))
    play_again = input("Would you like to play another game? Y/N: ")
    if play_again.upper() == "Y":
        main_logic()
    else:
        pass

main_logic()
