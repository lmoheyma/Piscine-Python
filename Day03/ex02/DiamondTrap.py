from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class King which inherits from Baratheon
    and Lannister"""
    def __init__(self, first_name):
        """Constructor for King, with first_name
        as first parameter
        A King has brown eyes and dark hairs by default"""
        super().__init__(first_name=first_name, is_alive=True)

    def set_eyes(self, eyes):
        """Setter for eyes attribut"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Setter for hairs attribut"""
        self.hairs = hairs

    def get_eyes(self):
        """Getter for eyes attribut"""
        return self.eyes

    def get_hairs(self):
        """Getter for hairs attribut"""
        return self.hairs
