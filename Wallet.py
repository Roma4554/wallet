from typing import Union, Iterable

from Record import Record
from json_function import new_wallet, add_record, read_records, get_records_list, add_records_list

class Wallet:
    """
    Класс для представления личного финансового кошелька.

    Атрибуты:
    __wallet_name: str - Имя кошелька;
    __count_records: int - количество записей в кошельке;
    balance: Union[int, float] - баланс кошелька.

    Методы:
    add(self, record: Record) -> None - метод для добавления записи в .json, с учеом изменения баланса
    add_list(self, list_records: list[Record]) -> None - метод для добавления списка записей в .json файл
    count(self, category: str) -> int: - метод для подсчета суммы по указанной категории
    get_records(self) -> Iterable[Record] - метод возвращает итератор с перечнем записей
    get_records_list(self) -> list[Record] - метод возвращает список с записями из .json файла

    """
    def __init__(self,
                 name: str) -> None:
        self.__count_records, self.balance = new_wallet(name)
        self.__wallet_name = name

    def add(self,
            record: Record) -> None:
        """Метод для добавления записи в .json, с учеом изменения баланса"""
        if isinstance(record, Record):
            if record.category == 'Расход':
                if record.value_sum > self.__balance:
                    print("На счету недостаточно средств!\n")
                    return
                else:
                    self.__balance -= record.value_sum
            else:
                self.__balance += record.value_sum

            add_record(self.__wallet_name, record)
            self.__count_records += 1
        else:
            raise TypeError("Значение должно быть типа Record.")

    def add_list(self, list_records: list[Record]) -> None:
        """Метод для добавления списка записей в .json файл"""
        add_records_list(self.__wallet_name, list_records)


    def count(self, category: str) -> int:
        """Метод для подсчета суммы по указанной категории"""
        value = 0
        for record in read_records(self.__wallet_name):
            if record.category == category:
                value += record.value_sum
        return value

    def get_records(self) -> Iterable[Record]:
        """Метод возвращает итератор с перечнем записей"""
        return read_records(self.__wallet_name)

    def get_records_list(self) -> list[Record]:
        """Метод возвращает список с записями из .json файла"""
        return get_records_list(self.__wallet_name)

    @classmethod
    def __verify_balance(cls, value: float) -> None:
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("Значение должно быть типа float или int.")
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным!\n")

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, value: int) -> None:
        self.__verify_balance(value)
        self.__balance = value

    @property
    def count_records(self) -> int:
        return self.__count_records