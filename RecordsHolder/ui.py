from RecordsHolder.model import Record

def display_menu_get_choice(menu):
    # Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
    while True:
        print(menu)
        choice = input('Enter a choice: ')
        if menu.is_valid(choice):
            return choice
        else:
            print('Not valid, try again.')

def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def get_new_record_info():
    playerName = input('Enter Player Name: ')
    country = input("Enter player's Country: ")
    catches = int(input('Enter number of catches: '))
    return Record(playerName, country, catches)

def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)

def show_records(records):
    if records:
        for record in records:
            print(record)
    else:
        print('None to display')

