def printLangs(name: str) -> None:
    print(f'This language is : {name}')


def main() -> None:
    langs: list[str] = ['Python', 'Java', 'Java script', 'ECMA script']

    for lang in langs:
        printLangs(lang)
    print('Thanks for the time')


main()
