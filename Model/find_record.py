from typing import Optional

from wallet.Wallet import Wallet


def sort_records_category(wallet: Wallet, choice: str) -> Optional[list[str]]:
    """Функция для поиска записей по категории"""

    match choice:
        case '1':
            choice = "Доход"
        case '2':
            choice = "Расход"
        case '3':
            return

    return [str(record) for record in wallet.get_records() if record.category == choice]


def sort_record_date(wallet: Wallet, choice: str) -> Optional[list[str]]:
    """Функция для поиска записей по дате"""
    return [str(record) for record in wallet.get_records() if str(record.date) == choice]


def sort_record_sum(wallet: Wallet, choice: str, value_sum: str) -> Optional[list[str]]:
    """Функция для поиска записей по сумме"""

    match choice:
        case '1':
            return [str(record) for record in wallet.get_records() if record.value_sum > value_sum]
        case '2':
            return [str(record) for record in wallet.get_records() if record.value_sum < value_sum]
        case '3':
            return [str(record) for record in wallet.get_records() if record.value_sum == value_sum]
        case '4':
            return
