import requests

swapi_dict = {
  1: ["http://swapi.co/api/people/", "name"],
  # 2: "http://swapi.co/api/planets/",
  2: ["http://swapi.co/api/films/", "title"],
  # 4: "http://swapi.co/api/species/",
  3: ["http://swapi.co/api/vehicles/", "name"],
  # 6: "http://swapi.co/api/starships/",
}
while True:
    overall_choice = int(input("""
    1 Characters
    2 Films
    3 Vehicles
    0 Exit
    """))

    if overall_choice == 1:
        url, look_up = swapi_dict[overall_choice]
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
        more_info = input("Would you like details on a character? Y/n ").lower()
        if more_info == 'y':
            person = input("Type in the character's name: ").lower()
            print(response['name'])

    if overall_choice == 2:
        url, look_up = swapi_dict[overall_choice]
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

    if overall_choice == 3:
        url, look_up = swapi_dict[overall_choice]
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

    if overall_choice == 0:
        break





# would you like to get more results? like to see some detail? type 1
