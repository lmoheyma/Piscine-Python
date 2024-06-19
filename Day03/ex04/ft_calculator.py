class calculator:
    """A class calculator that is able
    to do calculations  (dot product, addition, subtraction)
    of 2 vectors."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Takes 2 lists in arguments, calculate the product
        between each element of the list V1 and V2,
        then return the sum of each result"""
        dotProduct = [V1[i] * V2[i] for i in range(len(V2))]
        print(f"Dot product is: {sum(dotProduct)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Takes 2 lists in arguments, and returns a list that
        contains the sum of each elements in V1 and V2"""
        addVec = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is: {addVec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Takes 2 lists in arguments, and returns a list that
        contains the sunstraction of each elements in V1 and V2"""
        subVec = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {subVec}")
