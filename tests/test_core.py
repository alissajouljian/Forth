import unittest
from compiler import ForthInterpreter

class TestForth(unittest.TestCase):
    def setUp(self):
        self.forth = ForthInterpreter()

    def test_add(self):
        self.forth.run("2 3 +")
        self.assertEqual(self.forth.stack.pop(), 5)

    def test_define_word(self):
        self.forth.run(": square dup * ;")
        self.forth.run("4 square")
        self.assertEqual(self.forth.stack.pop(), 16)

    def test_stack_ops(self):
        self.forth.run("2 dup *")
        self.assertEqual(self.forth.stack.pop(), 4)

if __name__ == '__main__':
    unittest.main()

