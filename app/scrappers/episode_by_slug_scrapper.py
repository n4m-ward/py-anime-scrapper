import os
import bs4
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()
animeUrl = os.environ.get('ANIME_SITE_URL')
episodeUrlSulfix = 'episodio/'


def get_episode_by_slug(slug):
    url = get_url_by_slug(slug)
    page = get_page_by_url(url)

    return get_all_episode_data(page)


def get_all_episode_data(page):
    return {
        'title': get_episode_title(page),
        'image': get_episode_image(page),
        'episodeData': get_episode_data(page),
        'seoDescription': get_seo_description(page),
    }


def get_episode_title(page):
    return page.find('h1', attrs={'class': 'epih1'}).contents[0]


def get_episode_image(page):
    return page.find('div', attrs={'class': 'imgep'}).find('img').attrs['src']


def get_episode_data(page):
    episodeDataToReturn = {}
    for content in page.find_all('div', attrs={'class': 'fixidtab'}):
        if (isinstance(content, bs4.element.Tag)):
            optionName = content.attrs['id']
            iframe = content.find('iframe')
            isTypeVideo = not iframe
            if isTypeVideo:
                video = content.find('video')
                episodeDataToReturn[optionName] = get_video_data(video)
            else:
                episodeDataToReturn[optionName] = get_iframe_data(iframe)

    return episodeDataToReturn


def get_iframe_data(iframe):
    return {
        'isMp4': False,
        'videoUrl': iframe.attrs['src'],
    }


def get_video_data(video):
    return {
        'isMp4': True,
        'videoUrl': video.find('source').attrs['src'],
        'videoPosterUrl': video.attrs['poster'],
    }


def get_seo_description(page):
    return page.find('div', attrs={'itemprop': 'description'}).find('p').contents[0]


def get_url_by_slug(slug):
    return animeUrl + episodeUrlSulfix + slug


def get_page_by_url(url):
    page = requests.get(url)
    soap = BeautifulSoup(page.content, 'html.parser')

    return soap
