from requests_handler import get_data, post_data
from mapper import map_data
from config import CONFIG

def main():
    raw_data = get_data()
    mapped_data = map_data(raw_data)
    
    for item in mapped_data:
        post_data(item)

if __name__ == "__main__":
    main()