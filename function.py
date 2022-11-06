def printLangs(name: str) -> None:
    print(f'This language is : {name}')


def getSubject(name: str) -> str:
    return name


def main() -> None:
    langs: list[str] = ['Python', 'Java', 'Java script', 'ECMA script']

    for lang in langs:
        # printLangs(lang)
        if 'Java' in getSubject(lang):
            print(f'{lang} in the list')
            break
        else:
            print('Java is not in the list')

    print('Thanks for the time')


main()
