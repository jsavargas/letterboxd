import json
import os
import re
import requests
from bs4 import BeautifulSoup

class letterboxdRadarr:

    def __init__(self):
        self._version = "1.10.0"
        self.app_id = 'APP_ID'

    def watchlistv(self):

        data = [{"id":484247,"imdb_id":"tt7040874","title":"A Simple Favor","release_year":"2018","clean_title":"/film/a-simple-favor/","adult":False}
        ,{"id":557950,"imdb_id":"tt9224288","title":"Mainstream","release_year":"2020","clean_title":"/film/mainstream-2020/","adult":False}
        ,{"id":204082,"imdb_id":"tt2312718","title":"Homefront","release_year":"2013","clean_title":"/film/homefront/","adult":False}
        ,{"id":827681,"imdb_id":"tt15496702","title":"The Lost Year 1986","release_year":"2022","clean_title":"/film/the-lost-year-1986/","adult":False}
        ,{"id":798286,"imdb_id":"tt13521006","title":"Beau Is Afraid","release_year":"2023","clean_title":"/film/beau-is-afraid/","adult":False}
        ,{"id":840326,"imdb_id":"tt14846026","title":"Sisu","release_year":"2022","clean_title":"/film/sisu-2022/","adult":False}
        ,{"id":14337,"imdb_id":"tt0390384","title":"Primer","release_year":"2004","clean_title":"/film/primer/","adult":False}
        ,{"id":569094,"imdb_id":"tt9362722","title":"Spider-Man: Across the Spider-Verse","release_year":"2023","clean_title":"/film/spider-man-across-the-spider-verse/","adult":False}
        ,{"id":713704,"imdb_id":"tt13345606","title":"Evil Dead Rise","release_year":"2023","clean_title":"/film/evil-dead-rise/","adult":False}
        ,{"id":502356,"imdb_id":"tt6718170","title":"The Super Mario Bros. Movie","release_year":"2023","clean_title":"/film/the-super-mario-bros-movie/","adult":False}
        ,{"id":964980,"imdb_id":"tt16419074","title":"Air","release_year":"2023","clean_title":"/film/air-2023/","adult":False}
        ,{"id":881,"imdb_id":"tt0104257","title":"A Few Good Men","release_year":"1992","clean_title":"/film/a-few-good-men/","adult":False}
        ]
        
        return data
    
    def watchlist(self):
        print('watchlist')
        username = 'jsavargas'
        watched_movies = []
        session = requests.Session()

        watchlist_url = "https://letterboxd.com/{}/watchlist/".format(username)
        
        search_page = session.get(watchlist_url)
        #print(f'search_page "{search_page.text}" "{watchlist_url}"')
        search_soup = BeautifulSoup(search_page.content, "html.parser")


        #watched_movies = [{'title':movie.get('title'),'accountID':movie.get('accountID')} for movie in movies if movie.get('type') == 'movie' and movie.get('accountID') == '1']


        # Obtener el enlace de la película
        #watched_movies = search_soup.findAll("div", {"class": "film-poster"})
        #watched_movies = [{'clean_title':movie['data-film-slug'], 'title':movie.find('img')['alt']} for movie in search_soup.findAll("div", {"class": "film-poster"})]
        for movie in search_soup.findAll("div", {"class": "film-poster"}):
            details = self.getDetailsMovie(movie['data-film-slug'])
            watched_movies.append({
                'id':details['id'],
                'imdb_id':details['imdb_id'],
                'title':movie.find('img')['alt'],
                'release_year':details['release_year'],
                'clean_title':movie['data-film-slug'], 
                'themoviedb':details['themoviedb'],
                'adult': False
                } )
            #break
        print('watchlist')
        print(f'movie_link  => "{watched_movies}"')

        #{"id":484247,
        # "imdb_id":"tt7040874",
        # "title":"A Simple Favor",
        # "release_year":"2018",
        # "clean_title":"/film/a-simple-favor/",
        # "adult":false}

        return watched_movies
    
    def getDetailsMovie(self, movie):
        print('getDetailsMovie 1')
        imdb_id = ''
        themoviedb = ''

        watchlist_url = f"https://letterboxd.com{movie}"

        session = requests.Session()
        search_page = session.get(watchlist_url)
        #print(f'search_page "{search_page.text}" "{watchlist_url}"')
        #search_soup = BeautifulSoup(search_page.content, "html.parser")

        IMDB_REGEX = r'http://www\.imdb\.com/title/(tt\d+)/'
        TMDB_REGEX = r'https://www\.themoviedb\.org/movie/(\d+)/'

        #watched_movies = search_soup.find("div", {"class": "film-poster"})
        imdb_id_match = re.search(IMDB_REGEX, search_page.text)
        themoviedb_match = re.search(TMDB_REGEX, search_page.text)
        print('getDetailsMovie 2')

        if imdb_id_match: imdb_id = imdb_id_match.group(1)
        if themoviedb_match: themoviedb = themoviedb_match.group(1)

        id_pattern = r'filmData.*?id:\s(\d+)'
        release_year_pattern = r'filmData.*?releaseYear:\s"(\d+)"'

        id_match = re.search(id_pattern, search_page.text)
        release_year_match = re.search(release_year_pattern, search_page.text)
        if id_match: id_value = id_match.group(1)
        if release_year_match: release_year_value = release_year_match.group(1)
        return {'imdb_id':imdb_id, 'themoviedb':themoviedb, 'id': id_value, 'release_year':release_year_value }