class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'


if __name__ == '__main__':
    p1 = Person("Sahil")
    print(p1)
