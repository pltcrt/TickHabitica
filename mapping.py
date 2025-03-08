def map_task(task):
    """Маппинг данных из GET-запроса в формат POST-запроса."""
    return {
        "text": task["title"],
        "type": "todo",  # Всегда "todo"
        "notes": task.get("content", "")
    }
