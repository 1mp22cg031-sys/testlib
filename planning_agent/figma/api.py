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


def fetch_figma_data(token, file_id):
    url = f"https://api.figma.com/v1/files/{file_id}"
    headers = {"X-Figma-Token": token}

    response = requests.get(url, headers=headers)

    print("🔍 Status Code:", response.status_code)
    print("🔍 Response:", response.text)

    return response.json()


def get_figma_data(token=None, file_id=None):
    token = token or os.getenv("FIGMA_TOKEN")
    file_id = file_id or os.getenv("FIGMA_FILE_ID")

    print("🔍 Token:", token)
    print("🔍 File ID:", file_id)

    return fetch_figma_data(token, file_id)