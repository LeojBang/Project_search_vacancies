from src.vacancy import Vacancy


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: str) -> list[dict]:
    """Функция для фильтрации вакансий по ключевым словам в названии."""
    return [
        vacancy.to_dict()
        for vacancy in vacancies_list
        for word in filter_words
        if word.lower() in vacancy.experience.lower()
    ]


def get_vacancies_by_salary(filter_vacancy: list[dict], salary_range: str) -> list[dict]:
    """Фильтрация вакансий по диапазону зарплат."""

    ranged_vacancies = []
    try:
        salary_from, salary_to = map(int, salary_range.split("-"))
    except ValueError:
        print("Некорректный формат диапазона зарплат. Используйте формат: '100000 - 200000'")
        return []

    for vacancy in filter_vacancy:
        salary = vacancy.get("salary", {})
        salary_from_vacancy = salary.get("from")
        salary_to_vacancy = salary.get("to")

        if salary_from_vacancy and salary_to_vacancy:
            try:
                salary_from_vacancy = int(salary_from_vacancy)
                salary_to_vacancy = int(salary_to_vacancy)
            except ValueError:
                continue

            if salary_from <= salary_from_vacancy and salary_to >= salary_to_vacancy:
                ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies: list[dict]) -> list[dict]:
    """Сортировка вакансий по зарплате (по убыванию)."""

    return sorted(ranged_vacancies, key=lambda x: x["salary"].get("to", 0), reverse=True)


def get_top_vacancies(sorted_vacancies: list[dict], top_n: int) -> list[dict]:
    """Получение топ N вакансий."""

    return sorted_vacancies[:top_n]


def print_vacancies(vacancies: list[dict]) -> None:
    """Вывод вакансий в консоль."""

    for vacancy in vacancies:
        print(f"Название: {vacancy['name']}")
        print(f"URL: {vacancy['url']}")
        salary = vacancy.get("salary", {})
        print(f"Зарплата: от {salary.get('from', 'Не указано')} до {salary.get('to', 'Не указано')}")
        print(f"Описание: {vacancy['experience']}")
        print("-" * 50)
