from re import search
from datetime import datetime
from time import sleep

from Wallet import Wallet
from Record import Record

def check(wallet: Wallet) -> bool:
    """Функция получает на вход кошелек и возращает истину если в нем не содержится записей"""
    if wallet.count_records == 0:
        print('Упс, кажется пусто :(\n')
        sleep(0.7)
        return True

def show_balance(wallet: Wallet) -> None:
    """Функция для вывода общего баланса кошелька и баланса по статьям """
    choice = input('Пожалуйста, выберите необходимый баланс:\n' \
                   '1 - Текущий баланс\n' \
                   '2 - Доходы\n' \
                   '3 - Расходы\n' \
                   '4 - Выйти в главное меню\n')
    match choice:
        case '1':
            print(f'Текущий баланс: {wallet.balance}\n')
        case '2':
            print(f'Доход за все время: {wallet.count("Доход")}\n')
        case '3':
            print(f'Расход за все время: {wallet.count("Расход")}\n')
        case '4':
            return

def new_records(wallet: Wallet) -> None:
    """Функция для внесение новой записи"""

    def record_write(category: str) -> None:
        """Функция для получения необходиой информации о внасимой записи"""
        while True:
            try:
                sum = float(input('Введите сумму:\n'))
                description = input('Введите описание:\n')
                record = Record(category, sum, description)
                break
            except ValueError as ex:
                print(ex)
            except TypeError:
                print('Упс, что-то пошло не так попробуйте еще раз')
        wallet.add(record)

    choice = input('Пожалуйста, выберите категорию:\n' \
                   '1 - Доходы\n' \
                   '2 - Расходы\n')
    match choice:
        case '1':
            record_write('Доход')
        case '2':
            record_write('Расход')

def find_record(wallet: Wallet) -> None:
    """Функция позволяющая осуществлять поиск по записям: по категории, дате или сумме"""

    if check(wallet):
        return

    def sort_records_category() -> None:
        """Функция для поиска запесей по категории"""
        choice = input('Выберети категорию:\n' \
                       '1 - Доходы\n' \
                       '2 - Расходы\n'
                       '3 - Выйти в главное меню\n')
        match choice:
            case '1':
                choice = "Доход"
            case '2':
                choice = "Расход"
            case '3':
                return

        for record in wallet.get_records():
            if record.category == choice:
                print(record)

    def sort_record_date() -> None:
        """Функция для поиска запесей по дате"""
        pattern = r'\b(?:[12]\d{3})\-(?:0[1-9]|1[012])\-(?:0[1-9]|[12]\d|3[01])\b'
        print('Введите дату в формате ГГГГ-ММ-ДД')
        while True:
            choice = input()
            if choice == 'exit':
                return
            elif not search(pattern, choice):
                print('Дата должна быть в формате ГГГГ-ММ-ДД. ' \
                      'Попробуйте еще раз или введите exit для выхода\n')
            else:
                for record in wallet.get_records():
                    if str(record.date) == choice:
                        print(record)
                return

    def sort_record_sum() -> None:
        """Функция для поиска запесей по сумме"""
        choice = input('Выберети тип поиска по сумме:\n' \
                       '1 - Больше указанной суммы\n' \
                       '2 - Меньше указанной суммы\n' \
                       '3 - Равно указанной сумме\n')

        while True:
            value_sum = input('Введите сумму:\n')
            if not value_sum.isdigit():
                print('Введите число')
            else:
                value_sum = int(value_sum)
                break

        match choice:
            case '1':
                for record in wallet.get_records():
                    if record.value_sum > value_sum:
                        print(record)
            case '2':
                for record in wallet.get_records():
                    if record.value_sum < value_sum:
                        print(record)
            case '3':
                for record in wallet.get_records():
                    if record.value_sum == value_sum:
                        print(record)

    choice = input('Выберете тип поиска:\n' \
                   '1 - по категории\n' \
                   '2 - по дате\n' \
                   '3 - по сумме\n'
                   '4 - Выйти в главное меню\n')
    match choice:
        case '1':
            sort_records_category()
        case '2':
            sort_record_date()
        case '3':
            sort_record_sum()
        case '4':
            return

def change_record(wallet: Wallet) -> None:
    """Функция позволяющая изменять выбранную запись в кошельке"""
    if check(wallet):
        return

    num_record = input(f'Введите номер записи для редактирования (Всего: {wallet.count_records})\n')
    if num_record.isdigit() and 0 < int(num_record) <= wallet.count_records:
        records = wallet.get_records_list()
        record = records[int(num_record) - 1]
        print('Выбранная запись:\n' \
              f'{record}')

        choice = input('Что необходимо отредактировать?\n' \
                      '1 - Дата\n' \
                      '2 - Категория\n' \
                      '3 - Сумма\n' \
                      '4 - Описание\n' \
                      '5 - Выйти в главное меню\n')

        def set_date() -> None:
            """Функция для изменения даты записи"""
            while True:
                value = input('Введите новую дату в формате ГГГГ-ММ-ДД:\n')
                try:
                    value = datetime.fromisoformat(value).date()
                    record.date = value
                    print('Дата успешно изменена!\n')
                    break
                except:
                    print('Неверный формат даты!\n')

        def set_category() -> None:
            """Функция для изменения категории записи"""
            value = "Доход" if record.category == "Расход" else "Расход"

            match value:
                case 'Доход':
                    wallet.balance += record.value_sum * 2
                case 'Расход':
                    try:
                        wallet.balance -= record.value_sum * 2
                    except ValueError as ex:
                        print(ex)
                        raise ValueError

            record.category = value
            print('Категория успешно изменена!')

        def set_sum() -> None:
            """Функция для изменения суммы записи"""
            while True:
                try:
                    value = float(input('Введите новое значение суммы\n'))
                    if value < 0:
                        print('Сумма не может быть отрицательной\n')
                        continue
                    break
                except (TypeError, ValueError):
                    print('Пожалуйста, введите число!\n')

            if record.category == 'Доход':
                wallet.balance += (value - record.value_sum)
            else:
                wallet.balance -= (value - record.value_sum)
            record.value_sum = value

        def set_description() -> None:
            """Функция для изменения описания записи"""
            value = input('Введите новое описание\n')
            record.description = value

        match choice:
            case '1':
                set_date()
            case '2':
                try:
                    set_category()
                except ValueError:
                    return
            case '3':
                set_sum()
            case '4':
                set_description()
            case '5':
                return

        wallet.add_list(records)

    else:
        print('Введеные данные некорректны!\n')
