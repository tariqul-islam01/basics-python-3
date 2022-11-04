marks: dict[str, int] = {
    'maths': 80,
    'science': 75,
    'physics': 89,
    'biology': 49
}

print(f'Marks: {marks}')

for subject in marks.keys():
    print(subject)

for mark in marks.values():
    print(mark)

for sub, score in marks.items():
    print(f'{sub}: {score}/100')

for sub, score in marks.items():
    if score >= 50:
        print(f'{sub} Passed')
    else:
        print(f'{sub} Failed!!!')

marks['biology'] = 70
print(f'Marks of Biology increased to {marks["biology"]}')

for sub, score in marks.items():
    if score >= 50:
        print(f'{sub} Passed')
    else:
        print(f'{sub} Failed!!!')

bio_score = marks['biology']
print(f'Biology: {bio_score}')

# eng_score = marks['english']
#  throw an error

# print(f'English score is : {eng_score}')

# Better way

eng_score = marks.get('english')  # None

if eng_score is None:
    print('English is not is list')

del marks['biology']
print(f'After deleting subject: {marks}')
