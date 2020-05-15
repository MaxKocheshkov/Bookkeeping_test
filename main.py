from application import salary
from db import people
from datetime import datetime


def main():
    print(f'Текущее время: {datetime.utcnow()}')
    while True:
        user_input = input('Введите команду: ')
        if user_input == 's':
            salary.calculate_salary()
        elif user_input == 'p':
            people.get_employees()
        elif user_input == 'q':
            print('До свидания!')
            break


if __name__ == '__main__':
    main()
