# py-anime-scrapper

## Dependencias necessarias:

- python 3 ou superior
- pip

## how to run the project:

```
pip install -r requirements.txt
flask run
```

## Documentação - Endpoints

### GET - /categories

#### Pega todas as categorias do site

#### Exemplo de requisição:

```
localhost:5000/categories
```

#### Exemplo de resposta:

```
{
    "allCategories": [
        {
            "name": "Ação",
            "slug": "acao"
        },
        {
            "name": "Artes Marciais",
            "slug": "artes-marciais"
        }
}
```

### GET - /last-episodes

#### Pega todos os ultimos episodios lançados.

#### Exemplo de requisição:

```
localhost:5000/last-episodes
```

#### Exemplo de resposta:

```
{
    "lastEpisodes": [
        {
            "image": "https://animesonline.cc/wp-content/uploads/2019/07/gQODK1aRngAfkCqBNqKrHyCtdqY-300x169.jpg",
            "quality": "Legendado",
            "slug": "darling-in-the-franxx-episodio-1",
            "title": "Darling in the Franxx Episodio 1"
        },
        {
            "image": "https://animesonline.cc/wp-content/uploads/2020/04/k9FPjWsC0DNnVThIULcdEVuPn6h-300x169.jpg",
            "quality": "Legendado",
            "slug": "boku-no-hero-academia-4-episodio-25",
            "title": "Boku no Hero Academia 4 Episodio 25"
        }
}
```

### GET - /animes/category

#### Pega uma lista de animes por categoria

#### Parametros

- **category**: Slug pego no endpoint `/categories`
- **page**: Numero da paginação do site. **Default 0**.

#### Exemplo de requisição:

```
localhost:5000/animes/category?category=artes-marciais&page=2
```

#### Exemplo de resposta

```
{
    "allAnimes": [
        {
            "name": "Baki Hanma",
            "poster_url": "https://animesonline.cc/wp-content/uploads/2021/10/mHMKMla5q7jThEEqzINPbozMPKe-185x278.jpg",
            "slug": "baki-hanma"
        },
        {
            "name": "Martial Master (Wu Shen Zhu Zai)",
            "poster_url": "https://animesonline.cc/wp-content/uploads/2020/11/r0uS45gd4q5fo71XqQQCpaBJqPC-185x278.jpg",
            "slug": "wu-shen-zhu-zai"
        }
}
```

### GET - /animes/name

#### Pega um ou varios animes que contem o nome buscado.

#### Parametros

- **name**: Nome do anime.
- **page**: Numero da paginação do site. **Default 0**.

#### Exemplo de requisição:

```
localhost:5000/animes/category?name=naruto&page=0
```

#### Exemplo de resposta:

```
{
    "allAnimes": [
        {
            "name": "Boruto: Naruto Next Generations",
            "poster_url": "https://animesonline.cc/wp-content/uploads/2020/09/7dde3a40ce5d5615813a5ac12683631a1616450115-185x278.jpg",
            "slug": "boruto-naruto-next-generations"
        },
        {
            "name": "Naruto Shippuden",
            "poster_url": "https://animesonline.cc/wp-content/uploads/2019/09/ic9Gb4Zz09ns3JPYHdax8u5kt0n-185x278.jpg",
            "slug": "naruto-shippuden"
        },
        {
            "name": "Naruto Clássico Dublado",
            "poster_url": "https://animesonline.cc/wp-content/uploads/2019/06/lTVhwFcSHqN0Xv8HLxDHILtrwfX-185x278.jpg",
            "slug": "naruto"
        }
    ]
}
```

### GET - /anime/slug

#### Pega uma lista com titulo, sinopse, tags, lista de episodios separado por temporada e ano de lançamento.

#### Parametros

- **slug**: Slug do anime pego no endpoints `/animes/category` ou no endpoint `/animes/name`.

#### Exemplo de requisição:

```
localhost:5000/anime/slug?slug=naruto-shippuden
```

#### Exemplo de resposta

```
{
  "animeData": {
   "seasons":[
      {
         "Temporada  1 ":[
            {
               "date":"Feb. 15, 2007",
               "posterUrl":"https://animesonline.cc/wp-content/uploads/2019/09/lFg0YnHI7sJkPSv38a8ctE96sqr-300x170.jpg",
               "slug":"naruto-shippuden-episodio-1",
               "titulo":"Episodio 1"
            },
            {
               "date":"Feb. 15, 2007",
               "posterUrl":"https://animesonline.cc/wp-content/uploads/2019/09/zbvJ4ts4JJmqP6koMNnLzBX6qiJ-300x170.jpg",
               "slug":"naruto-shippuden-episodio-2",
               "titulo":"Episodio 2"
            }
         ],
         "Temporada  2 ":[...]
      }
   ]
      "sinopse": " Naruto Shippuuden ocorre 2 anos e meio após Naruto ter ficado para  treinar com Jiraiya. Após seu retorno, Naruto descobre que seus amigos  shinobi’s o superaram na classificação, e ele caiu para trás. No  entanto, com apenas 6 meses para resgatar Sasuke, Naruto tem de  enfrentar inimigos ainda mais perigosos. O plano da Akatsuki se revela  lentamente e os perigos surgem mais do que nunca!",
      "tags": [
          "Ação",
          "Artes Marciais",
          "Aventura",
          "Comédia",
          "Dublado",
          "Legendado",
          "Letra N",
          "Shounen",
          "Super Poderes"
      ],
      "title": "Naruto Shippuden Todos os Episodios Online",
      "year": "2007"
  }
}
```

### GET - /episode/slug

#### Pega as opções de video disponivel para um episodio, a partir do slug, contendo o video legendado/dublado e/ou full HD (isMp4).

#### Parametros

- **slug**: Slug do episodio pego no endpoint `/animes/slug?slug=slug` ou no endpoint `/last-episodes`.

#### Exemplo de requisição:

```
localhost:5000/episode/slug?slug=boku-no-hero-academia-4-episodio-25
```

#### Exemplo de resposta

```
{
    "episode": {
        "episodeData": {
            "option-1": {
                "isMp4": false,
                "option": " Dublado ",
                "videoUrl": "https://www.blogger.com/video.g?token=AD6v5dzhFy2A6_Bh7pHkfS-CUn12W34VI5Tn-zBI91JsDZJBJmfa_ucA0gh8Bw5E30VnzWxLi2M3lHh8o6puLfW3doBVuozM7dJM_F-qpTHOINCYtSdr6wnlbzmdKZneQwFE_vhumHk"
            },
            "option-2": {
                "isMp4": false,
                "option": " Legendado ",
                "videoUrl": "https://www.blogger.com/video.g?token=AD6v5dxLdWI9Y5DgeorLFpz3YZBpAkVpPzqE5wyEoWLxnev-OhonKRD6pneDb8JLsEwKUjGNrYYYwYL3hkZ3EoLJHftwPy3g_5sL7dhZ9zfwlGpm9716D1dFE1sGkin9ujtYbvSl93if"
            }
        },
        "image": "https://animesonline.cc/wp-content/uploads/2020/04/k9FPjWsC0DNnVThIULcdEVuPn6h-300x169.jpg",
        "seoDescription": "Boku no Hero Academia 4 Episodio 25 Online, Assistir Boku no Hero Academia 4 Episodio 25 Completo, Assistir Boku no Hero Academia 4 ep 25 HD, Animes Online.",
        "title": "Boku no Hero Academia 4 Episodio 25 Online"
    }
}
```
