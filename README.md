# Hallo gangsters!

Zorg dat je django op je systeem hebt staan

```commandline
pip install django djangorestframework
```

Dan moet je in de root van dit project zeggen `hanki panky` nee eigenlijk niet maar wel

```commandline
python manage.py runserver
```

Er zijn op het moment 2 api calls

- Games
- Genres

De code is te vinden in `/api/views.py`

---

## Games

#### GET

URL: `/games`
Response: Je krijgt een lijst van alle games terug

```json
{
  "games": [
    {},
    {},
    {}
  ]
}
```

#### POST

URL: `/games`
Body: 
```
CONTENT_TYPE: multipart/form-data
REQUEST_BODY:
    game_id: 111111
```

Response: Dit is een search op game_id

```json
{
  "game": {}
}
```

---

URL: `/games`
Body: 
```
CONTENT_TYPE: multipart/form-data
REQUEST_BODY:
    game_name: 111111
```

Response: Dit is een search op game_name

```json
{
  "game": {}
}
```

---

URL: `/games`
Body: 
```
CONTENT_TYPE: multipart/form-data
REQUEST_BODY:
    game_genres: "[\"Action\", \"Adventure\"]"
    game_genres_min_match: 2
    game_genres_max: 4
```

`game_genres` is json in een string. Dit zijn de genres waarop gezocht wordt
`game_genres_min_match` is het minimaal aantal genres wat moet matchen
`game_genres_max` is het maximaal aantal games wat je terug wilt hebben

*Zonder max*
Response:

```json
{
  "games": {
    "4": [
      {},
      {}
    ],
    "3": [
      {}
    ]
  }
}
```

De `4` en `3` houd in hoeveel genres overeen komen met de zoektermen

*Met max*

```json
{
  "games": [
    {},
    {},
    {},
    {}
  ]
}
```

Dit is gesorteerd op eerste game heeft meeste overeenkomende genres

## Genres

#### GET

URL: `/genres`
Response: Je krijgt een lijst van alle genres terug

```json
{
  "genres": [
    {},
    {},
    {}
  ]
}
```
