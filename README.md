# Личный финансовый кошелек
___

## Описание 

Консольное приложение для учета личных доходов и расходов.

## Как запустить
В работе приложения используются библиотеки из стандартного каталога Python 3.10. Запуск приложения осуществляется 
командой ```python main.py``` из терминала.


## Как пользоваться


Приложение позволяет создать собственный финансовый кошелек для учета личных доходов и расходов. 
Управление происходит с помощью команд в главном меню приложения (в консоли).

**Основные возможности приложения:**
1. <u>*Вывод баланса:*</u> Показать текущий баланс, а также отдельно доходы и расходы.
2. <u>*Добавление записи:*</u> Возможность добавления новой записи о доходе или расходе.
3. <u>*Редактирование записи:*</u> Изменение существующих записей о доходах и расходах.
4. <u>*Поиск по записям:*</u> Поиск записей по категории, дате или сумме.

При запуске приложения у пользователя запрашивается имя кошелька, после чего либо создается новый 
кошелек, либо, если кошелек уже был создан ранее, то продолжается работа с ранее созданным кошельком.

После выбора личного кошелька пользователь может выбрать необходимые действия
в меню консоли посредством ввода номера команды. 

**"Главном меню" представлено следующими командами:**
* Вывести баланс
* Добавить новую запись
* Редактировать запись
* Поиск по записям
* Выход

Выбрав нужный пункт и следуя дальнейшим указаниям пользователь может выполнить все основные
возможности приложения указанные ранее.

В случае, если пользователь хочет завершить работу с программой, то ему необходимо
выбрать *"Выход"* в главном меню.

Хранение всех запесей осуществляется в текстовом файле формата .json. Имя файла соответсвуте
названию кошелька введенного пользователем при запуске программы.

**Файл .json имеет следующую структуру:**
````
{
    "records": [
        {
            "Дата": "2024-05-04",
            "Категория": "Доход",
            "Сумма": "6000.0",
            "Описание": "ЗП"
        },
        {
            "Дата": "2024-05-05",
            "Категория": "Расход",
            "Сумма": "2400.0",
            "Описание": "Покупка продуктов"
        },
        {
            "Дата": "2024-05-05",
            "Категория": "Доход",
            "Сумма": "2000.0",
            "Описание": "Премия"
        }
    ]
}
````
где каждый словарь в списке ````records```` представляет собой отдельную запись,
содержащую информацию о дате записи, категории, сумме, а так же описанию статьи дохода/расхода.