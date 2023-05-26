import json
import os
import re
import requests
from bs4 import BeautifulSoup
import concurrent.futures

class letterboxdRadarr:

    def __init__(self):
        self._version = "1.10.0"
        self.max_workers = 30

    def watchlist(self,username):
        print('watchlist')
        watched_movies = []
        movies = []
        session = requests.Session()

        count = 0
        while True:
            count += 1

            watchlist_url = "https://letterboxd.com/{}/watchlist/page/{}/".format(username, count)
            search_page = session.get(watchlist_url)
            search_soup = BeautifulSoup(search_page.content, "html.parser")
            _movies = search_soup.findAll("div", {"class": "film-poster"})
            if _movies:
                for _movie in _movies:
                    movies.append(_movie)
            else: break

        print(f'movie_link  => "{movies}"')
        # Realizar las solicitudes en paralelo
        #{"id":484247,
        # "imdb_id":"tt7040874",
        # "title":"A Simple Favor",
        # "release_year":"2018",
        # "clean_title":"/film/a-simple-favor/",
        # "adult":false}

        return self.concurrent(movies)

    def getDetailsMovie(self, movie):
        imdb_id = ''
        themoviedb = ''

        title = movie['data-film-slug']
        watchlist_url = f"https://letterboxd.com{title}"

        session = requests.Session()
        search_page = session.get(watchlist_url)

        IMDB_REGEX = r'http://www\.imdb\.com/title/(tt\d+)/'
        TMDB_REGEX = r'https://www\.themoviedb\.org/movie/(\d+)/'
        id_pattern = r'filmData.*?id:\s(\d+)'
        release_year_pattern = r'filmData.*?releaseYear:\s"(\d+)"'

        imdb_id_match = re.search(IMDB_REGEX, search_page.text)
        themoviedb_match = re.search(TMDB_REGEX, search_page.text)

        if imdb_id_match: imdb_id = imdb_id_match.group(1)
        if themoviedb_match: themoviedb = themoviedb_match.group(1)

        id_match = re.search(id_pattern, search_page.text)
        release_year_match = re.search(release_year_pattern, search_page.text)
        if id_match: id_value = id_match.group(1)
        if release_year_match: release_year_value = release_year_match.group(1)
        return {'imdb_id': imdb_id, 
                'themoviedb': themoviedb, 
                'id': id_value, 
                'title': movie.find('img')['alt'],
                'release_year': release_year_value, 
                "clean_title": movie['data-film-slug'] }
    
    def films(self,username):
        print('watchlist')
        watched_movies = []
        movies = []
        session = requests.Session()

        count = 0
        while True:
            count += 1

            watchlist_url = "https://letterboxd.com/{}/films/page/{}/".format(username, count)
            search_page = session.get(watchlist_url)
            search_soup = BeautifulSoup(search_page.content, "html.parser")
            _movies = search_soup.findAll("div", {"class": "film-poster"})
            if _movies:
                for _movie in _movies:
                    movies.append(_movie)
            else: break

        print(f'movie_link  => "{movies}"', flush=True)
        
        return self.concurrent(movies)

    def concurrent(self, movies):
        watched_movies = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Iterar sobre las URLs y enviar las solicitudes
            futures = [executor.submit(self.getDetailsMovie, movie) for movie in movies]
    
        # Obtener los resultados a medida que se van completando las solicitudes
        for future in concurrent.futures.as_completed(futures):
            resultado = future.result()
            watched_movies.append(resultado)

        return watched_movies
