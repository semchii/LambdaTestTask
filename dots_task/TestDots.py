from unittest import TestCase, main
from dots import dots


class DotsTest(TestCase):
    def setUp(self):
        self.cases = [
            ("abcd", ['abcd', 'a.bcd', 'ab.cd', 'a.b.cd', 'abc.d', 'a.bc.d', 'ab.c.d', 'a.b.c.d']),
            ("abc", ['abc', 'a.bc', 'ab.c', 'a.b.c']),
            ("ab", ['ab', 'a.b']), ("", [])
        ]

    def test_normal_behavior(self):
        for expected_value, input_value in self.cases:
            self.assertTrue(dots(input_value), expected_value)


if __name__ == '__main__':
    main()

