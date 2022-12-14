import calculator

class Tests:
    def test plus (self):
        output = calculator. calculate("8 + 4")
        assert output == 11
    def test minus (self):
        output = calculator. calculate("8 - 4")
        assert output == 4
    def test_ multiply(self):
        output = calculator. calculate("8 * 4")
        assert output == 32
    def test divide(self):
        output = calculator. calculate("8 / 4")
        assert output == 2
