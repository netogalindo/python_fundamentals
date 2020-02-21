from typing import List


def list_avg(sequence: List) -> float: # It tells Python sequence is a list, and that it'll return a float
    return sum(sequence) / len(sequence)


list_avg(123) # This results in a error, but, after using type hinting, Python highlights this as an error


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

# @classmethod
# def paperback(cls, name: str, page_weight: int) -> "Book":
#     return cls(name, cls.TYPES[1], page_weight)
# This would be a way for me to say the return type would be an object from the Book class (From last class)
# Notice it's written between quotes, because this method is being created before the class has finished processing
# If the method is located in a different class, then the return type would be written without quotes
