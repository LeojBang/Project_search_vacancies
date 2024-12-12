from src.user_interaction import (filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies,
                                  sort_vacancies)


def test_filter_vacancies(first_vacancy, second_vacancy):
    """Тестирует фильтрацию вакансий по ключевым словам."""

    # Выполняем фильтрацию по слову "Требование"
    filtered_vacancies = filter_vacancies([first_vacancy, second_vacancy], "Требование")

    # Проверяем, что первая отфильтрованная вакансия имеет ожидаемые данные
    assert filtered_vacancies[0].get("name") == "Python Developer"
    assert filtered_vacancies[0].get("salary") == {"from": 100000, "to": 150000}
    assert filtered_vacancies[0].get("experience") == "Требования: опыт работы от 3 лет..."

    # Проверяем, что десятая отфильтрованная вакансия имеет ожидаемые данные
    assert filtered_vacancies[10].get("name") == "Java Developer"
    assert filtered_vacancies[10].get("salary") == {"from": 100000, "to": 180000}
    assert filtered_vacancies[10].get("experience") == "Требования: опыт работы от 2 лет..."


def test_get_vacancies_by_salary(filter_vacancy):
    """Тестирует фильтрацию вакансий по диапазону зарплат."""

    # Фильтруем вакансии с зарплатой от 25000 до 60000
    ranged_salary = get_vacancies_by_salary(filter_vacancy, "25000-60000")

    # Проверяем, что отфильтровано 3 вакансии
    assert len(ranged_salary) == 3


def test_get_vacancies_by_salary_invalid_input(filter_vacancy):
    """Тестирует обработку некорректного формата ввода для диапазона зарплат."""

    # Подаем некорректный формат диапазона зарплат
    ranged_salary = get_vacancies_by_salary(filter_vacancy, "25000 60000")

    # Ожидаем пустой список из-за некорректного ввода
    assert ranged_salary == []


def test_sort_vacancies(filter_vacancy):
    """Тестирует сортировку вакансий по зарплате (по убыванию)."""

    # Выполняем сортировку вакансий
    result = sort_vacancies(filter_vacancy)

    # Проверяем порядок отсортированных зарплат
    assert result[0].get("salary") == {"from": 80000, "to": 100000}
    assert result[1].get("salary") == {"from": 25000, "to": 60000}
    assert result[2].get("salary") == {"from": 25000, "to": 50000}
    assert result[3].get("salary") == {"from": 30000, "to": 50000}


def test_get_top_vacancies(filter_vacancy):
    """Тестирует получение топ N вакансий после сортировки."""
    # Сортируем вакансии
    sorting = sort_vacancies(filter_vacancy)

    # Получаем топ-2 вакансии
    result = get_top_vacancies(sorting, 2)

    # Проверяем, что результат содержит ровно 2 вакансии
    assert len(result) == 2


def test_print_vacancies(capsys, sample_vacancies):
    """Тестирует вывод вакансий на консоль."""

    # Вызываем функцию print_vacancies для вывода тестовых данных
    print_vacancies(sample_vacancies)

    # Захватываем вывод из консоли
    captured = capsys.readouterr()

    # Ожидаемый вывод
    expected_output = (
        "Название: Python Developer\n"
        "URL: https://example.com/python_dev\n"
        "Зарплата: от 100000 до 150000\n"
        "Описание: Разработка на Python.\n"
        "--------------------------------------------------\n"
        "Название: Senior Python Developer\n"
        "URL: https://example.com/senior_python_dev\n"
        "Зарплата: от 200000 до 250000\n"
        "Описание: Опыт работы с Django.\n"
        "--------------------------------------------------\n"
    )

    # Проверяем, что захваченный вывод совпадает с ожидаемым

    assert captured.out == expected_output
