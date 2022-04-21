import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
animeUrl = os.environ.get('ANIME_SITE_URL')
categoryUrlSulfix = 'generos/'


def get_page():
    page = requests.get(animeUrl + categoryUrlSulfix)
    soap = BeautifulSoup(page.content, 'html.parser')

    return soap


def get_category_div():
    soap = get_page()
    categoryDiv = soap.find_all('div', attrs={'class': 'wp-content'})

    return categoryDiv


def get_all_categories():
    categoryDiv = get_category_div()
    categoryList = []
    for category_content in categoryDiv[0].contents:
        slug = get_category_slug(category_content)

        category = {
            'name': category_content.find('a').contents[0],
            'slug': slug
        }
        categoryList.append(category)

    return categoryList


def get_category_slug(category_content):
    categoryUrl = category_content.contents[0].attrs['href']
    splitedUrl = categoryUrl.split('/')

    return splitedUrl[len(splitedUrl) - 2]
