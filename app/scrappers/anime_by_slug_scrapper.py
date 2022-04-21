import os
import bs4.element
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
animeUrl = os.environ.get('ANIME_SITE_URL')
animeBySlugUrlSulfix = 'anime/'


def get_page_by_url(url):
    page = requests.get(url)
    soap = BeautifulSoup(page.content, 'html.parser')

    return soap


def get_url_by_slug(slug):
    return animeUrl + animeBySlugUrlSulfix + slug


def get_anime_data_by_slug(slug):
    url = get_url_by_slug(slug)
    page = get_page_by_url(url)

    return {
        'title': get_anime_title(page),
        'year': get_anime_year(page),
        'tags': get_anime_tags(page),
        'sinopse': get_sinopse(page),
        'seasons': get_all_seasons(page)
    }


def get_anime_title(page):
    return page.find_all('h1')[0].contents[0]


def get_anime_year(page):
    aboutDiv = page.find('div', attrs={'class': 'sheader'})

    return aboutDiv.find('span', attrs={'class': 'date'}).contents[0]


def get_anime_tags(page):
    tagArrayToReturn = []
    tagsDiv = page.find('div', attrs={'class': 'sgeneros'}).contents
    for div in tagsDiv:
        if isinstance(div, bs4.element.Tag):
            tagArrayToReturn.append(div.contents[0])

    return tagArrayToReturn


def get_sinopse(page):
    return page.find('div', attrs={'class': 'wp-content'}).find('p').contents[2]


def get_all_seasons(page):
    seasonArrayToReturn = []
    seasonDivs = page.find_all('div', attrs={'class': 'se-c'})
    for seasonDiv in seasonDivs:
        if isinstance(seasonDiv, bs4.element.Tag):
            seasonObject = get_season_data(seasonDiv)
            seasonArrayToReturn.append(seasonObject)

    return seasonArrayToReturn


def get_season_data(season_div):
    seasonName = get_season_name(season_div)
    episodes = get_season_episodes(season_div)

    return {
        seasonName: episodes
    }


def get_season_name(season_div):
    seasonNameDiv = season_div.contents[0]

    return seasonNameDiv.find_all('span', attrs={'class': 'title'})[0].contents[0]


def get_season_episodes(season_div):
    episodesArrayToReturn = []
    liArray = season_div.find_all('li')
    for episodeLi in liArray:
        if isinstance(episodeLi, bs4.element.Tag):
            episodeData = get_episode_data(episodeLi)
            episodesArrayToReturn.append(episodeData)

    return episodesArrayToReturn


def get_episode_data(episode_li):
    return {
        'titulo': get_episode_title(episode_li),
        'slug': get_episode_slug(episode_li),
        'date': get_episode_date(episode_li),
        'posterUrl': get_anime_poster_url(episode_li),
    }


def get_episode_title(episode_li):
    return episode_li.find('div', attrs={'class': 'episodiotitle'}).find_all('a')[0].contents[0]


def get_episode_slug(episode_li):
    episodeUrl = episode_li.contents[0].contents[0].attrs['href']
    splitedUrl = episodeUrl.split('/')

    return splitedUrl[len(splitedUrl) - 2]


def get_episode_date(episode_li):
    return episode_li.find('div', attrs={'class': 'episodiotitle'}).find_all('span')[0].contents[0]


def get_anime_poster_url(episode_li):
    return episode_li.find('img').attrs['src']
