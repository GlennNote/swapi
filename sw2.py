# Give out the names of people who fly X-wing fighters

import json, requests, sys
from pprint import pprint

peopleUrl = 'https://swapi.co/api/people/'
starshipsUrl = 'https://swapi.co/api/starships/'

# Check how many people are in the list
def check_length(url):
    counter = requests.get(url)
    counter_text = json.loads(counter.text)
    items_in_list = counter_text['count'] + 1
    return items_in_list



# Get a list of everyone who has a starship
def show_pilots():
        items_in_list = check_length(peopleUrl)

        for i in range(1, items_in_list):
            person_obj = requests.get('{}{}'.format(peopleUrl, i))
            person_text = json.loads(person_obj.text)
            
            # Get the names of each of their starships if they have one
            try:
                person_starships = person_text['starships']
                if len(person_starships) > 0:
                    for el in person_starships:
                        starship_obj = requests.get('{}'.format(el))
                        starship_text = json.loads(starship_obj.text)
                        if starship_text['name'] == 'X-wing':
                            print(person_text['name'])
                        sys.stdout.flush()    
                else:
                    pass
                sys.stdout.flush()
            except:
                pass

show_pilots()
   



