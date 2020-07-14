from dataclasses import dataclass
from functools import wraps


@dataclass
class Person:
    street_address: str = None
    postcode: str = None
    city: str = None
    company_name: str = None
    position: str = None
    annual_income: int = None

    def __str__(self):
        return ", ".join(str(value) for _, value in vars(self).items())


class PersonBuilder:
    def __init__(self, person: Person = Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


def fluent(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self

    return wrapper


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    @fluent
    def at(self, company_name: str):
        self.person.company_name = company_name

    @fluent
    def as_a(self, position: str):
        self.person.position = position

    @fluent
    def earns(self, amount: int):
        self.person.annual_income = amount


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person):
        super().__init__(person)

    @fluent
    def at(self, street_address: str):
        self.person.street_address = street_address

    @fluent
    def with_postcode(self, postcode: str):
        self.person.postcode = postcode

    @fluent
    def in_city(self, city: str):
        self.person.city = city


if __name__ == "__main__":
    pb = PersonBuilder()
    person = (
        pb.lives.at("Test Street")
        .in_city("Test City")
        .with_postcode("123-32")
        .works.at("Test Company")
        .as_a("Test Worker")
        .earns(3210000)
        .build()
    )

    print(person)
