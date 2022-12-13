def calcul (expression):
    allowed = '+-/*'
    for sign in allowed:
        if sign in expression:
            left, right = expression.split (sign)
            left, right = int(left), int(right)
            return {
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
                }[sign](left, right)
            

if __name__ == '__main__':
    calcul('')
