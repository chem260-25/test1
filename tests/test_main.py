import sys
import pytest
from add_nums import add_numbers

def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5, "Failed on positive numbers"

def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5, "Failed on negative numbers"

def test_add_mixed_numbers():
    assert add_numbers(-2, 3) == 1, "Failed on mixed numbers"

def test_add_zeros():
    assert add_numbers(0, 0) == 0, "Failed on zeros"

