from typing import Any

fname, lname = ('Tariqul', 'Islam')

print(fname)
print(lname)

first_fruit, *rest_fruit = ['banana', 'apple', 'avocado']

print(first_fruit)
print(rest_fruit)

# unpack dict

specs = {
    'ram': '16 GB',
    'rom': '128 GB',
    'chip': 'M1',
    'cpu': '8 core',
    'gpu': '8 core'
}

macbook = {'type': 'macbook air', **specs}

print(macbook)


def print_macbook(*arg: str) -> None:
    # by default arg in tuple
    for macbook in arg:
        print(macbook)


print_macbook('macbook air 2020', 'macbook pro M1', 'iMac 2022')


def unknown_prod(**kwarg: Any) -> None:
    for key, value in kwarg.items():
        print(f'{key}:{value}')


unknown_prod(name='macbook air', release='2020', chip='M1')
unknown_prod(name='macbook pro', release='2022', chip='M2')
