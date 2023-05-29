from flask import (
    Blueprint,
    jsonify
)

from controllers.letterboxdRadarr import letterboxdRadarr


import json
import random
import time
import asyncio
from datetime import datetime

import os


index = Blueprint("index", __name__)



@index.route("/<user>/watchlist/")
def watchlist(user=None):
    fecha_hora_actual = datetime.now()
    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

    print(f" [!] watchlist {cadena_fecha_hora}", flush=True)
    movies = []
    try:
        newletterboxdRadarr = letterboxdRadarr()
        movies = newletterboxdRadarr.watchlist(user)
    except Exception as e:
        print(f" [!] Exception index.route watchlist [{e}]", flush=True)
    return jsonify(movies)

@index.route("/<user>/films/")
def films(user=None):
    fecha_hora_actual = datetime.now()
    cadena_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

    print(f" [!] films {cadena_fecha_hora}", flush=True)
    movies = []
    try:
        newletterboxdRadarr = letterboxdRadarr()
        movies = newletterboxdRadarr.films(user)
    except Exception as e:
        print(f" [!] Exception index.route films [{e}]", flush=True)
    return jsonify(movies)

