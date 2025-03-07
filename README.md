# TickHabitica. Release v1 - Integration Service

## Overview
Release version 7.2 is a Python-based integration service designed to sync tasks between different platforms. This release integrates data from a source API and sends the processed data to a target API. The system allows fetching data, transforming it according to a predefined mapping, and posting the transformed data to a new endpoint.

## Configuration (config.py)
The config.py file stores all the settings for API interactions, such as URLs for GET and POST requests, query parameters, and field mappings.
* auth section contains the authentication settings, including the authorization token.
* post section includes the target URL and headers for making POST requests to send data.
* mapping defines how data from the source API should be mapped before being posted to the target API.

## Request Handler (requests_handler.py)
This module handles API requests: both GET and POST requests are made using the requests library.
Functions:
* get_data(url): Fetches data from a URL with the provided headers.
* post_data(data): Sends data to a specified POST URL.

## Mapper (mapper.py)
This module is responsible for transforming the raw data according to the mapping configuration defined in config.py.
Functions:
* map_data(raw_data): Processes the raw task data and maps it based on the configuration.

## Main Script (main.py)
This is the entry point for the application, which ties everything together: fetching, transforming, and posting data.
Functions:
* fetch_data(): Retrieves the data from the source API.
* map_fields(data): Maps the fetched data to the target format.
* send_data(task): Sends the mapped data to the target API.

## Conclusion
This integration service efficiently fetches task data from one platform, transforms it as per the defined configuration, and sends it to another platform. It supports flexible configuration and can be adapted for different use cases by changing the mapping and endpoints in config.py.

## Requirements
* Python 3.x
* requests library (pip install requests)

To run the project:
1. Clone the repository or download the files.
2. Install the necessary dependencies.
3. Adjust the configuration file (config.py) as needed.
4. Run the main.py script to execute the integration.