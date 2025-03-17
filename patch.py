import unittest
from unittest.mock import patch
from load_file import load_file


class TestCase(unittest.TestCase):
    # Patch decorator with location of object to mock
    @patch('load_file.open')
    # Note the second argument, mock_open which is passed from patch
    def test_load(self,mock_open):
        # Test for IOError
        mock_open.side_effect = IOError
        # This is a context manager that allows us to test for exceptions
        with self.assertRaises(IOError):
            load_file()


if __name__ == '__main__':
    unittest.main()
