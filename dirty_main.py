from application.salary import *
from db.people import *
from datetime import datetime


def dirty_main():
    print(f'Текущее дата/время: {datetime.utcnow()}')
    while True:
        user_input = input('Введите команду: ')
        if user_input == 's':
            calculate_salary()
        elif user_input == 'p':
            get_employees()
        elif user_input == 'q':
            print('До свидания!')
            break


if __name__ == '__main__':
    dirty_main()
