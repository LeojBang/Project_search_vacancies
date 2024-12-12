import pytest

from src.vacancy import Vacancy


@pytest.fixture(autouse=True)
def reset_vacancy():
    Vacancy.clear_list()


@pytest.fixture
def first_vacancy():
    return Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        {"from": 100000, "to": 150000},
        "Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        "Java Developer",
        "<https://hh.ru/vacancy/654321>",
        {"from": 100000, "to": 180000},
        "Требования: опыт работы от 2 лет...",
    )


@pytest.fixture
def filter_vacancy():
    return [
        {
            "name": "Python-разработчик",
            "url": "https://hh.ru/vacancy/112422077",
            "salary": {
                "from": 25000,
                "to": 50000,
            },
            "snippet": "Опыт работы со схожим стеком от полугода (нам важно решение конкретных задач, а не стаж).",
        },
        {
            "name": "Strong Junior Backend разработчик",
            "url": "https://hh.ru/vacancy/112760167",
            "salary": {"from": 30000, "to": 50000},
            "snippet": "Опыт работы с Django/DRF. - Опыт работы с Redis, Docker, и похожие технологии.",
        },
        {
            "name": "QA Engineer / Тестировщик ПО",
            "url": "https://hh.ru/vacancy/110796947",
            "salary": {"from": 80000, "to": 100000},
            "snippet": "Иметь опыт работы с графическими приложениями для макетов и прототипов. ",
        },
        {
            "name": "Разработчик Python в IT-компанию (Удаленно / Без собеседований)",
            "url": "https://hh.ru/vacancy/112882100",
            "salary": {"from": 25000, "to": 60000},
            "snippet": "Ты должен знать: ️ React (Базовые корректировки на основе примеров).",
        },
    ]


@pytest.fixture
def sample_vacancies():
    """Возвращает тестовый список вакансий для проверки вывода."""
    return [
        {
            "name": "Python Developer",
            "url": "https://example.com/python_dev",
            "salary": {"from": 100000, "to": 150000},
            "snippet": "Разработка на Python.",
        },
        {
            "name": "Senior Python Developer",
            "url": "https://example.com/senior_python_dev",
            "salary": {"from": 200000, "to": 250000},
            "snippet": "Опыт работы с Django.",
        },
    ]


@pytest.fixture
def head_hunter():
    return [
        {
            "id": "112422077",
            "premium": False,
            "name": "Python-разработчик",
            "department": None,
            "has_test": False,
            "response_letter_required": True,
            "area": {"id": "1003", "name": "Гомель", "url": "https://api.hh.ru/areas/1003"},
            "salary": None,
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-12-03T13:28:47+0300",
            "created_at": "2024-12-03T13:28:47+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=112422077",
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/112422077?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/112422077",
            "relations": [],
            "employer": {
                "id": "10724692",
                "name": "НЕ ПРОСТО СТУДИЯ",
                "url": "https://api.hh.ru/employers/10724692",
                "alternate_url": "https://hh.ru/employer/10724692",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10724692",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Опыт работы со схожим стеком от полугода",
                "responsibility": "Реализация подключения Facebook с помощью API к нашему продукту.",
            },
            "contacts": None,
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "project", "name": "Проектная работа"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]
