import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, city):
        self.url = 'https://www.wetteronline.de/wetter/' + city
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def get_temperature(self):
        return self.soup.find(id='nowcast-card-temperature').find(class_='value').text

    def get_day_summary(self):
        return self.soup.find(class_='report-text').text


def get_weather():
    city = input('City: ')
    s = Scraper(city)
    return s.get_day_summary()
