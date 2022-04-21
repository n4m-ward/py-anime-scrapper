import os
import bs4.element
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
animeUrl = os.environ.get('ANIME_SITE_URL')
animeByNameUrlSulfix = 'search/'


def get_animes_by_name_and_page(name, page):
    url = get_url_by_name(name, page)
    page = get_page_by_url(url)

    return get_array_of_animes(page)


def get_array_of_animes(page):
    arrayToReturn = []
    for content in page.find_all('div', attrs={'id': 'archive-content'}):
        if isinstance(content, bs4.element.Tag):
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
    animeUrl = content.findAll('a')[1].attrs['href']
    splitedUrl = animeUrl.split('/')

    return splitedUrl[len(splitedUrl) - 2]


def get_poster_url(content):
    return content.find('img').attrs['src']


def get_page_by_url(url):
    page = requests.get(url)
    soap = BeautifulSoup(page.content, 'html.parser')

    return soap


def get_url_by_name(name, page):
    name = name.replace(' ', '+')
    fullAnimeUrl = animeUrl + animeByNameUrlSulfix + name

    if page == 0:
        return fullAnimeUrl

    return fullAnimeUrl + '/page/' + str(page)
