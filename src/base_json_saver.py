from abc import ABC, abstractmethod


class BaseJSONSaver(ABC):
    """Базовый класс, определяет методы добавления и удаления вакансий из файла"""

    @abstractmethod
    def add_vacancy(self, vacancies: list) -> None:
        """Абстрактный метод добавления вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancies: list) -> None:
        """Абстрактный метод удаления вакансий из файла"""
        pass
