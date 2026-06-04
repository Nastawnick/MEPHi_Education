from pathlib import Path
import sys

root = Path(__file__).parent.parent
sys.path.insert(0, str(root))

from src.is_even import is_even

def test_py():
    assert is_even(4)