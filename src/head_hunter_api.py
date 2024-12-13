from typing import Any

import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """Класс получает информацию о вакансиях с сайта HeadHunter"""

    def __init__(self, file_worker: str = "data/json_vacancies.json"):
        """Конструктор объекта запроса инфо через API сервис"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list = []
        super().__init__(file_worker)

    def get_vacancies(self, keyword: str) -> list:
        """Метод получения вакансий с сайта HeadHunter"""
        return self._load_vacancies(keyword)

    def _connect_to_api(self, keyword: str) -> Any:
        """Protected метод подключения к API и проверки статус-кода"""
        self.__params["text"] = keyword
        try:
            response = requests.get(
                self.__url, headers=self.__headers, params={k: str(v) for k, v in self.__params.items()}
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Ошибка подключения к API: {e}")
            return None

    def _load_vacancies(self, keyword: str) -> list:
        """Protected метод загрузки данных вакансий из API сервиса"""
        self.__params["text"] = keyword
        self.__params["page"] = 0
        self.__vacancies = []
        if isinstance(self.__params["page"], int):
            while self.__params["page"] < 20:
                response = self._connect_to_api(keyword)
                if not response:
                    break

                vacancies = response.json().get("items", [])
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1

        return self.__vacancies
