fruits: list[str] = ['apple', 'banana', 'jack fruit', 'mango']

print(fruits)

print(f'Fruits length {len(fruits)}')
for fruit in fruits:
    print(fruit)


removedFruit = fruits.pop()

print(f'removed fruits {removedFruit}')

print(fruits)

fruits.append('avocado')
print(fruits)

fruits.remove('banana')

print(f'fruits after removing banana {fruits}')

fruits.insert(1, 'banana')

print(f'insert banana in index 1 {fruits}')


if 'banana' in fruits:
    print('Yes banana in the list')
else:
    print('No banana is not in the list')

print(f'Before sort: {fruits}')
fruits.sort()
print(f'After sort: {fruits}')

fruits.reverse()
print(f'After reverse: {fruits}')

removed_fruits_by_index = fruits.pop(2)
print(f'Removed index 2 : {removed_fruits_by_index}')
print(fruits)
