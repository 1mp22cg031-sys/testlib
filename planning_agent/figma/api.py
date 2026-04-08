import requests
import json
import os
import time

FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")
FILE_ID = os.getenv("FIGMA_FILE_ID")

url = f"https://api.figma.com/v1/files/{FILE_ID}"

headers = {
    "X-Figma-Token": FIGMA_TOKEN
}

CACHE_FILE = "data/input/figma_raw.json"


def fetch_figma_data():
    for _ in range(5):
        response = requests.get(url, headers=headers)
        response = requests.get(url, headers=headers)

        print("🔍 Token:", token)
        print("🔍 File ID:", file_id)
        print("🔍 URL:", url)
        print("🔍 Status Code:", response.status_code)
        print("🔍 Response:", response.text)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            time.sleep(5)

    raise Exception("Failed to fetch Figma data")


def get_figma_data():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)

    data = fetch_figma_data()

    os.makedirs("data/input", exist_ok=True)

    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

    return data