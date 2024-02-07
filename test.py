import unittest

from main import convert


class Test(unittest.TestCase):

    def test_trivial(self):
        rate = convert(
            conversion_rates=[
                ('a', 'b', 2.0),
            ],
            a_to_b=('a', 'a'),
        )

        self.assertEqual(1.0, rate.value)

    def test_feasible1(self):
        rate = convert(
            conversion_rates=[
                ('a', 'b', 10.0),
                ('a', 'c', 5.0),
            ],
            a_to_b=('b', 'c'),
        )

        self.assertEqual(0.5, rate.value)

    def test_feasible2(self):
        rate = convert(
            conversion_rates=[
                ('a', 'b', 10.0),
                ('b', 'c', 5.0),
            ],
            a_to_b=('a', 'c'),
        )

        self.assertEqual(50.0, rate.value)


if __name__ == '__main__':
    unittest.main()
