import unittest
import task
import os

class TestCase(unittest.TestCase):

    def setUp(self):
        self.filename = "temp_file"
        file = open(self.filename, "w")
        file.write("Hello World")
        file.close()

    def tearDown(self):
        os.remove(self.filename)

    def test1(self):
        expected = "Hello"
        self.assertEqual(task.read_first_five(self.filename),expected)

if __name__ == '__main__':
    unittest.main()
