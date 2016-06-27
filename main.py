import requests
import sys

def results(response, look_up):
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item[look_up])
            url = response['next']
            response = requests.get(url).json()
    else:
        for item in response['results']:
            print(item[look_up])

def get_swapi_data(choice):
    url, look_up = swapi_dict[choice]
    response = requests.get(url).json()
    results(response, look_up)

swapi_dict = {
  1: ["http://swapi.co/api/people/", "name"],
  # 2: "http://swapi.co/api/planets/",
  2: ["http://swapi.co/api/films/", "title"],
  # 4: "http://swapi.co/api/species/",
  3: ["http://swapi.co/api/vehicles/", "name"],
  # 6: "http://swapi.co/api/starships/",
}
while True:
    choice = int(input("""
    1 Characters
    2 Films
    3 Vehicles
    0 Exit
    """))

    if choice == 0:
        exit()
    get_swapi_data(choice)
    


        # more_info = input("Would you like details on a character? Y/n ").lower()
        # if more_info == 'y':
        #     person = input("Type in the character's name: ").lower()
        #     print(response['name'])



# would you like to get more results? like to see some detail? type 1
