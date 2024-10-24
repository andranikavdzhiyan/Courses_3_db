import pytest

from src.hh_parser import HHParser


def test_get_employers(mock_requests_get):
    """Тестируем метод получения 10-ти работодателей."""
    # Настраиваем имитацию ответа от API
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {
        "items": [
            {"id": 1, "name": "Employer A"},
            {"id": 2, "name": "Employer B"},
            # Добавьте дополнительные имитируемые работодатели по мере необходимости
        ]
    }

    parser = HHParser()
    employers = parser.get_employers()

    assert len(employers) == 2  # Проверяем, что получаем 2 работодателя
    assert employers[0]["name"] == "Employer A"  # Проверяем имя первого работодателя


def test_get_vacancies(mock_requests_get):
    """Тестируем метод получения 50-ти вакансий для заданного работодателя."""
    # Настраиваем имитацию ответа от API
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {
        "items": [
            {"id": 1, "name": "Vacancy A"},
            {"id": 2, "name": "Vacancy B"},
            # Добавьте дополнительные имитируемые вакансии по мере необходимости
        ]
    }

    parser = HHParser()
    vacancies = parser.get_vacancies(employer_id=1)

    assert len(vacancies) == 2  # Проверяем, что получаем 2 вакансии
    assert vacancies[0]["name"] == "Vacancy A"  # Проверяем имя первой вакансии


def test_get_employers_error(mock_requests_get):
    """Тестируем обработку ошибки при получении работодателей."""
    # Настраиваем имитацию ответа от API с ошибкой
    mock_requests_get.return_value.status_code = 404
    mock_requests_get.return_value.text = "Not Found"

    parser = HHParser()

    with pytest.raises(Exception) as excinfo:
        parser.get_employers()
    assert "Ошибка 404: Not Found" in str(
        excinfo.value
    )  # Проверяем сообщение об ошибке


def test_get_vacancies_error(mock_requests_get):
    """Тестируем обработку ошибки при получении вакансий."""
    # Настраиваем имитацию ответа от API с ошибкой
    mock_requests_get.return_value.status_code = 500
    mock_requests_get.return_value.text = "Internal Server Error"

    parser = HHParser()

    with pytest.raises(Exception) as excinfo:
        parser.get_vacancies(employer_id=1)
    assert "Ошибка 500: Internal Server Error" in str(
        excinfo.value
    )  # Проверяем сообщение об ошибке
