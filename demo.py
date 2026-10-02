# Carlos Paulino - Week 5 EC - Faker

"""Demo of the Faker Module: Generate fake student data."""
from faker import Faker

fake = Faker()

Faker.seed(42)

SEXES = ["Male", "Female"]

ETHNICITIES = ["White", "Black or African American", "Hispanic or Latino",
               "Asian", "Middle Eastern or North African"]

def make_student():
    """Return one fake student as a dictionary."""
    sex = fake.random_element(SEXES)
    if sex == "Male":
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()
    return {
        "first_name": first_name,
        "last_name": fake.last_name(),
        "email": fake.safe_email(),
        "sex": sex,
        "race_ethnicity": fake.random_element(ETHNICITIES),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=60),
    }

print("Five fake students")
for _ in range(5):
  student = make_student()
  print(student["first_name"], student["last_name"], student["email"], student["birth_date"], student["sex"], student["race_ethnicity"])

print("Three SQL rows")
for _ in range(3):
  student = make_student()
  first = student["first_name"].replace("'", "''")
  last = student["last_name"].replace("'", "''")
  print(f"('{first}', '{last}', '{student['email']}', '{student['race_ethnicity']}', '{student['sex']}'),")
