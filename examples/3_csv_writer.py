import csv

from faker import Faker
from faker.providers import internet
from faker.providers.address.ru_RU import Provider as RuAddress
from faker.providers.person.ru_RU import Provider as RuPerson

fake = Faker()
fake.add_provider(internet)
fake.add_provider(RuAddress)
fake.add_provider(RuPerson)

with open('eggs.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    writer.writerow(['id', 'name', 'address', 'ip'])
    for number in range(10):
        writer.writerow([str(number).zfill(5), fake.name(), fake.address(), fake.ipv4_public()])

# TODO: Попробуйте самостоятельно разобрать работу с методом DictWriter
with open('names.csv', 'w', newline='') as csv_file:
    fieldnames = ['id', 'name', 'address']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for number in range(5):
        writer.writerow({'id': str(number).zfill(3), 'name': fake.name(), 'address': fake.address()})
