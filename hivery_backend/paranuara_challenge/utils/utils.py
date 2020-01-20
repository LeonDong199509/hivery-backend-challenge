import json
import os
from paranuara_challenge.models import Person
FRUITS = None
VEGETABLES = None

# read file
with open(os.path.join('paranuara_challenge/utils/','fruits.json')) as f:
    FRUITS = json.load(f)['fruits']

with open(os.path.join('paranuara_challenge/utils/','vegetables.json')) as f:
    VEGETABLES = json.load(f)['vegetables']


def split_fruit_veg(data):
    """split food list to fruit and vegetable
    
    Returns:
        [list] -- [fruits list]
        [list] -- [vegetables list]
    """ 
    if isinstance(data, str):
        data = json.loads(data)      
    fruits = []
    vegs = []
    for i in data:
        if i in FRUITS:
            fruits.append(i)
        elif i in VEGETABLES:
            vegs.append(i)
    return fruits,vegs

def find_common(a,b):
    """find common elements of 2 lists 
    
    Arguments:
        a {[list]} -- [list 1]
        b {[list]} -- [list 2]
    
    Returns:
        [list or None] -- [common elements]
    """    
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return a_set & b_set 
    else: 
        return None
           
def clean_friends(friends):
    """clean friends to a number based list
    
    Arguments:
        friends {[list]} -- [a list whose elements contain json structure]
    
    Returns:
        [list] -- [pure number based list]
    """ 
    if isinstance(friends, str):
        friends = json.loads(friends)    
    if not friends:
        return []
    return list(map(lambda x:x['index'],friends))


def find_friends(friends):
    """find friends have brown eyes and are still alive

    Arguments:
        friends {[list]} -- [a list of friends'index]
    """
    if not friends:
        return []
    condioned_friends = []
    for i in friends:
        person_obj = Person.objects.get(index=i)
        if person_obj.eyeColor=='brown' and person_obj.has_died == False :
            condioned_friends.append(i)
    return condioned_friends
