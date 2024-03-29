from dataclasses import dataclass


@dataclass
class UserModel:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    new_email: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    salary: int = None
    department: str = None
    phone_number: int = None
    subject: int = None
    state: str = None
    city: str = None


