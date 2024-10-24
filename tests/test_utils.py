import os

import psycopg2

from src.utils import create_database, create_tables, insert_data


def test_create_database(db_name):
    """Тест на создание базы данных."""
    create_database(db_name)

    conn = psycopg2.connect(
        dbname="postgres",
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
    exists = cur.fetchone() is not None

    cur.close()
    conn.close()
    assert exists, "База данных не была создана."


def test_create_tables(db_name):
    """Тест на создание таблиц."""
    create_database(db_name)  # Создание базы данных
    create_tables(db_name)

    conn = psycopg2.connect(
        dbname=db_name,
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )
    cur = conn.cursor()
    cur.execute("SELECT to_regclass('employer')")
    employer_exists = cur.fetchone()[0] is not None
    cur.execute("SELECT to_regclass('vacancy')")
    vacancy_exists = cur.fetchone()[0] is not None

    cur.close()
    conn.close()
    assert employer_exists, "Таблица employer не была создана."
    assert vacancy_exists, "Таблица vacancy не была создана."


def test_insert_data(mock_get_employers, mock_get_vacancies, db_name):
    """Тест на вставку данных."""
    # Подготовка имитации данных
    mock_get_employers.return_value = [{"id": 1, "name": "Test Employer"}]
    mock_get_vacancies.return_value = [
        {
            "id": 1,
            "name": "Test Vacancy",
            "salary": {"from": 1000, "to": 2000},
            "alternate_url": "http://example.com/vacancy/1",
        }
    ]

    insert_data(db_name)

    conn = psycopg2.connect(
        dbname=db_name,
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )
    cur = conn.cursor()

    # Проверка на наличие работодателя
    cur.execute("SELECT * FROM employer WHERE id=1")
    employer = cur.fetchone()
    assert employer is not None, "Данные работодателя не были вставлены."

    # Проверка на наличие вакансии
    cur.execute("SELECT * FROM vacancy WHERE id=1")
    vacancy = cur.fetchone()
    assert vacancy is not None, "Данные вакансии не были вставлены."

    cur.close()
    conn.close()
