from flask import Flask, request
from app.scrappers import category_scrapper, last_episodes_scrapper, anime_category_scrapper, anime_by_name_scrapper, \
    anime_by_slug_scrapper, episode_by_slug_scrapper

app = Flask("anime-scrapper")


@app.route('/')
def health_check():
    return {
        "status": 200,
        "msg": "ok"
    }


@app.route('/categories')
def get_all_categories():
    allCategories = category_scrapper.get_all_categories()

    return {'allCategories': allCategories}


@app.route('/last-episodes')
def get_last_episodes():
    lastEpisodes = last_episodes_scrapper.get_last_episodes()

    return {'lastEpisodes': lastEpisodes}


@app.route('/animes/category')
def get_animes_by_category():
    try:
        category = request.args.get("category")
        page = request.args.get("page") or 0
        result = anime_category_scrapper.get_all_animes_by_category_url(category, page)

        return {'allAnimes': result}
    except Exception as exception:
        print(exception)

        return {
            'erro': True,
            'message': 'anime not found'
        }


@app.route('/animes/name')
def get_anime_by_name():
    try:
        name = request.args.get("name")
        page = request.args.get("page") or 0
        result = anime_by_name_scrapper.get_animes_by_name_and_page(name, page)

        return {'allAnimes': result}
    except Exception as exception:
        print(exception)
        return {
            'erro': True,
            'message': 'Houve um erro interno!',
        }


@app.route('/anime/slug')
def get_anime_by_slug():
    slug = request.args.get("slug")
    animeData = anime_by_slug_scrapper.get_anime_data_by_slug(slug)

    return {'animeData': animeData}


@app.route('/episode/slug')
def get_episode_by_slug():
    slug = 'boku-no-hero-academia-4-episodio-25'
    episodeData = episode_by_slug_scrapper.get_episode_by_slug(slug)

    return {'episode': episodeData}