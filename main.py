from Wallet import Wallet
from function import show_balance, new_records, find_record, change_record

if __name__ == "__main__":
      wallet_name = input('Введите название кошелька:\n')

      wallet = Wallet(wallet_name)

      print(f'Добро пожаловать в ваш личный финансовый кошелек: {wallet_name}!')
      while True:
            choice = input('Пожалуйста, выберите необходимую функцию:\n' \
                  '1 - Вывести баланс\n' \
                  '2 - Добавить новую запись\n' \
                  '3 - Редактировать запись\n' \
                  '4 - Поиск по записям\n' \
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



