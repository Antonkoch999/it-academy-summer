import unittest

import ddt

from src.Homework6 import eiler


@ddt.ddt
class TestHomework(unittest.TestCase):

    @ddt.data(
        (100, 1752),
        (10, 5),
        (200, 70516)
    )
    @ddt.unpack
    def test_eiler(self, num, expected):
        result = eiler.func(num)
        self.assertEqual(result, expected)

    @ddt.data(
        -10,
        0,
    )
    def test_invalid_input(self, num):
        with self.assertRaises(IndexError):
            eiler.func(num)

    @ddt.data(
        '23',
        [12],
        {'22': 123},
    )
    def test_invalid_eiler(self, num):
        with self.assertRaises(TypeError):
            eiler.func(num)
