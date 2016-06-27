import requests
import sys

def results(response, name_title, detail_url):
    if response['next']:
        while response['next']:
            for item in response['results']:
                print(item[name_title])
                print(item[detail_url])
            url = response['next']
            response = requests.get(url).json()
    else:
        for item in response['results']:
            print(item[name_title])
            print(item[detail_url])


def get_swapi_data(choice):
    url, name_title, detail_url = swapi_dict[choice]
    response = requests.get(url).json()
    results(response, name_title, detail_url)


swapi_dict = {
  1: ["http://swapi.co/api/people/", "name", "url"],
  # 2: "http://swapi.co/api/planets/",
  2: ["http://swapi.co/api/films/", "title", "url"],
  # 4: "http://swapi.co/api/species/",
  3: ["http://swapi.co/api/vehicles/", "name", "url"],
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


    # for key, value in response['results'].items():
    #     print(key, value)

    # more_info = input("Would you like details? Y/n ").lower()
    # if more_info == 'y':
    #     person = input("Type in name or title: ").lower()
    #     print(['results', 'name'])



# would you like to get more results? like to see some detail? type 1
