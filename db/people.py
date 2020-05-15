from db import people_data


def get_employees():
    get_user_dep = int(input('Введите номер отдела: '))
    for num_dep in people_data.departments.keys():
        if get_user_dep == num_dep:
            print(f'Сотрудники отдела {get_user_dep}: {people_data.departments[num_dep]}')


if __name__ == '__main__':
    get_employees()
