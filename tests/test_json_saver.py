import json

from src.json_saver import JSONSaver


def test_json_saver_get_json_data(tmp_path, head_hunter):
    """Тест для метода get_json_data, проверяет получение данных из JSON-файла."""

    # Создаем экземпляр JSONSaver
    json_saver = JSONSaver()

    # Создаем временный файл и записываем туда тестовые данные head_hunter
    temp_file = tmp_path / "test_json_saver.json"
    temp_file.write_text(json.dumps(head_hunter, indent=4))

    # Убедимся, что файл существует
    assert temp_file.exists()

    # Проверяем, что метод get_json_data возвращает корректные данные

    file_content = json_saver.get_json_data(temp_file)
    assert file_content == head_hunter


def test_json_saver_add_vacancy(tmp_path, first_vacancy):
    """Тест для метода add_vacancy, проверяет добавление вакансий в JSON-файл."""

    # Путь к временному файлу
    temp_file = tmp_path / "test_json_saver.json"

    # Создаем экземпляр JSONSaver, используя временный файл
    json_saver = JSONSaver(file_worker=str(temp_file))

    # Добавляем первую вакансию
    json_saver.add_vacancy([first_vacancy])

    # Читаем содержимое файла после добавления первой вакансии
    with open(temp_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Проверяем, что файл содержит одну вакансию
    assert len(data) == 1
    assert data[0]["name"] == first_vacancy.name


def test_json_saver_delete_vacancy(tmp_path, first_vacancy, second_vacancy):
    """Тест для метода add_vacancy, проверяет добавление вакансий в JSON-файл."""

    # Путь к временному файлу
    temp_file = tmp_path / "test_json_saver.json"

    # Создаем экземпляр JSONSaver, используя временный файл
    json_saver = JSONSaver(file_worker=str(temp_file))

    # Добавляем две вакансии
    json_saver.add_vacancy([first_vacancy, second_vacancy])

    # Удаляем первую вакансию
    json_saver.delete_vacancy([first_vacancy])

    # Читаем содержимое файла после удаления первой вакансии
    with open(temp_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Проверяем, что файл содержит одну вакансию
    assert len(data) == 1
    assert data[0]["name"] == second_vacancy.name
