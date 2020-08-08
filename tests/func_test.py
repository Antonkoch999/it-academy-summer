import unittest

import ddt

from src.Homework6 import homework4_2


@ddt.ddt
class TestHomework(unittest.TestCase):

    @ddt.data(
        (('Moscow',), ['Moscow - Russia']),
        (('Brest',), ['Brest - Belarus', 'Brest - France']),
        (('Kiev',), ['Kiev - Ukraine']),
        (('Kiev', 'Minsk'), ['Kiev - Ukraine', 'Minsk - Belarus']),
        ((12312, '12312'), []),
        (['Moscow', 'Kiev'], ['Moscow - Russia', 'Kiev - Ukraine']),
        ({'Moscow': '123', 'Kiev': 'sada'}, ['Moscow - Russia',
                                             'Kiev - Ukraine']),
    )
    @ddt.unpack
    def test_cities(self, args, expected):
        self.assertEqual(homework4_2.cities(args), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            homework4_2.cities(4312)
