import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","fullthrottle_labs.settings")
django.setup()

from faker import Faker
from accounts.models import User,ActivityPeriod
import random
import uuid

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]

fakeobj = Faker()
def create_post(N):
    for _ in range(N):
        add_user()

def add_useractivity(u):
    a = ActivityPeriod.objects.create(start_time = fakeobj.date_time_this_year(before_now=True, after_now=False, tzinfo=None),end_time = fakeobj.date_time_this_year(before_now=True, after_now=False, tzinfo=None),user = u)
    a.save()
    return a

def add_user():
    u = User.objects.create(real_id=my_random_string(9),real_name = fakeobj.name(),password = fakeobj.password(length=12),time_zone = fakeobj.timezone())
    u.save()
    for _ in range(random.randint(1,5)):
        add_useractivity(u)

    return u
    
create_post(5)
