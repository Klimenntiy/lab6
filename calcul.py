def calcul (expression):
    allowed = '+-/*'
    if not any (sign in expression for sign in allowed):
        raise ValueError('Должен быть хотя бы один знак')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split (sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError ('2 целых числа')

if __name__ == '__main__':
    calcul('')
