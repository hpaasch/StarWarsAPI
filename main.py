import requests
import sys

def output_results(response, name_title, detail_url):
    for item in response['results']:
        print(item[name_title])
        id = item[detail_url].split('/')
        print(id[5])

def collect_results(response, name_title, detail_url):
    if response['next']:
        while response['next']:
            output_results(response, name_title, detail_url)
            url = response['next']
            response = requests.get(url).json()
    else:
        output_results(response, name_title, detail_url)
    
def call_swapi_data(choice):
    url, name_title, detail_url = swapi_dict[choice]
    response = requests.get(url).json()
    collect_results(response, name_title, detail_url)


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
    call_swapi_data(choice)


    # for key, value in response['results'].items():
    #     print(key, value)

    # more_info = input("Would you like details? Y/n ").lower()
    # if more_info == 'y':
    #     person = input("Type in name or title: ").lower()
    #     print(['results', 'name'])



# would you like to get more results? like to see some detail? type 1
