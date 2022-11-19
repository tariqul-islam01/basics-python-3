class Animal:
    def __init__(self, name: str, num_of_leg: int, age: int) -> None:
        self.name = name
        self.num_of_leg = num_of_leg
        self.age = age

    def __str__(self) -> str:
        return f'Animal name is {self.name} has {self.num_of_leg} and its {self.age} years old'

    def talk(self, can_speask: bool) -> None:
        if can_speask:
            print(f'{self.name} can speak')
        else:
            print(f'{self.name} can not speak')


a1 = Animal('Sero', 2, 24)
print(a1)
a1.talk(False)


class Human(Animal):
    def __init__(self, name: str, num_of_leg: int, age: int, lang: str) -> None:
        super().__init__(name, num_of_leg, age)
        self.lang = lang
        self.can_speak = True

    def __str__(self) -> str:
        return super().__str__()


h1 = Human('Tariqul', 2, 26, 'Bengali')
print(h1)
h1.talk(True)
