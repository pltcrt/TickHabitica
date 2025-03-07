# config.py
# В этом файле хранятся все настройки, такие как URL для GET и POST запросов, параметры запросов и маппинг полей

CONFIG = {
    "auth": {
        "url": "https://ticktick.com/open/v1/project/6780df39ebbe9b000000063e/data",
        "headers": {
            "Authorization": "Bearer e5893689-9387-40de-a21b-1e315d4361a4",
            "Content-Type": "application/json"
        }
    },
    "post": {
        "url": "https://habitica.com/api/v3/tasks/user",
        "headers": {
            "x-api-user": "1e05932d-5154-450d-8c7a-d7f6c00e5475",
            "x-api-key": "7b50d847-a7ba-432c-bca2-7d573c3c61bd",
            "Content-Type": "application/json" }        
    },
    "mapping": {
        "title": "text",
        "content": "notes",
        "type": "todo"
    }
}

# config. url
# 65f01bf9ca9ace5a5f5dc704
# 65f01cf9ca9ace5a5f5dc89e
# 65f01d04ca9ace5a5f5dc8b3
# 65f01d2aca9ace5a5f5dc8d0
# 65f01d4eca9ace5a5f5dc8fd
# 66824a56091eac43ff3fdc1b
# 66bf0d648f0869c6b2352d7b
# 6780df39ebbe9b000000063e
# 6785193cebbe9b00000002c1