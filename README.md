# Проект: Система для работы с вакансиями

## Описание проекта

Данный проект представляет собой систему для поиска, фильтрации, сортировки и сохранения вакансий из
API [HeadHunter](https://hh.ru). Вакансии можно фильтровать по ключевым словам, диапазону зарплат и другим параметрам.
Также реализована возможность сохранения вакансий в JSON-файл и удаления их оттуда.

## Структура проекта

```plaintext
project/
│-- data/
│   ├── json_vacancies.json     # json-файл со всеми вакансиями полученные из класса HeadHunterAPI
│   └── vacancies.json          # json-файл с вакансиями сохраненными классом JSONSaver
│-- htmlcov/                    # Директория с информацией о покрытии тестами
│-- src/
│   ├── base_api.py             # Базовый класс взаимодействия с API HeadHunter
│   ├── base_json_saver.py      # Базовый класс для сохранения данных в JSON
│   ├── head_hunter_api.py      # Класс для взаимодействия с API HeadHunter
│   ├── json_saver.py           # Класс для работы с JSON-файлом
│   ├── user_interaction.py     # Функции для фильтрации и вывода вакансий
│   └── vacancy.py              # Класс для представления вакансий
│-- tests/
│   ├── conftest.py              # Фикстуры для тестов
│   ├── test_head_hunter_api.py  # Тесты для модуля head_hunter_api.py
│   ├── test_json_saver.py       # Тесты для модуля json_saver.py
│   ├── test_user_interaction.py # Тесты для модуля user_interaction.py
│   └── test_vacancy.py          # Тесты для модуля vacancy.py
├── .flake8
├── .gitignore
├── LICENSE
├── main.py                      # Главным модуль для запуска приложения
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Установка:

Для установки и управления зависимостями проекта используется Poetry. Убедитесь, что у вас установлена последняя версия
Poetry. Если у вас его нет, установите его,
следуя [инструкциям на официальном сайте Poetry](https://python-poetry.org/docs/#installation).

1. Клонируйте репозиторий:

```
git clone https://github.com/LeojBang/Project_search_vacancies.git
```

2. Установите зависимости проекта:

```bash
poetry install
````

3. Запуск проекта

```bash
python3 main.py
```

## Использование

### Получение и фильтрация вакансий

Пример кода для получения и фильтрации вакансий:

```python
from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.user_interaction import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies

hh = HeadHunterAPI()
raw_vacancies = hh.get_vacancies("Python")

# Преобразование в объекты Vacancy
vacancies = Vacancy.cast_to_object_list(raw_vacancies)

# Фильтрация вакансий по ключевым словам
filtered = filter_vacancies(vacancies, "Python")

# Фильтрация по зарплате
salary_filtered = get_vacancies_by_salary(filtered, "120000-220000")

# Сортировка по зарплате
sorted_vacancies = sort_vacancies(salary_filtered)

# Получение топ-5 вакансий
top_vacancies = get_top_vacancies(sorted_vacancies, 5)

# Вывод вакансий
print_vacancies(top_vacancies)
```

### Тестирование

Для запуска тестов используйте pytest:

```bash
pytest
```
Для запуска тестов с информацией о покрытии используйте pytest-cov:

```bash
pytest --cov=src --cov-report=html
```
### Примеры тестов

- Тест загрузки вакансий:

```python
from unittest.mock import patch
from src.head_hunter_api import HeadHunterAPI


@patch("requests.get")
def test_head_hunter_api_load_vacancies(mock_request, head_hunter):
    mock_request.return_value.json.return_value = {"items": head_hunter}

    hh = HeadHunterAPI()
    response = hh.get_vacancies("Python")

    assert response[0]["name"] == "Python-разработчик"
```

- Тестирует сравнение двух вакансий по зарплате с помощью оператора **>=**:

```python
def test_vacancy_ge(first_vacancy, second_vacancy):

    # Сравниваем две вакансии
    result = first_vacancy >= second_vacancy

    # Проверяем, что результат сравнения соответствует ожиданию
    assert result is False
```

## Зависимости

Проект использует следующие библиотеки:

	•	requests для работы с внешними API.
	•	pytest для тестирования.
	•	pytest-cov для отчета с покрытием тестами.

### Контакты

Для вопросов и предложений, пожалуйста, свяжитесь со мной по электронной почте: m.merkulovdodo@gmail.com

## Лицензия
Этот файл `README.md` предоставляет общее представление о проекте, описывает его функциональность, установку и запуск. Убедитесь, что настроены зависимости, и что ваш проект правильно работает с API для получения данных.

### Skypro