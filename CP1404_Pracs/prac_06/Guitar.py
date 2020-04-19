""" Guitar class """


CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string representation of a Guitar."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar can be considered vintage based on age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sorting Guitars by their year released."""
        return self.year < other.year
