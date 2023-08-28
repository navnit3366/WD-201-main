class Person:
    _name = "Person"  # This is a protected member

    def __init__(self, name):
        self._name = name

    def greet(self):
        print("Hello, my name is " + self._name)


john = Person("John")
john._name = (
    "Jane"  # Creates a new attribute but does not edit the existing _name attribute
)
john.greet()  # Hello, my name is John
