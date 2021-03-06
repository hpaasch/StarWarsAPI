import requests
import sys

def output_results(response, name_title, detail_url):
    for item in response['results']:
        id = item[detail_url].split('/')
        print(id[5], item[name_title])

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
    more_info = input("Do you want details? Y/n ")
    if more_info == 'y':
        detail_id = int(input("Enter number for details: "))
        new_url = url + str(detail_id)
        response = requests.get(new_url).json()
        if url == "http://swapi.co/api/films/":
            print("\n***** FILM DETAILS *****")
            print('Title:', response['title'])
            print('Release date:', response['release_date'])
            print('Director:', response['director'])
            print("\n***** Opening crawl *****")
            print(response['opening_crawl'])
            print("\n***** Characters *****")
            for item in response['characters']:
                print(item)
            print("\n***** Vehicles *****")
            for item in response['vehicles']:
                print(item)
        elif url == "http://swapi.co/api/people/":
            print("\n***** CHARACTER DETAILS *****")
            for key, value in response.items():
                print('\n', key, ':', value)
        elif url == "http://swapi.co/api/vehicles/":
            print("\n***** VEHICLE DETAILS *****")
            for key, value in response.items():
                print('\n', key, ':', value)


swapi_dict = {
  1: ["http://swapi.co/api/people/", "name", "url"],
  2: ["http://swapi.co/api/films/", "title", "url"],
  3: ["http://swapi.co/api/vehicles/", "name", "url"],
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
