import view
import model


def start():
    user_choise = 0
    while user_choise != 8:
        user_choise = view.main_menu()

        match user_choise:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                change = view.change_contact()
                change_list = list(view.change_list_contact())
                model.change_phone_book(change, change_list)
            case 6:
                delete = view.delete_contact()
                model.delete_contact(delete)
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)
