from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    country: str

    def __str__(self):
        return f"{self.street} {self.city} {self.country}"


@dataclass
class Person:
    name: str
    address: Address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


if __name__ == "__main__":
    jan = Person("Jan", Address("Budryka 4", "Cracow", "Poland"))
    adam = deepcopy(jan)

    adam.name = "Adam"
    adam.address.street = "Budryka 2"

    print(jan)
    print(adam)
