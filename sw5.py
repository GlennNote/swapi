# Create a function that takes in a homeworld and a starship and returns the people on common
 
import json, requests, sys
from pprint import pprint

peopleUrl = 'https://swapi.co/api/people/'
planetsUrl = 'https://swapi.co/api/planets/'
starships = 'https://swapi.co/api/starships/'

# ask for a starship
chosen_starship = input("Please choose a starship: ")
# ask for a homeworld
chosen_homeworld = input("Please choose a homeworld: ")

def find_common(starship, homeworld, url):
    for person_id in range (1, 87):
        person_obj = requests.get('{}{}'.format(url, person_id))
        person_text = json.loads(person_obj.text)
        try:
            for starship_id in person_text['starships']: 
                    
                starship_obj = requests.get(starship_id)
                starship_text = json.loads(starship_obj.text)

                homeworld_obj = requests.get(person_text['homeworld'])
                homeworld_text = json.loads(homeworld_obj.text)
                
                if starship_text['name'] == starship and homeworld_text['name'] == homeworld:
                    print("* {} has chosen starship and homeworld".format(person_text['name']))
                    break
                else:
                    print("{} does not have these in common.".format(person_text['name']))
                    break

                sys.stdout.flush()
        except:
            pass
        sys.stdout.flush()

find_common(chosen_starship, chosen_homeworld, peopleUrl)
