import codecs
import json
import random
from pathlib import Path

from django.http import JsonResponse

base_dir = Path(__file__).resolve().parent
game_file = Path(base_dir, "games.json")

json_file = codecs.open(game_file, encoding="utf-8")
json_games = json.load(json_file)["games"]


def get_games(request):
    if request.method == "POST":
        game_id = request.POST.get("game_id")
        game_name = request.POST.get("game_name")
        game_genres = request.POST.get("game_genres")

        game = None

        if game_id:
            game = find_game_by("appid", int(game_id))

        if game_name:
            game = find_game_by("name", game_name)

        if game_genres:
            game_genres_needle = json.loads(game_genres)

            min_match = request.POST.get("game_genres_min_match") or len(game_genres_needle)
            max_match = request.POST.get("game_genres_max")

            found_games = find_games_by_genres(game_genres_needle, int(min_match))

            if max_match:
                max_games = []
                keys = list(found_games.keys())
                key_index = 0

                for i in range(0, int(max_match)):
                    length = len(found_games[keys[key_index]])

                    if length == 1:
                        max_games.append(found_games[keys[key_index]][0])
                        key_index += 1
                    else:
                        random_number = random.randint(0, length - 1)
                        random_game = found_games[keys[key_index]][random_number]
                        max_games.append(random_game)
                        found_games[keys[key_index]].pop(random_number)

                return JsonResponse({
                    "games": max_games
                })

            return JsonResponse({
                "games": found_games
            })

        if game is None:
            return JsonResponse({
                "status": 404,
                "message": "Game not found"
            }, status=404)

        return JsonResponse({
            "game": game
        })

    return JsonResponse({
        "games": json_games
    })


def get_genres(request):
    genres = []

    for game in json_games:
        for game_genre in game["genres"]:
            if game_genre not in genres:
                genres.append(game_genre)

    return JsonResponse({
        "genres": genres
    })


def find_game_by(key, value):
    for game in json_games:
        if game[key] == value:
            return game


def find_games_by_genres(genres, min_match):
    found_games = {}

    for game in json_games:
        matching_genres = 0
        for game_genre in game["genres"]:
            if game_genre["description"] in genres:
                matching_genres += 1

        if matching_genres > 0 and matching_genres > min_match - 1:
            if matching_genres in found_games.keys():
                found_games[matching_genres].append(game)
            else:
                found_games[matching_genres] = [game]

    sorted_games = {}

    for key in sorted(found_games.keys(), reverse=True):
        if key < min_match:
            continue

        sorted_games[key] = found_games[key]

    return sorted_games
