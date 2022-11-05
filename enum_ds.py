from enum import Enum


class PizzaSize(Enum):
    SMALL = 8
    MEDIUM = 10
    LARGE = 12


choice = PizzaSize.MEDIUM

print(f'One order for {choice.value} inch pizza')
