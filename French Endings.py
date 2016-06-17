# French Verb Endings
#By:Alfredo Yax

import sys
import re

''' use sys to get user input '''
userInput = ' '.join(sys.argv[1:])

''' use regular expression to parse the input and check if it's the right form '''
search = re.search('(je|tu|il|elle|on|nous|vous|ils|elles) (\w+)(re|er|ir)$', userInput)

''' index numbers representing each person, to be used in suffix list '''
persons = {
    "je": 0,
    "tu": 1,
    "il": 2,
    "elle": 2,
    "on": 2,
    "nous": 3,
    "vous": 4,
    "ils": 5,
    "elles": 5
}

''' suffixes used to generate correct conjugation. '''
suffixes = {
    "re": ["s", "s", " ", "ons", "ez", "ent"],
    "er": ["e", "es", "e", "ons", "ez", "ent"],
    "ir": ["s", "s", "t", "ssons", "ssez", "ssent"]
}

''' parse input components with groups, then print the correct verb conjugation '''
if search:
    person = search.group(1)
    verb = search.group(2)
    ending = search.group(3)
    print(person, verb + suffixes[ending][persons[person]])
else:
    print("Usage: french.py je courir (or any verb with a subject and verb)")
