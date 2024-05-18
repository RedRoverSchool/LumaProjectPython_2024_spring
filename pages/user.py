from dataclasses import dataclass


@dataclass
class Person:
    user_email: str = None
    first_name: str = None
    last_name: str = None
    street_address: str = None
    city: str = None
    postcode: str = None
    phone_number: str = None