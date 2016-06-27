import requests

swapi_dict = {
  1: "http://swapi.co/api/people/",
  # 2: "http://swapi.co/api/planets/",
  2: "http://swapi.co/api/films/",
  # 4: "http://swapi.co/api/species/",
  3: "http://swapi.co/api/vehicles/",
  # 6: "http://swapi.co/api/starships/",
}

choice = int(input("""
1 Characters
2 Films
3 Vehicles
"""))

url = "http://swapi.co/api/people"

if choice == 1:
    response = requests.get(url).json()
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item['name'])
            url = response['next']
            response = requests.get(url).json()
    else:
        for item in response['results']:
            print(item['name'])



# would you like to get more results? like to see some detail? type 1
