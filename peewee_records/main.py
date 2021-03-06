from peewee_records import records_store as store, ui as ui
from peewee_records.records_store import RecordError
from peewee_records.menu import Menu

QUIT = 'Q'

def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == QUIT:
            break

def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add a record', add_record)
    menu.add_option('2', 'Search For Record Holder', search_record_holder)
    menu.add_option('3', 'Show all Plyers', show_all_players)
    menu.add_option('4', 'Update a Record', update_record)
    menu.add_option('5', 'Delete a Record', delete_record)
    menu.add_option(QUIT, 'Quit', quit_program)

    return menu

def add_record():
    new_record = ui.get_new_record_info()
    try:
        store.add_record(new_record)
        ui.message('Added successfully')
    except RecordError as e:
        ui.message(e)

def search_record_holder():
    search_term = ui.ask_question('Enter player name, will match partial names ')
    matches = store.record_holder_search(search_term)
    ui.show_records(matches)

def show_all_players():
    players = store.get_all_records()
    ui.show_records(players)

def update_record():
    search_term = ui.ask_question('Enter player name, will match partial names ')
    new_number_of_catches = int(ui.ask_question('Enter number of catches: '))
    # matches = store.record_holder_search(search_term)
    store.update_number_of_catches(search_term, new_number_of_catches)

def delete_record():
    search_term = ui.ask_question('Enter the name of the player you want to delete')
    store.delete_record_holder(search_term)

def quit_program():
    ui.message('Thanks and bye!')



if __name__ == '__main__':
    main()