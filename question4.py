class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Make the class iterable
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)

# Iterate over the instance
for attr in rect:
    print(attr)
