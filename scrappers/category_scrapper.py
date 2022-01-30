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
        category = {
            'name': category_content.contents[0].contents[0],
            'link': category_content.contents[0].attrs['href']
        }
        categoryList.append(category)

    return categoryList
