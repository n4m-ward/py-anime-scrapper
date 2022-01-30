import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
animeUrl = os.environ.get('ANIME_SITE_URL')
lastEpisodesPageSulfix = 'tv/'


def get_page():
    page = requests.get(animeUrl + lastEpisodesPageSulfix)
    soap = BeautifulSoup(page.content, 'html.parser')

    return soap


def get_last_episodes_div():
    soap = get_page()
    lastEpisodesDiv = soap.find_all('div', attrs={
        'class': 'items',
        'id': 'blog'
    })

    return lastEpisodesDiv[0]


def get_last_episodes():
    episodesArray = []
    for episodeObject in get_last_episodes_div():
        episode = {
            'image': get_episode_image_url(episodeObject),
            'link': get_episode_slug(episodeObject),
            'title': get_episode_title(episodeObject),
            'quality': get_episode_quality(episodeObject),
        }

        episodesArray.append(episode)

    return episodesArray


def get_episode_image_url(episodeObject):
    return episodeObject.contents[0].contents[1].contents[0].attrs


def get_episode_slug(episodeObject):
    episodeUrl = episodeObject.contents[0].contents[1].attrs['href']
    splitedUrl = episodeUrl.split('/')

    return splitedUrl[len(splitedUrl) - 2]


def get_episode_title(episodeObject):
    return episodeObject.contents[1].contents[0].contents[1].contents[0]


def get_episode_quality(episodeObject):
    return episodeObject.contents[0].contents[3].contents[0]
