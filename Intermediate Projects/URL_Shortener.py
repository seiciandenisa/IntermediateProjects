from typing import Final
import requests

API_KEY: Final[str] = '16d6787c554bc762a890dee06589280e77291'  # from cuttly account -> to make requests
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'  # from cuttly account -> used to make the API request


def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}  # the setting used to make a request
    # the parameters for the payload can be found on cuttly
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link: ', short_link)
            # the status is from the API documentation, and it's the one that states that the link has been shortened
            # this will check if we got a valid response back and print the link to the user
        else:
            print('Error status: ', url_data['status'])


def main():
    input_link: str = input('Enter a link: ')
    shorten_link(input_link)


if __name__ == '__main__':
    main()

# include try and except blocks
# there are more statuses include them also
