import requests
import json
from datetime import datetime   
import os


def extract_raw(endpoint):
    url = f"https://dummyjson.com/{endpoint}"
    try:
        response = requests.get(url)
        data = response.json()
    
        # Date and time
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        
        route = f"data/raw/{endpoint}/date={date}"
        os.makedirs(route, exist_ok=True)
        
        file = f"{route}/{endpoint}_{time}.json"
        
        with open(file, "w") as f:
            json.dump(data, f, indent=2)
        
        print(f"{endpoint} guardado en: {file}")
    
    except requests.RequestException as error:
        print(f"Error extracting {endpoint}: {error}")
        raise