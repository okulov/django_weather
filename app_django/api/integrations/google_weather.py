import requests
from bs4 import BeautifulSoup
from requests import PreparedRequest

# Source: https://www.geeksforgeeks.org/how-to-extract-weather-data-from-google-in-python/

class UncorrectCity(Exception):
    pass


class InvalidRequest(Exception):
    pass


def get_temperature(city: str = "New York"):
    query = "weather" + city
    google_address = "https://www.google.com/search"
    params = {'q': query}
    req = PreparedRequest()
    req.prepare_url(google_address, params)
    url = req.url

    # requests instance
    try:
        html = requests.get(url).content

        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')

        # get the temperature
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

        # this contains time and sky description
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

        # format the data
        data = str.split('\n')
        time = data[0]
        sky = data[1]

        # list having all div tags having particular class name
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

        # particular list with required data
        strd = listdiv[5].text

        # formatting the string
        pos = strd.find('Wind')
        return temp, time, sky, pos
    except AttributeError as e:
        raise UncorrectCity()
    except Exception as e:
        raise InvalidRequest()


if __name__ == '__main__':
    temp, time, sky, pos = get_temperature()
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print("Wind: ", pos)
