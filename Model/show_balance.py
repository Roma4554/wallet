from typing import Optional

from wallet.Wallet import Wallet


def check_records_list(wallet: Wallet) -> bool:
    """Функция получает на вход кошелек и возвращает истину если в нем не содержится записей"""
    if wallet.count_records == 0:
        return True


def show_balance(wallet: Wallet, choice: str) -> Optional[str]:
    """Функция для вывода общего баланса кошелька и баланса по статьям """
    match choice:
        case '1':
            return f'Текущий баланс: {wallet.balance}\n'
        case '2':
            return f'Доход за все время: {wallet.count("Доход")}\n'
        case '3':
            return f'Расход за все время: {wallet.count("Расход")}\n'
        case '4':
            return