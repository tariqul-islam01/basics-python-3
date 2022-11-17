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
