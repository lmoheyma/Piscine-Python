import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate and return a random str with a length
    of 15. Used to generate an id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Dataclass that represents a student.
    A student have a name, a surname, an active status,
    a login and an id which is random.
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """
        A constructor to initialize a student with a login
        as attribute, based on his name and surname
        """
        self.login = self.name[0].capitalize() + self.surname.lower()
