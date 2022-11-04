langs: tuple[str, str, str] = ('Bengali', 'english', 'spanish')


print(langs)
print(f'Total languages: {len(langs)}')

for lang in langs:
    print(lang)

print(f'second lang is {langs[1]}')

additional_langs = ('hindi', 'marathi')
total_langs = langs + additional_langs
print(f'All langs are : {total_langs}')

if 'marathi' in total_langs:
    print('Marati is in the list')
else:
    print('Marathi is not in the list')
