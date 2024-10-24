import os

import pytest

from src.db_manager import DBManager


@pytest.fixture
def db_manager(test_db):
    """Фикстура для инициализации DBManager с тестовой базой данных."""
    return DBManager(os.getenv("database"))


def test_get_companies_and_vacancies_count(db_manager):
    """Тестируем метод получения списка компаний и количества вакансий."""
    result = db_manager.get_companies_and_vacancies_count()
    assert len(result) == 2
    assert result[0][1] == "Company A"  # Проверка названия компании
    assert result[0][2] == 2  # Проверка количества вакансий


def test_get_all_employers(db_manager):
    """Тестируем метод получения всех вакансий."""
    result = db_manager.get_all_employers()
    assert len(result) == 3  # Должно быть 3 вакансии
    assert result[0][1] == "Vacancy 1"  # Проверка имени первой вакансии


# def test_get_avg_salary(db_manager):
#     """Тестируем метод получения средней зарплаты."""
#     result = db_manager.get_avg_salary()
#     assert result[0][0] == pytest.approx(63333.33, rel=1e-2)  # Проверка средней зарплаты


def test_get_vacancies_with_higher_salary(db_manager):
    """Тестируем метод получения вакансий с зарплатой выше средней."""
    result = db_manager.get_vacancies_with_higher_salary()
    assert len(result) == 1  # Должна быть одна вакансия выше средней
    assert result[0][0] == "Vacancy 2"  # Проверка имени вакансии


def test_get_vacancies_with_keyword(db_manager):
    """Тестируем метод получения вакансий по ключевому слову."""
    result = db_manager.get_vacancies_with_keyword("1")
    assert len(result) == 1  # Должна быть одна вакансия
    assert result[0][1] == "Vacancy 1"  # Проверка имени вакансии
