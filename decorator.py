from enum import Enum, auto
from datetime import datetime


class Role(Enum):
    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"Person: {self.fname} {self.lname}"

    @property
    def fullname(self) -> str:
        return f'{self.fname} {self.lname}'


class Staff(Person):
    def __init__(self, fname: str, lname: str, staff_id: int, role: Role) -> None:
        super().__init__(fname, lname)
        self.staff_id = staff_id
        self.role = role
        self.is_staff: bool = True
        # private member
        self._date_joined = datetime.now()

        match role:
            case Role.ASSOCIATE:
                # strick private memeber
                self.__salary: float = 15
            case Role.SUPERVISOR:
                self.__salary = 20
            case Role.MANAGER:
                self.__salary = 30

    def __str__(self) -> str:
        # return super().__str__()
        return f'Name is: {self.fullname}'


p1 = Person('John', 'Doe')
print(p1)
print(p1.fullname)

employee1 = Staff('Tariqul', 'Islam', 1, Role.MANAGER)
print(employee1)
