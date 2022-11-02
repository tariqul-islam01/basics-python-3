fav_color = input('Please type your fav color. >>>').lower()

match fav_color:
    case 'green':
        print(f'you got {fav_color} t-shirt')
    case 'red':
        print(f'you got {fav_color} pant')
    case 'black':
        print(f'you got {fav_color} cap')
    case _:
        print(f'Sorry {fav_color} has no gift')
