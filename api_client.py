import json
import requests
from datetime import datetime
from pathlib import Path
import os









BASE_URL = "https://dummyjson.com"

# def fetch_data(endpoint):
#     url = f"{BASE_URL}/{endpoint}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error fetching data from {endpoint}: {response.status_code}")
#         return None
    

# response = requests.get(f"{BASE_URL}/products")
# data = response.json()


# # Date and time
# date = datetime.now().strftime("%Y-%m-%d")
# time = datetime.now().strftime("%H:%M:%S")

# #route 
# route = f"data/raw/products/date={date}"
# os.makedirs(route, exist_ok=True)


# file =f"{route}/products_{time}.json"


# with open(file, "w") as f:
#     json.dump(data, f, indent=2)

# print(f"Guardado en: {file}")



endpoints = ["products", "users", "carts"]


for endpoint in endpoints:
    response = requests.get(f"{BASE_URL}/{endpoint}")
    data = response.json()
    
    # Date and time
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")

    #route 
    route = f"data/raw/{endpoint}/date={date}"
    os.makedirs(route, exist_ok=True)

    file =f"{route}/{endpoint}_{time}.json"

    with open(file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Guardado en: {file}")