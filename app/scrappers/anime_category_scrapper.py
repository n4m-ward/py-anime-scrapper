import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
animeUrl = os.environ.get('ANIME_SITE_URL')
animeCategoryUrlSulfix = 'genero/'


def get_category_url_by_page(category, page):
    if page == 0:
        return animeUrl + animeCategoryUrlSulfix + category

    return animeUrl + animeCategoryUrlSulfix + category + '/page/' + str(page)


def get_all_animes_by_category_url(category, page):
    arrayToReturn = []
    url = get_category_url_by_page(category, page)
    page = get_page_by_url(url)
    for content in page.find_all('div', attrs={'class': 'items'})[0]:
        animeObject = {
            'name': get_anime_name(content),
            'slug': get_anime_slug(content),
            'poster_url': get_poster_url(content),
        }
        arrayToReturn.append(animeObject)

    return arrayToReturn


def get_anime_name(content):
    return content.findAll('a')[1].contents[0]


def get_anime_slug(content):
    animeUrl = content.find('a').attrs['href']
    splitedUrl = animeUrl.split('/')

    return splitedUrl[len(splitedUrl) - 2]


def get_poster_url(content):
    return content.find('img').attrs['src']


def get_page_by_url(url):
    page = requests.get(url)
    soap = BeautifulSoup(page.content, 'html.parser')

    return soap