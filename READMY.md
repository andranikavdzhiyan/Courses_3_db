# Проект 
Поиск вакансий


## Описание:
Программа получения информации о вакансиях с платформы hh.ru в России по заданным критериям


## Установка:
Клонируйте репозиторий 
``` https://github.com/andranikavdzhiyan/Courses_3_db```


## Зависимости
- python 3.12
- requests 2.32.3


## Установка зависимостей
```pip install -r requirements.txt```


## Конфигурация
Перед запуском проекта убедитесь, что все зависимости установлены и выполнены необходимые конфигурационные шаги


## Использование:
Точка запуска программы является модулем main.py— просто запустите его

 ##  Структура проекта

Вот обзор структуры проекта:

```plaintext
Course_work/
│
├── .flake8                 # Конфигурация для проверки стиля кода
├── .gitignore              # Правила игнорирования файлов Git
├── READMY.md               # Документация проекта (этот файл)
├── poetry.lock             # Файл блокировки зависимостей Poetry
├── pyproject.toml          # Конфигурационный файл проекта для Poetry
├── main.py                 # Точка входа в приложение
│
├── src/                    # Исходный код приложения
│   ├── __init__.py         # Помечает src как пакет
│   ├── hh_parser.py        # Функция работы с API
│   ├── utils.py            # Вспомогательные функции
│   └── db_manager.py       # создание класса DBManager подключения к базе данных и реализованы запрашиваемые методы 
│   
└── tests/                     
    ├── __init__.py            
    ├── conftest.py            
    ├── test_hh_parser.py         
    ├── test_utils.py                
    └── test_db_manager.py  

```

### На данной стадии покрытие тестов составляет 99% 
```
====================== test session starts ====================================
platform win32 -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Andrey\PycharmProjects\my_prj\Courses_3_db
configfile: pyproject.toml
plugins: cov-5.0.0
collected 11 items                                                                                                                                                                         

tests\test_db_manager.py ....               [ 36%]
tests\test_hh_parser.py ....                [ 72%] 
tests\test_utils.py ...                     [100%]

---------- coverage: platform win32, python 3.12.4-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\db_manager.py             27      1    96%
src\hh_parser.py              18      0   100%
src\utils.py                  38      2    95%
tests\__init__.py              0      0   100%
tests\conftest.py             48      0   100%
tests\test_db_manager.py      23      0   100%
tests\test_hh_parser.py       30      0   100%
tests\test_utils.py           39      0   100%
----------------------------------------------
TOTAL                        223      3    99%

```



## Документация:
### Для получения дополнительной информации обратитесь к документации.

## Лицензия:
### Этот проект лицензирован по лицензии MIT. `☺`