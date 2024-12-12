from unittest.mock import patch

from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


@patch("requests.get")
def test_vacancy(mock_request, head_hunter):
    """Тестирует получение и преобразование вакансий с помощью HeadHunterAPI и Vacancy."""

    # Мокаем ответ от API с тестовыми данными из фикстуры head_hunter
    mock_request.return_value.json.return_value = {"items": head_hunter}

    # Создаем экземпляр HeadHunterAPI и вызываем метод get_vacancies
    hh = HeadHunterAPI()
    response = hh.get_vacancies("Python")

    # Преобразуем полученные вакансии в объекты Vacancy
    python = Vacancy.cast_to_object_list(response)

    # Проверяем данные первой вакансии
    assert python[0].name == "Python-разработчик"
    assert python[0].url == "https://hh.ru/vacancy/112422077"
    assert python[0].salary == {"from": 0, "to": 0}
    assert python[0].experience == "От 1 года до 3 лет"

    assert len(Vacancy.list_vacancies()) == 20


@patch("requests.get")
def test_vacancy_validate(mock_request, head_hunter):
    """Тестирует корректную обработку зарплаты в полученных вакансиях."""

    # Мокаем ответ от API с тестовыми данными зарплаты
    mock_request.return_value.json.return_value = {"items": [{"salary": {"from": 50000, "to": 60000}}]}

    # Создаем экземпляр HeadHunterAPI и вызываем метод get_vacancies
    hh = HeadHunterAPI()
    response = hh.get_vacancies("Python")

    # Преобразуем полученные вакансии в объекты Vacancy
    python = Vacancy.cast_to_object_list(response)

    # Проверяем, что зарплата корректно установлена
    assert python[0].salary == {"from": 50000, "to": 60000}


def test_vacancy_ge(first_vacancy, second_vacancy):
    """Тестирует сравнение двух вакансий по зарплате с помощью оператора >=."""

    # Сравниваем две вакансии
    result = first_vacancy >= second_vacancy

    # Проверяем, что результат сравнения соответствует ожиданию
    assert result is False
