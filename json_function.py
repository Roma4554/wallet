import json
import os
from datetime import datetime
from typing import Iterable

from Record import Record


def new_wallet(name: str) -> tuple[int, int]:
    """
    Функция проверяет наличие кошелька с указанным именем,
    в случае отсутствия создает .json хранилище для нового кошелька
    """
    file_name = f'{name}.json'
    if os.path.exists(file_name):
        with open(file_name, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        income = 0
        expenses = 0
        for record in data['records']:
            if record["Категория"] == 'Доход':
                income += float(record["Сумма"])
            else:
                expenses += float(record["Сумма"])
        return len(data['records']), income - expenses
    else:
        with open(file_name, mode='w', encoding='utf-8') as json_file:
            json.dump({"records": list()}, json_file, ensure_ascii=False, indent=4)
        return 0, 0


def add_record(name: str, record: Record) -> None:
    """Функция для внесения новой записи в .json файл"""
    file_name = f'{name}.json'
    with open(file_name, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    data["records"].append(record.write_format())
    with open(file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def add_records_list(name: str, records_list: list[Record]) -> None:
    """Функция для внесения полученного списка в .json файл"""
    file_name = f'{name}.json'
    with open(file_name, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    records_list = [record.write_format() for record in records_list]
    data["records"] = records_list
    with open(file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def read_records(name: str) -> Iterable[Record]:
    """Функция итератор для получения записей из хранилища"""
    file_name = f'{name}.json'
    with open(file_name, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for string in data["records"]:
            yield Record(string['Категория'], float(string['Сумма']), string['Описание'],
                         datetime.fromisoformat(string['Дата']).date())


def get_records_list(name: str) -> list[Record]:
    """Функция возвращает список запесей из хранилища"""
    file_name = f'{name}.json'
    with open(file_name, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return [Record(string['Категория'], float(string['Сумма']), string['Описание'],
                   datetime.fromisoformat(string['Дата']).date()) for string in data["records"]]
