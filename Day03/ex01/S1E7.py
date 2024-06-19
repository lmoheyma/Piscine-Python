from S1E9 import Character


class Baratheon(Character):
    """A class Baratheon which inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character, with first_name
        as first parameter and is_alive as second,
        with a default value set to True
        A Baratheon has brown eyes and dark hairs"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


class Lannister(Character):
    """A class Lannister which inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character, with first_name
        as first parameter and is_alive as second,
        with a default value set to True
        A Lannister has blue eyes and light hairs"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Class method to create a Lannister object and return it"""
        return cls(first_name, is_alive)
