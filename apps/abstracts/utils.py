import random


def generate_string() -> str:
    simbols: str = (
        'qwertyuiop'
        'asdfghjkl'
        'zxcvbnm'
        '1234567890'
        '!@#$%*+'
    )
    code: str = ''
    _: int
    for _ in range(20):
        code += random.choice(simbols)

    return code