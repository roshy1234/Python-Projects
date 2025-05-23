import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length: int) -> str:
    combination: str = string.ascii_letters + string.digits + string.punctuation

    combination_length = len(combination)
    new_password: str = ''
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == '__main__':
    for i in range(1,6):
        new_pass: str = generate_password(length=8)
        if contains_symbols(new_pass) and contains_upper(new_pass):
            print(f'{i} -> {new_pass}')
        else:
            i=-1
            continue
