import requests as rq
print(rq)
BASE_URL="https://pokeapi.co/api/v2/"
x=rq.get(BASE_URL + "pokemon/" + "pikachu")
print(x.text,"x")