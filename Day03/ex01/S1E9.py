from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract class Character which inherits from ABC
    (Abstract Class)"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character, with first_name
        as first parameter and is_alive as second,
        with a default value set to True"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set is_alive to False when Character dies"""
        self.is_alive = False

    def __str__(self):
        """Overload the __str__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Overload the __repr__ method"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Stark(Character):
    """A class Stark which inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for Character, with first_name
        as first parameter and is_alive as second,
        with a default value set to True"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set is_alive to False when Character dies"""
        self.is_alive = False
