import unittest
from unittest.mock import Mock

# Mock file reader to control its behavior
open = Mock()

def load_file():
    # Does absolutely nothing other than raise the desired exception
    content = open('temp_file.txt')
    if content.length != 0:
        return content
    return None

class TestCase(unittest.TestCase):
    def test_read_file(self):
        # Test for IOError
        open.side_effect = IOError
        # This is a context manager that allows us to test for exceptions
        with self.assertRaises(IOError):
            load_file()

if __name__ == '__main__':
    unittest.main()