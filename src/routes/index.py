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
def group(user=None):
    print(f" [!] /<user>", flush=True)

    movies = []

    try:

        print(f" [!] /<user>", flush=True)

        newletterboxdRadarr = letterboxdRadarr()
        movies = newletterboxdRadarr.watchlist()

    except Exception as e:
        print(f" [!] Exception index.route group[{e}]", flush=True)


    return jsonify(movies)
    return '¡Hola, mundo!'


