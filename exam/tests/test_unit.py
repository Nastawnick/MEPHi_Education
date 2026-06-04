import unittest

from pathlib import Path
import sys

root = Path(__file__).parent.parent
sys.path.insert(0, str(root))

from src.is_even import is_even

class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        result = is_even(4)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

