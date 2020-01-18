import math
import sys
from os import rename

import requests

name = input('Your name ?')
print("Hello,", name)

#print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "Test"
    greeeting = 'Hello, {}'.format(who_to_greet)
    return greeeting

print(greet('World'))
print(greet('Corey'))


#r = requests.get('http://coretms.com')
#print(r.status_code)
