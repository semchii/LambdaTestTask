from unittest import TestCase, main
from dots import dots


class DotsTest(TestCase):
    def setUp(self):
        self.cases = [
            ("abcd", ['abcd', 'abc.d', 'ab.cd', 'ab.c.d', 'a.bcd', 'a.bc.d', 'a.b.cd', 'a.b.c.d']),
            ("abc", ['abc', 'ab.c', 'a.bc', 'a.b.c']),
            ("ab", ['ab', 'a.b']), ("", [])
        ]

    def test_normal_behavior(self):
        for expected_value, input_value in self.cases:
            self.assertTrue(dots(input_value), expected_value)


if __name__ == '__main__':
    main()

