# Function get_data_from_URL takes in a URL
# for an API request and then returns the data (json).
# Returns the dictionary which was json file.

# This module tests the received file.
# Also here we use the search of artist.
# This file is about the artist Eminem

import requests
import json

url = 'https://api.deezer.com/artist/eminem'


def get_data_from_URL(url):
    """(str) -> dict
    Function for getting data from URL (DEEZER)
    """
    querystring = {"q": "eminem"}
    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
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
    print("Name of artist:", data['name'])
    print("The number of albums:", data['nb_album'])


if __name__ == "__main__":
    main()
