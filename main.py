import requests

swapi_dict = {
  1: ["http://swapi.co/api/people/", "name"],
  # 2: "http://swapi.co/api/planets/",
  2: ["http://swapi.co/api/films/", "title"],
  # 4: "http://swapi.co/api/species/",
  3: ["http://swapi.co/api/vehicles/", "name"],
  # 6: "http://swapi.co/api/starships/",
}

choice = int(input("""
1 Characters
2 Films
3 Vehicles
"""))

url, look_up = swapi_dict[choice]

if choice == 1:
    response = requests.get(url).json()
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item[look_up])
            url = response['next']
            response = requests.get(url).json()
    else:
        for item in response['results']:
            print(item[look_up])
if choice == 2:
    response = requests.get(url).json()
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item[look_up])
            url = response['next']
            response = requests.get(url).json()
    else:
        for item in response['results']:
            print(item[look_up])

if choice == 3:
    response = requests.get(url).json()
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item[look_up])
            url = response['next']
            response = requests.get(url).json()
    else:
        for item in response['results']:
            print(item[look_up])



# would you like to get more results? like to see some detail? type 1
