from typing import Any


class Vacancy:
    __list_vacancies: list = []
    __slots__ = ("__name", "__url", "__salary", "__experience")

    def __init__(self, name: str, url: str, salary: dict, experience: str):
        self.__name = name
        self.__url = url
        self.__salary = self.__validate(salary)
        self.__experience = experience

    @classmethod
    def cast_to_object_list(cls, vacancy_data: list) -> list:
        """Метод для создания объекта Vacancy из словаря данных."""
        for vacancy in vacancy_data:
            name = vacancy.get("name")
            url = vacancy.get("alternate_url")
            salary = vacancy.get("salary")
            experience = vacancy.get("experience", {}).get("name", "Не указано")
            cls.__list_vacancies.append(cls(name, url, salary, experience))
        return cls.__list_vacancies

    @classmethod
    def list_vacancies(cls) -> list:
        return cls.__list_vacancies

    @classmethod
    def clear_list(cls):
        cls.__list_vacancies = []

    @staticmethod
    def __validate(salary: dict | None) -> dict:
        if salary is None:
            return {"from": 0, "to": 0}
        if isinstance(salary, dict):
            salary_from = salary.get("from", 0)
            salary_to = salary.get("to", 0)
            return {"from": salary_from, "to": salary_to}
        else:
            return {"from": 0, "to": 0}

    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "url": self.__url,
            "salary": self.__salary,
            "experience": self.__experience,
        }

    @property
    def salary(self) -> dict:
        return self.__salary

    @property
    def experience(self) -> str:
        return self.__experience

    @property
    def name(self) -> str:
        return self.__name

    @property
    def url(self) -> str:
        return self.__url

    def __ge__(self, other: "Vacancy") -> Any:
        """Сравнивает вакансии по верхней границе зарплаты ('to')."""

        salary_self = self.__salary.get("to", 0)
        salary_other = other.__salary.get("to", 0)
        if salary_self is None:
            salary_self = 0
        if salary_other is None:
            salary_other = 0

        return salary_self >= salary_other
