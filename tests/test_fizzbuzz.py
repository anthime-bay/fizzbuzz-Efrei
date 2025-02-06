# Test cases for fizzbuzz function

import sys
import unittest
from io import StringIO

import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("input,expected", [
    (1, "1"), (3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"),
    (30, "FizzBuzz"), (99, "Fizz"), (100, "Buzz")
])
def test_fizzbuzz(input, expected):
    assert fizzbuzz(input) == expected