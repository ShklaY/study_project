from dataclasses import dataclass
from faker import Faker
import random


@dataclass
class TestData:
    # TODO why do we initialize faker here?
    fake = Faker(locale='uk_UA')
    full_name: str = fake.name()
    email: str = fake.email()
    new_email: str = fake.email()
    current_address: str = fake.address()
    permanent_address: str = fake.address()
    first_name: str = fake.first_name()
    last_name: str = fake.last_name()
    age: int = random.randint(18, 79)
    salary: int = random.randint(1000, 20000)
    list_departments = [
        'Insurance',
        'Compliance',
        'Legal'
    ]
    department: str = list_departments[random.randint(0, 2)]
    phone_number: int = random.randint(9347822912, 9947822913)
    list_subjects = [
        "Hindi",
        "English",
        "Maths",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Commerce",
        "Accounting",
        "Economics",
        "Arts",
        "Social Studies",
        "History",
        "Civics"
    ]
    subject: int = list_subjects[random.randint(0, 13)]


class DataStateAndCity:
    dict_state_city = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
}

    list_states = list(dict_state_city.keys())
    random_state = list_states[random.randint(0, 3)]

    cities_in_the_random_state = dict_state_city[random_state]
    length_of_the_cities_list = len(cities_in_the_random_state)
    random_city = cities_in_the_random_state[random.randint(0, length_of_the_cities_list - 1)]

