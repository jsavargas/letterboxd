
# letterboxd rss to radarr

Connect radarr to letterboxd.com lists

### Radarr v3

1. Configure a new list in radarr, using the _Custom Lists_ provider.
2. Set _List URL_ to `http://192.168.0.10:5858` followed by the path to your list in letterboxd. For example: `http://192.168.0.10:5858/jsavargas/watchlist/`
3. Configure the rest of the settings to your liking
4. Test & Save.

### Supported Lists:

-   Watchilsts: https://letterboxd.com<b>/jsavargas/watchlist/</b>
-   Watched Movies: https://letterboxd.com<b>/jsavargas/films/</b>


### Endpoints

-   http://192.168.0.10:5858/jsavargas/watchlist/
-   http://192.168.0.10:5858/jsavargas/films/


### Using docker

#### Building it yourself

```
git clone https://github.com/jsavargas/letterboxd.gitcd
cd letterboxd
docker-compose build 
docker-compose up -d
```