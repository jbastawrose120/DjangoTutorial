import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fakeFName = fakegen.first_name()
        fakeLName = fakegen.last_name()
        fakeEmail = fakegen.email()

        user = User.objects.get_or_create(first_name=fakeFName, last_name=fakeLName, email=fakeEmail)[0]
#TODO Exception handling for duplicate user names (unique constraint collisions)



if __name__ == '__main__':
    print('Populating Script!')
    populate(20)
    print('Populating Complete!')
