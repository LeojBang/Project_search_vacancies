import json
import os
from typing import Any

from src.base_json_saver import BaseJSONSaver


class JSONSaver(BaseJSONSaver):

    def __init__(self, file_worker: str = "data/vacancies.json"):
        self.__file_worker = file_worker

    @staticmethod
    def __create_vacancy_dict(vacancies: list) -> list:
        """Создает словарь из объекта Vacancy."""
        return [
            {
                "name": vacancy.name,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "experience": vacancy.experience,
            }
            for vacancy in vacancies
        ]

    @staticmethod
    def get_json_data(file_path: str) -> Any:
        """Метод получения данных из файла"""
        with open(file_path, "r+", encoding="utf-8") as file:
            json_data = json.load(file)
            return json_data

    def add_vacancy(self, vacancies: list) -> None:
        json_file_vacancies = self.__load_data()

        vacancy_dicts = self.__create_vacancy_dict(vacancies)

        for vacancy_dict in vacancy_dicts:
            if vacancy_dict not in json_file_vacancies:
                json_file_vacancies.append(vacancy_dict)

        self.__save_data(json_file_vacancies)

    def delete_vacancy(self, vacancies: list) -> None:
        json_vacancies = self.__load_data()

        vacancy_dicts = self.__create_vacancy_dict(vacancies)

        for vacancy_dict in vacancy_dicts:
            if vacancy_dict in json_vacancies:
                json_vacancies.remove(vacancy_dict)

        self.__save_data(json_vacancies)

    def __save_data(self, data: list) -> None:
        with open(self.__file_worker, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)  # type: ignore

    def __load_data(self) -> Any:
        if os.path.exists(self.__file_worker):
            with open(self.__file_worker, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
