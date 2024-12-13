from abc import ABC, abstractmethod
from typing import Any


class BaseAPI(ABC):
    """Абстрактный класс инициализации пути до файла и получения вакансий по ключевому слову"""

    @abstractmethod
    def __init__(self, file_worker: str) -> None:
        self.file_worker = file_worker

    @abstractmethod
    def _connect_to_api(self, keyword: str) -> Any:
        """Метод для подключения к API"""
        pass

    @abstractmethod
    def _load_vacancies(self, keyword: str) -> list:
        """Метода для получения вакансий по ключевому слову"""
        pass
