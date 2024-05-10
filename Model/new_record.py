from typing import Union

from wallet.Wallet import Wallet
from wallet.Record import Record


def new_records(wallet: Wallet, category: str, value_sum: Union[float, int], description: str) -> None:
    """Функция для получения необходимой информации о вносимой записи"""
    record = Record(category, value_sum, description)
    wallet.add(record)

