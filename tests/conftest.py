import os
from unittest.mock import patch

import psycopg2
import pytest
from dotenv import load_dotenv

from src.hh_parser import HHParser
from src.utils import create_database, create_tables

load_dotenv()


@pytest.fixture(scope="module")
def test_db():
    """Фикстура для создания тестовой базы данных."""
    conn = psycopg2.connect(
        dbname=os.getenv("database"),  # Используйте базу данных для тестов
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Создаем тестовые таблицы и данные
    cursor.execute(
        """
        CREATE TABLE employer (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """
    )
    cursor.execute(
        """
        CREATE TABLE vacancy (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            salary_from INT,
            url VARCHAR(255),
            employer_id INT,
            FOREIGN KEY (employer_id) REFERENCES employer (id)
        );
    """
    )
    # Вставляем тестовые данные
    cursor.execute("INSERT INTO employer (name) VALUES ('Company A'), ('Company B');")
    cursor.execute(
        "INSERT INTO vacancy (name, salary_from, url, employer_id) VALUES "
        "('Vacancy 1', 60000, 'http://example.com/vacancy1', 1), "
        "('Vacancy 2', 80000, 'http://example.com/vacancy2', 1), "
        "('Vacancy 3', 50000, 'http://example.com/vacancy3', 2);"
    )

    yield conn

    # Удаляем тестовые таблицы после тестов
    cursor.execute("DROP TABLE IF EXISTS vacancy;")
    cursor.execute("DROP TABLE IF EXISTS employer;")
    cursor.close()
    conn.close()


@pytest.fixture
def mock_requests_get():
    """Фикстура для имитации requests.get."""
    with patch("requests.get") as mock_get:
        yield mock_get


@pytest.fixture(scope="module")
def db_name():
    """Фикстура для названия базы данных."""
    return "test_db"


@pytest.fixture(scope="module", autouse=True)
def setup_database(db_name):
    """Фикстура для настройки базы данных перед тестами."""
    # Создание базы данных
    create_database(db_name)
    create_tables(db_name)

    yield

    # Удаление базы данных после тестов
    conn = psycopg2.connect(
        dbname="postgres",
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {db_name} WITH (FORCE)")
    cur.close()
    conn.close()


@pytest.fixture
def mock_get_employers():
    """Фикстура для имитации метода get_employers."""
    with patch.object(HHParser, "get_employers") as mock:
        yield mock


@pytest.fixture
def mock_get_vacancies():
    """Фикстура для имитации метода get_vacancies."""
    with patch.object(HHParser, "get_vacancies") as mock:
        yield mock
