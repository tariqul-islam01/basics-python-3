from __future__ import annotations
from enum import Enum, auto
from datetime import datetime
from typing import final


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


# no inheritance possible
@final
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

    @classmethod
    def new(cls, person: Person, staff_id: int, role: Role) -> Staff:
        return cls(person.fname, person.lname, staff_id, role)

    @property
    def joined_date(self) -> str:
        return f"{self._date_joined.strftime('%B %d, %Y')}"

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, amt: float) -> None:
        if self.role == Role.ASSOCIATE and amt < 15:
            print('Error! Associate can not have salary less than $15/hr')
        elif self.role == Role.SUPERVISOR and amt < 20:
            print('Error! Supervisor can not have salary less than $20/hr')
        elif self.role == Role.MANAGER and amt < 25:
            print('Error! Manager can not have salary less than $25/hr')
        else:
            self.__salary = amt
            print(
                f"Staff Details: Name: {self.fullname} has salary ${self.salary}/hr")


p1 = Person('John', 'Doe')
print(p1)
print(p1.fullname)

employee1 = Staff('Tariqul', 'Islam', 1, Role.MANAGER)
print(employee1)

employee2 = Staff.new(p1, 1234, Role.SUPERVISOR)
print(employee2)
print(employee2.joined_date)
print(employee2.salary)
employee2.salary = 25
print(employee2.salary)
