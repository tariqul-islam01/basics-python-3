
my_score: int = 34

print(f'my score is {my_score}')

my_score = 54

print(f'my score is {my_score}')

# use plugin mypy

str_group = dict[str, str | int]

MAKBOOK: str_group = {
    "name": "Macbook air",
    "chip": "M1",
    "memory": "16 GB",
    "release": 2020
}

print(MAKBOOK)
