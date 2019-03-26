"""
Advanced Testing

# TASK 1

Can you get the commeted out tests passing?
"""

import unittest

csv_filename = "my_csv_file.csv"
number_files = 3

def my_name_is(name):
    print('hello my name is ', name)


class TheWorldIsSaneTestCase(unittest.TestCase):

    def test_world_is_sane(self):
        self.assertEqual(1 + 1, 2)

    def test_world_is_still_sane(self):
        self.assertNotEqual(1 + 2, 2)

    # TODO - Fix me
    # def test_world_is_not_perfectly_sane(self):
    #     self.assertEqual(1 + 4, 3)

class StarterTestCase(unittest.TestCase):

    def test_assert_types(self):
        self.assertIsInstance(csv_filename, str)
        # TODO - Fix me
        # self.assertIsInstance(number_files, float)

    def test_callables(self):
        # Task -  what is a callable type in python?
        self.assertTrue(callable(my_name_is))


if __name__ == '__main__':
    unittest.main()