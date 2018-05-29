# List the species of each planet

import json, requests, sys
from pprint import pprint

planetUrl = 'https://swapi.co/api/planets/'

def list_planets(url):
    chosen_planet = input('Which planet would you like to know the species of?')
    print('Searching for species on {}'.format(chosen_planet))

    for planet_id in range (1, 61):
        planets_obj = requests.get('{}{}'.format(url, planet_id))
        planets_text = json.loads(planets_obj.text)
        
        if chosen_planet == planets_text['name']:
            #print out the residents
            for resident_id in planets_text['residents']:
                resident_obj = requests.get(resident_id)
                resident_text = json.loads(resident_obj.text)

                for species_id in resident_text['species']:
                    species_obj = requests.get(species_id)
                    species_text = json.loads(species_obj.text)
                    print(species_text['name'])
                    sys.stdout.flush()
            break
 
        sys.stdout.flush()
    

list_planets(planetUrl)