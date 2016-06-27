import requests

url = "http://swapi.co/api/people"
swapi_dict = {
  1: "http://swapi.co/api/people/",
  2: "http://swapi.co/api/planets/",
  3: "http://swapi.co/api/films/",
  4: "http://swapi.co/api/species/",
  5: "http://swapi.co/api/vehicles/",
  6: "http://swapi.co/api/starships/",
}

response = requests.get(url).json()

choice = int(input("1 for People, 2 for Planets "))

if choice == 1:
    for people in response['results']:
        print(people['name'])
elif choice == 2:
    for planets in response['results']:
        print(planets['name'])
