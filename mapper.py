from config import CONFIG

def map_data(raw_data):
    mapped_items = []
    seen_titles = set()  # Используем множество для отслеживания уникальных заголовков
    
    for task in raw_data.get("tasks", []):
        title = task.get("title", "Untitled")
        if title in seen_titles:
            continue  # Пропускаем дубликаты
        
        seen_titles.add(title)
        mapped_item = {
            CONFIG["mapping"]["title"]: title,
            CONFIG["mapping"]["content"]: task.get("content", ""),
            "type": CONFIG["mapping"]["type"]
        }
        mapped_items.append(mapped_item)
    
    return mapped_items