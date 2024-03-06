class FaledNameError(Exception):
    pass
class FaledGameError(Exception):
    pass

def name(name1):
    try:
        raise FaledNameError('Name is not found')
    except FaledNameError as e:
        print(f'Ошибка: {e}')
        raise FaledGameError('Theres already such a game.')


name(name1= 1)

