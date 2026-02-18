

import requests

from typing import List, Dict


def fetch_api(urls: List[str]) -> List[Dict]:

    responses = []


    for url in urls:

        try:

            response = requests.get(url)

            # Raise an exception if the request was unsuccessful, otherwise process as normal

            response.raise_for_status()

            data = response.json()  # Assuming JSON responses; adjust parsing for different content types

            responses.append({"url": url, "data": data})

        except requests.RequestException as e:

            print(f"API fetch failed for {url}: {e}")

            continue


    return responses


# Example usage with a list of API endpoints to be fetched

api_endpoints = ["https://api.example.com/data1", "https://apistaticendpoint.com"]

fetched_apis = fetch_api(api_endpoints)

