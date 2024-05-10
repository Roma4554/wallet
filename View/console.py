from re import search

from wallet.Wallet import Wallet
import wallet.Model as model


def show_balance(wallet: Wallet) -> None:
    """Функция для вывода общего баланса кошелька и баланса по статьям """

    choice = input("Пожалуйста, выберите необходимый баланс:\n"
                   "1 - Текущий баланс\n"
                   "2 - Доходы\n"
                   "3 - Расходы\n"
                   "4 - Выйти в главное меню\n")

    print(model.show_balance(wallet, choice))


def new_records(wallet: Wallet) -> None:
    """Функция для внесения новой записи"""

    def record_write(category: str) -> None:
        """Функция для получения необходимой информации о вносимой записи"""
        while True:
            try:
                answer = input('Введите сумму или exit для выхода:\n')
                if answer.lower() == 'exit':
                    return
                try:
                    sum = float(answer)
                except ValueError:
                    raise ValueError('Пожалуйста, введите число')
                description = input('Введите описание:\n')
                model.new_records(wallet, category, sum, description)
                print('Запись успешно добавлена!')
                break
            except ValueError as ex:
                print(ex)
            except OverflowError as ex:
                print(ex)
                return
            except TypeError:
                print('Упс, что-то пошло не так попробуйте еще раз')

    choice = input('Пожалуйста, выберите категорию:\n'
                   '1 - Доходы\n'
                   '2 - Расходы\n')
    match choice:
        case '1':
            record_write('Доход')
        case '2':
            record_write('Расход')


def find_record(wallet: Wallet) -> None:
    """Функция позволяющая осуществлять поиск по записям: по категории, дате или сумме"""

    if model.check_records_list(wallet):
        print('Упс кажется пусто :(')
        return

    def sort_records_category() -> None:
        """Функция для поиска записей по категории"""
        choice = input('Выберете категорию:\n'
                       '1 - Доходы\n'
                       '2 - Расходы\n'
                       '3 - Выйти в главное меню\n')
        records = model.sort_records_category(wallet, choice)
        if records:
            print('\n'.join(records))

    def sort_record_date() -> None:
        """Функция для поиска записей по дате"""

        while True:
            """Функция для поиска записей по дате"""
            pattern = r'\b(?:[12]\d{3})\-(?:0[1-9]|1[012])\-(?:0[1-9]|[12]\d|3[01])\b'
            print('Введите дату в формате ГГГГ-ММ-ДД')
            while True:
                choice = input()
                if choice == 'exit':
                    return
                elif not search(pattern, choice):
                    print('Дата должна быть в формате ГГГГ-ММ-ДД.\n'
                          'Попробуйте еще раз или введите exit для выхода.\n')
                else:
                    print('\n'.join(model.sort_record_date(wallet, choice)))
                    return

    def sort_record_sum() -> None:
        """Функция для поиска записей по сумме"""
        choice = input('Выберете тип поиска по сумме:\n'
                       '1 - Больше указанной суммы\n'
                       '2 - Меньше указанной суммы\n'
                       '3 - Равно указанной сумме\n')

        while True:
            value_sum = input('Введите сумму:\n')
            if not value_sum.isdigit():
                print('Введите число')
            else:
                value_sum = int(value_sum)
                break
        records = model.sort_record_sum(wallet, choice, value_sum)
        if records:
            print('\n'.join(records))

    choice = input('Выберете тип поиска:\n'
                   '1 - по категории\n'
                   '2 - по дате\n'
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

    if model.check_records_list(wallet):
        print('Упс кажется пусто :(')
        return

    num_record = input(f'Введите номер записи для редактирования (Всего: {wallet.count_records})\n')
    if num_record.isdigit():
        try:
            record = model.get_record(wallet, int(num_record))
        except IndexError as ex:
            print(ex)
            return
        print('Выбранная запись:\n'
              f'{record}')

        choice = input('Что необходимо отредактировать?\n'
                       '1 - Дата\n'
                       '2 - Категория\n'
                       '3 - Сумма\n'
                       '4 - Описание\n'
                       '5 - Выйти в главное меню\n')

        def set_date() -> None:
            """Функция для изменения даты записи"""
            while True:
                value = input('Введите новую дату в формате ГГГГ-ММ-ДД:\n')
                try:
                    model.set_date(value, record)
                    print('Дата успешно изменена!\n')
                    break
                except:
                    print('Неверный формат даты!\n')

        def set_category() -> None:
            """Функция для изменения категории записи"""
            try:
                model.change_category(wallet, record)
            except ValueError as ex:
                print(ex)
                raise ValueError

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

            try:
                model.set_sum(wallet, record, value)
            except ValueError as ex:
                print(ex)

        def set_description() -> None:
            """Функция для изменения описания записи"""
            model.set_description(record)

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

        model.save_change(wallet, record, int(num_record))

    else:
        print('Введенные данные некорректны!\n')


def start_view():
    wallet_name = input('Введите название кошелька:\n')

    wallet = Wallet(wallet_name)

    print(f'Добро пожаловать в ваш личный финансовый кошелек: {wallet_name}!')
    while True:
        choice = input('Пожалуйста, выберите необходимую функцию:\n'
                       '1 - Вывести баланс\n'
                       '2 - Добавить новую запись\n'
                       '3 - Редактировать запись\n'
                       '4 - Поиск по записям\n'
                       '5 - Выход\n')

        match choice:
            case '1':
                show_balance(wallet)
            case '2':
                new_records(wallet)
            case '3':
                change_record(wallet)
            case '4':
                find_record(wallet)
            case '5':
                print('Уже все? :(')
                break
