# Show all female pilots

import json, requests, sys
from pprint import pprint

peopleUrl = 'https://swapi.co/api/people/'

# Check how many people there are
def count_people(url):
    people = requests.get(url)
    people_text = json.loads(people.text)
    counter = people_text['count']
    return counter

# Check who is female
def check_for_female_pilots():    
   for person_id in range(33, count_people(peopleUrl) + 1):
        try:
            person_obj = requests.get('{}{}'.format(peopleUrl,person_id))
            person_text = json.loads(person_obj.text)
            
            if person_text['gender'] == 'female':    
                
                print('{}\t{}\t{}'.format(person_id, person_text['name'].encode(), person_text['starships']))
                sys.stdout.flush()

        except:
            print('{}\tdoes not exist.'.format(person_id))


check_for_female_pilots()   
# Check if these females have a starship