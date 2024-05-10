from typing import Union
from datetime import datetime, date


class Record:
    """
    Класс для представления записи.

    Атрибуты:
    category: str - категория (Доход/Расход);
    value: Union[float, int] - значение суммы
    description: str - описание записи
    date_record: date - дата внесения записи (по умолчанию текущая дата)

    Методы:
    write_format(self) -> dict[str:str] - возвращает атрибуты в виде словаря для записи в формате .json

    """

    def __init__(self,
                 category: str,
                 value: Union[float, int],
                 description: str,
                 date_record: date = datetime.now().date()) -> None:

        self.date = date_record
        self.category = category
        self.value_sum = value
        self.description = description

    def __str__(self):
        return f"Дата {self.date}\nКатегория: {self.category}\nСумма: {self.value_sum}\nОписание: {self.description}\n"

    def write_format(self) -> dict[str:str]:
        """
        Метод возвращает атрибуты класса в виде словаря для записи в формате .json
        """
        return dict(Дата=str(self.date), Категория=self.category, Сумма=str(self.value_sum), Описание=self.description)

    @classmethod
    def __verify_date(cls, date_record: date) -> None:
        if not isinstance(date_record, date):
            raise TypeError("Дата должна быть типа date.")

    @classmethod
    def __verify_category(cls, category: str) -> None:
        if not isinstance(category, str):
            raise TypeError("Категория должна быть типа str.")

    @classmethod
    def __verify_value_sum(cls, value: Union[float, int]) -> None:
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("Значение должно быть типа float или int.")
        if value < 0:
            raise ValueError("Сумма должна быть положительной!")

    @classmethod
    def __verify_description(cls, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError("Описание должно быть типа str.")

    @property
    def date(self) -> datetime:
        return self.__date

    @date.setter
    def date(self, value: datetime) -> None:
        self.__verify_date(value)
        self.__date = value

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, value: str) -> None:
        self.__verify_category(value)
        self.__category = value

    @property
    def value_sum(self) -> float:
        return self.__value_sum

    @value_sum.setter
    def value_sum(self, value: float) -> None:
        self.__verify_value_sum(value)
        self.__value_sum = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__verify_description(value)
        self.__description = value
