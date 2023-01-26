def main_menu():
    commands = ['Показать все контакты', 'Открыть файл', 'СОхранить файл', 'Новый контакт',
                'Изаенить контакт', 'удалить контакт', 'Найти контакт', 'Выйти из программы']
    print('Выберете пункт меню: ')

    for i in range(len(commands)):
        print(f'\t{i+1}.{commands[i]}')
    user_input = int(input('\nВведите пунет меню: '))
    if 1 <= user_input <= len(commands):
        return user_input
    else:
        print(f'Введите корректное значение от 1 до {len(commands)}: ')


def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        count = 1
        for item in phone_book:
            print(f'{count}.  {item[0]} {item[1]} ({item[2]}) ')
            count += 1
    else:
        print('Телефонная книга пуста или не загружена')


def load_success():
    print('Телефонна книга загруженна умешно')


def save_success():
    print('Телефонна книга сохранена успешно')


def new_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите comment ')
    return name, phone, comment


def find_contact():
    search = input('Введите искомое значение: ')
    return search


def change_contact():
    global phone_book
    change = (int(input('Введите номер контакта который надо изменить: ')))-1
    return change
    


def change_list_contact():
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите comment ')
    return name, phone, comment


def delete_contact():
    delete = (int(input('Введите номер контакта который надо удалить: ')))-1
    return delete
