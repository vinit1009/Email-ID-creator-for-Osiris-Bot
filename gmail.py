from __future__ import unicode_literals
from __future__ import print_function
from os.path import abspath, join, dirname
import random


    
    
full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())




destination = open('email.txt', 'w')
destination1 = open('fname.txt', 'w')
destination2 = open('lname.txt', 'w')

n = int(input("enter the number of email id:"))

for x in range(n):
    rand = random.randint(10000, 999999)

    first_name = get_first_name()
    last_name = get_last_name()
    username = first_name+last_name+str(rand)


    print(username, file = destination)
    print(first_name, file = destination1)
    print(last_name, file = destination2)


destination.close()
destination1.close()
destination2.close()
