import requests as rq
lista_de_pokemon=["pikachu","charizard","squirtle","Bulbasaur"]

BASE_URL="https://pokeapi.co/api/v2/"

for x in lista_de_pokemon:
    pokemon={"nome":"","nome":"","nome":"","nome":"",}
    print(x)

    k=rq.get(BASE_URL + "pokemon/" + x )

    resposta=k.json()
    resposta["abilities"]
    print(resposta["abilities"])
#for y in resposta:
 # print(y)
