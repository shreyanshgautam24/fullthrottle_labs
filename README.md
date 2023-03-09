Populate databse with some dummydata:
Api URL: /api/fullthrottle_test/
I needed some dummy data automatically loaded in the database to work on this part and I need to refresh the data every few days or so.

It would be too much work to do this manually so I wrote a simple script that would be ran as management command in Django. Using management commands is a good way to run the scripts that depend on the Django ORM and other Django features as the settings and paths will already be set for you.

To do this, all you have to do is a create a management.commands package in your application package and place your Python script there. For example, I have a script called populate_script.py, so I’d put it here in my project folder inside fullthrottle_labs.

To populate the DataBase i Have used Faker Package:

Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.

Faker is heavily inspired by PHP Faker, Perl Faker, and by Ruby Faker.
Install with pip:

pip install Faker
Note: this package was previously called fake-factory.

Use faker.Faker() to create and initialize a faker generator, which can generate data by accessing properties named after the type of data you want.

from faker import Faker
fake = Faker()

fake.name()
# 'Lucy Cechtelar'

Each call to method fake.name() yields a different (random) result. This is because faker forwards faker.Generator.method_name() calls to faker.Generator.format(method_name).

for _ in range(10):
  print(fake.name())

# 'Adaline Reichel'
# 'Dr. Santa Prosacco DVM'
# 'Noemy Vandervort V'
# 'Lexi O'Conner'
# 'Gracie Weber'
# 'Roscoe Johns'
# 'Emmett Lebsack'
# 'Keegan Thiel'
# 'Wellington Koelpin II'

