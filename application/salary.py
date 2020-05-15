def calculate_salary():
    salary = int(input("Введите заработанную плату в месяц: "))
    bonus = int(input("Введите количество премий за год: "))
    prize = bonus * salary
    final_payout = 12 * salary + prize
    print(f'{final_payout}')


if __name__ == '__main__':
    calculate_salary()