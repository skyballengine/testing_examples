import unittest
import task_2
import os


class TestCaseOther(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filename = "temp_file"
        file = open(cls.filename, "w")
        file.write("Hello World")
        file.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.filename)

    def test1(self):
        expected = "Hello"
        self.assertEqual(task_2.read_first_five(self.filename),expected)

    def test2(self):
        expected = "World"
        self.assertNotEqual(task_2.read_first_five(self.filename),expected)


if __name__ == '__main__':
    unittest.main()
