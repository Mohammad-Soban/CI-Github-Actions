import pytest

def square(n):
    return n ** 2

def square_root(n):
    return n ** 0.5

def cube(n):
    return n ** 3


# Testing the functions
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"
    assert square(4) == 16, "Test Failed: Square of 4 should be 16"

def test_square_root():
    assert square_root(4) == 2, "Test Failed: Square root of 4 should be 2"
    assert square_root(9) == 3, "Test Failed: Square root of 9 should be 3"
    assert square_root(16) == 4, "Test Failed: Square root of 16 should be 4"


def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"
    assert cube(4) == 64, "Test Failed: Cube of 4 should be 64"


# Test for the invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        square("string")
    with pytest.raises(TypeError):
        square_root("string")
    with pytest.raises(TypeError):
        cube("string")