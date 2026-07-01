class AgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age >= 18:
        return True
    else:
        raise AgeError(f'INVALID AGE {age}')


try:
    userage = int(input('ENTER YOUR AGE - '))
    valid_age = check_age(userage)
    print(valid_age)
except AgeError:
    print('ERROR - INVALID AGE')
