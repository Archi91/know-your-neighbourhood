from data_manager import DataManager
from ui import UI
from community import Community
from voivodeship import Voivodeship
from county import County
from admin_division import AdminDivision
from statistic import Statistic

def main():
    DataManager.create_instances_from_data('malopolska.csv')
    # UI.welcome_screen()
    while 1:
        UI.print_menu()
        option = UI.user_input("Option: ")
        if option == '1':
            UI.print_result(UI.build_table(['','MAŁOPOLSKIE'], Statistic.total()))
            UI.user_input('\nPress Enter to continue...')
        elif option == '2':
            UI.print_result('\n'.join(Statistic.three_longest_city()))
            UI.user_input('\nPress Enter to continue...')
        elif option == '3':
            UI.print_result(Statistic.largest_number_of_commun())
            UI.user_input('\nPress Enter to continue...')
        elif option == '4':
            UI.print_result(Statistic.more_than_one_category())
            UI.user_input('\nPress Enter to continue...')
        elif option == '5':
            UI.print_result(UI.build_table(['LOCATION', 'TYPE'], Statistic.advanced_search(UI.user_input('Searching for: '))))
            UI.user_input('\nPress Enter to continue...')
        elif option == '0':
            UI.print_result('')
            break
        else:
            pass

if __name__ == '__main__':
    main()