from Person import Person


class Employee(Person):
    def __init__(self, first, last, pay):
        Person.__init__(self, f'{first} {last}')
        self.pay = pay


    def __str__(self):
        return f'{Person.__str__(self)} | pay: {self.pay}'

