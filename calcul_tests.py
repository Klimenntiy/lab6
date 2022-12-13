from unittest import TestCase, main
from teach.calculator import calcul


class CalculT(TestCase):
    def test_plus(self):
        self.assertEqual(calcul('2 + 2'), 4)

    def test_minus(self):
        self.assertEqual(calcul('20 - 14'), 6)

    def test_multi(self):
        self.assertEqual(calcul('24 * 2'), 48)

    def test_divide(self):
        self.assertEqual(calcul('50 / 4'), 12.5)

    def test_no_signal(self):
        with self.assertRaises(ValueError) as e:
            calcul('meowmeow')
        self.assertEqual('Должен быть хотя бы один знак', e.exception.args[0])

    def test_no_signal2(self):
        with self.assertRaises(ValueError) as e:
            calcul('2.0+2.0-5.0')
        self.assertEqual('2 целых числа', e.exception.args[0])

    def test_no_signal3(self):
        with self.assertRaises(ValueError) as e:
            calcul('2+25-2')
        self.assertEqual('2 целых числа', e.exception.args[0])

    def test_no_signal4(self):
        with self.assertRaises(ValueError) as e:
            calcul('a+b')
        self.assertEqual('2 целых числа', e.exception.args[0])


if __name__ == '__main__':
    main()
