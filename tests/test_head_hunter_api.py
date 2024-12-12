from unittest.mock import patch

import requests

from src.head_hunter_api import HeadHunterAPI


@patch("requests.get")
def test_head_hunter_api_side_effect(mock_request, capsys):
    # Настраиваем mock так, чтобы вызов requests.get() выбрасывал исключение RequestException
    mock_request.side_effect = requests.RequestException("Сетевая ошибка")

    # Создаем экземпляр HeadHunterAPI и пытаемся подключиться к API
    hh = HeadHunterAPI()
    hh._connect_to_api("test")

    # Захватываем вывод в консоль
    message = capsys.readouterr()

    # Проверяем, что в выводе содержится сообщение об ошибке
    assert message.out.strip() == "Ошибка подключения к API: Сетевая ошибка"


@patch("requests.get")
def test_head_hunter_api_status_code(mock_request):
    # Настраиваем mock так, чтобы он возвращал объект со статус-кодом 200
    mock_request.return_value.status_code = 200

    # Создаем экземпляр HeadHunterAPI и вызываем метод _connect_to_api
    hh = HeadHunterAPI()
    response = hh._connect_to_api("test")

    # Проверяем, что requests.get был вызван
    assert mock_request.called

    # Проверка, что статус-код ответа равен 200
    assert response.status_code == 200


@patch("requests.get")
def test_head_hunter_api_load_vacancies(mock_request, head_hunter):
    # Настраиваем mock так, чтобы он возвращал ответ с данными вакансий
    mock_request.return_value.json.return_value = {"items": head_hunter}

    # Создаем экземпляр HeadHunterAPI и вызываем метод get_vacancies
    hh = HeadHunterAPI()
    response = hh.get_vacancies("Python")

    # Проверяем, что данные первой вакансии соответствуют ожидаемым значениям
    assert response[0]["name"] == "Python-разработчик"
    assert response[0]["salary"] is None
    assert response[0]["alternate_url"] == "https://hh.ru/vacancy/112422077"
