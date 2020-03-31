# Function get_data_from_URL takes in a URL
# for an API request and then returns the data (json).
# Returns the dictionary which was json file.

# This module tests the received file.
# Also here we use the search of artist by id.
# This file is about the artist Jack Johnson

import requests
import json

url = "https://itunes.apple.com/lookup?id=909253"


def get_data_from_URL(url):
    """(str) -> dict
    Function for getting data from URL (iTunes)
    """
    payload = ""
    headers = {
        'x-rapidapi-host': "iTunesvolodimir-kudriachenkoV1.p.rapidapi.com",
        'x-rapidapi-key': "SIGN-UP-FOR-KEY",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    received_file = json.loads(response.text)
    return received_file


def main():
    """NoneType -> NoneType
    Creates a file (this is data which was got from URL)
    Tests the received file
    """
    data = get_data_from_URL(url)
    print('Length of data:', len(data))
    print(data.keys())
    print("Length of first ([0]) results:", len(data['results'][0]))
    print("Keys of first ([0]) results:", data['results'][0].keys())
    print("Name of artist:", data['results'][0]['artistName'])
    print("Primary genre name:", data['results'][0]['primaryGenreName'])


if __name__ == "__main__":
    main()
