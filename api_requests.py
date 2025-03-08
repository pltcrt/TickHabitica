import requests
import json
from config import CONFIG
from mapping import map_task

def get_tasks():
    """Выполняет GET-запрос и возвращает список задач."""
    response = requests.get(CONFIG["auth"]["url"], headers=CONFIG["auth"]["headers"])
    if response.status_code == 200:
        data = response.json()
        print("Полученные данные:", json.dumps(data, indent=4, ensure_ascii=False))
        return data.get("tasks", [])
    else:
        print("Ошибка при получении данных:", response.status_code, response.text)
        return []

def post_task(mapped_task):
    """Отправляет POST-запрос с замаппленными данными."""
    response = requests.post(CONFIG["post"]["url"], json=mapped_task, headers=CONFIG["post"]["headers"])
    print("Отправленные данные:", json.dumps(mapped_task, indent=4, ensure_ascii=False))
    print("Ответ сервера:", response.status_code, response.text)

def main():
    tasks = get_tasks()
    for task in tasks:
        mapped_task = map_task(task)
        post_task(mapped_task)

if __name__ == "__main__":
    main()
