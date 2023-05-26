from flask import (
    Blueprint,
    jsonify
)

from controllers.letterboxdRadarr import letterboxdRadarr


import json
import random
import time
import asyncio

import os


index = Blueprint("index", __name__)



@index.route("/<user>/watchlist")
def watchlist(user=None):
    print(f" [!] /<user>", flush=True)
    movies = []
    try:
        print(f" [!] /<user>", flush=True)
        newletterboxdRadarr = letterboxdRadarr()
        movies = newletterboxdRadarr.watchlist(user)
    except Exception as e:
        print(f" [!] Exception index.route group[{e}]", flush=True)
    return jsonify(movies)
    return '¡Hola, mundo!'

@index.route("/<user>/films")
def films(user=None):
    print(f" [!] /<user>", flush=True)
    movies = []
    try:
        print(f" [!] /<user>", flush=True)
        newletterboxdRadarr = letterboxdRadarr()
        movies = newletterboxdRadarr.films(user)
    except Exception as e:
        print(f" [!] Exception index.route group[{e}]", flush=True)
    return jsonify(movies)
    return '¡Hola, mundo!'


