from datetime import datetime
from typing import Union

from wallet.Wallet import Wallet
from wallet.Record import Record


def get_record(wallet: Wallet, num_record: int) -> Record:
    if not(0 < int(num_record) <= wallet.count_records):
        raise IndexError('Данные введены не корректно!')
    records = wallet.get_records_list()
    return records[num_record - 1]

def save_change(wallet: Wallet, record: Record, num_record: int) -> None:
    records = wallet.get_records_list()
    records[num_record - 1] = record
    wallet.add_list(records)

def set_date(value: str, record: Record) -> None:
    """Функция для изменения даты записи"""

    value = datetime.fromisoformat(value).date()
    record.date = value


def change_category(wallet: Wallet, record: Record) -> None:
    """Функция для изменения категории записи"""
    value = "Доход" if record.category == "Расход" else "Расход"

    match value:
        case 'Доход':
            wallet.balance += record.value_sum * 2
        case 'Расход':
            wallet.balance -= record.value_sum * 2
    record.category = value


def set_sum(wallet: Wallet, record: Record, value: Union[int, float]) -> None:
    """Функция для изменения суммы записи"""
    if record.category == 'Доход':
        wallet.balance += (value - record.value_sum)
    else:
        wallet.balance -= (value - record.value_sum)
    record.value_sum = value


def set_description(record: Record) -> None:
    """Функция для изменения описания записи"""
    value = input('Введите новое описание\n')
    record.description = value
