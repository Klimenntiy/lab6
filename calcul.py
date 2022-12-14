def calcul(expression):
    allowed = '+-/*'
    for sign in allowed:
        if sign in expression:
            try:
                a, b = expression.split(sign)
                a, b = int(a), int(b)
                if sign == '+':
                    return a + b
                if sign == '-':
                    return a - b
                if sign == '*':
                    return a * b
                if sign == '/':
                    return a / b
            except(ValueError, TypeError):
                raise ValueError('не корректный ввод')
if __name__ == '__main__':
    calcul('')
