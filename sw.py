import json, requests, sys
from pprint import pprint

for i in range(1,87):
    # Person
    person_url = 'https://swapi.co/api/people/{}/'.format(i)
    response = requests.get(person_url)    
    person = json.loads(response.text)

    if "name" in person:
        pprint(person['name'])
        pprint(person['birth_year'])
        pprint(person['gender'])

        # Homeworld
        homeworld_url = '{}'.format(person['homeworld'])
        response_homeworld = requests.get(homeworld_url)
        obj_homeworld = json.loads(response_homeworld.text)
        print('H -\t{}'.format(obj_homeworld["name"]))
        print('   \t{}'.format(obj_homeworld["climate"]))
        print('   \t{}'.format(obj_homeworld["terrain"]))


        # Starship
        if len(person['starships']) > 0:
            for el in person['starships']:        
                starship_url = '{}'.format(el)
                response_starship = requests.get(starship_url)
                obj_starship = json.loads(response_starship.text)
                print('S -\t{}'.format(obj_starship["name"]))
                print('   \t{}'.format(obj_starship["model"]))
                print('   \t{}'.format(obj_starship["manufacturer"]))
        else:
            print('{} has no starships.'.format(person['name']))
            

        # Vehicle
        if len(person['vehicles']) > 0:
            for el in person['vehicles']:        
                vehicle_url = '{}'.format(el)
                response_vehicle = requests.get(vehicle_url)
                obj_vehicle = json.loads(response_vehicle.text)
                print('V -\t{}'.format(obj_vehicle["name"]))
                print('   \t{}'.format(obj_vehicle["model"]))
                print('   \t{}'.format(obj_vehicle["manufacturer"]))
        else:
            print('{} has no vehicles.'.format(person['name']))
            


        print('-------')
    else:
        print('Does not exist.')
    sys.stdout.flush()

