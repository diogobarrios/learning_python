import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):  # inherits from unittest.TestCase class
    """Tests for 'name_function.py'."""  # so python knows how to run the tests you write.

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')  # assert method (more below)*

    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Anadeus Mozart' works?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
if __name__ == '__main__':
    unittest.main(  )

# *assert methods verify that a result you received mathces the result you expect to receive, so in
# this example above, we want to see if formatted_name will ouput what we expect like 'Janis Joplin'
# capitalize first letters in both words and with a space between them.

