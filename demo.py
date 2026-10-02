# Carlos Paulino - Week 5 EC - Faker

"""Demo of the Faker Module: Generate fake student data."""
from faker import Faker

fake = Faker()
Faker.seed(42)

print("Five fake students")
for _ in range(5):
  print(fake.first_name(), fake.last_name(), fake.safe_email(), fake.date_of_birth(minimum_age=16, maximum_age=100))

print("Three SQL rows")
for _ in range(3):
  first = fake.first_name().replace("'", "''")
  last = fake.last_name().replace("'", "''")
  print(f"('{first}', '{last}', '{fake.safe_email()}'),")
  
