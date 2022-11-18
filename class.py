class Person:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return '<class "person">'

    def __str__(self) -> str:
        return f" Person: {self.first_name} {self.last_name}"


p1 = Person('Tariqul', 'Islam')
p2 = Person('John', 'Doe')

print(p1)
print(p2)
