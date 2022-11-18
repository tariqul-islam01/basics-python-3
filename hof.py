from typing import Callable


def hello() -> None:
    print('Hello world')


print(hello)
print(id(hello))
print(type(hello))


greet: Callable[[], None] = hello
greet()


def morning(name: str) -> str:
    return f"hello {name} good morning"


def night(name: str) -> str:
    return f"hello {name} good night"


def noon(name: str) -> str:
    return f"hello {name} good noon"


def universal_grreting(name: str, greeting: Callable[[str], str]) -> None:
    msg = greeting(name)
    print(msg)


universal_grreting('Tareq', night)
universal_grreting('Tareq', morning)
universal_grreting('Tareq', noon)


# fn return fn

def add_by_5(num: int) -> Callable[[], int]:
    def by_5() -> int:
        return num + 5

    return by_5


sum = add_by_5(15)

print(sum())


def unique_adder(num1: int) -> Callable[[int], int]:
    def adder(num2: int) -> int:
        return num1 + num2 - 1
    return adder


addr = unique_adder(10)
print(addr(6))
print(addr(20))
