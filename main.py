from src.head_hunter_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.user_interaction import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, \
    print_vacancies
from src.vacancy import Vacancy


# Функция для взаимодействия с пользователем
def user_interaction():
    print("Добро пожаловать в поиск вакансий!")
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите Ваш опыт: ")
    salary_range = input("Введите диапазон зарплат (например, '100000-150000'): ")

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Пример работы конструктора класса с одной вакансией
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", {"from": 100000, "to": 150000},
                      "Требования: опыт работы от 3 лет...")

    # Преобразование набора данных в список объектов
    vacancies = Vacancy.cast_to_object_list(hh_vacancies)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancies)
    # json_saver.delete_vacancy(vacancies)

    # Фильтрация по ключевым словам в названии вакансии
    filtered_vacancies = filter_vacancies(vacancies, filter_words)

    # Фильтрация по диапазону зарплат
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # Сортировка по зарплате (по убыванию)
    sorted_vacancies = sort_vacancies(ranged_vacancies)

    # Получение топ N вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    # Вывод информации о вакансиях
    if top_vacancies:
        print("\nТоп вакансий по вашему запросу:")
        print_vacancies(top_vacancies)
    else:
        print("Вакансии по заданным критериям не найдены.")


# Запуск программы
if __name__ == "__main__":
    user_interaction()
