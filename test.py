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

        self.assertEqual(1.0, rate)


if __name__ == '__main__':
    unittest.main()
