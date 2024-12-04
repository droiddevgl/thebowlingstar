import pytest
from numpy.ma.core import product

# multiply two positive integers
# test identity by multiplying any number by one
# test the zero property by multiplying any number by zero
# multiply a positive by a negative
# test negative numbers multiplied by negative numbers
# also multiply floating point numbers instead of integers

# all 3 functions below violates the dry (dont repeat yourself)
# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6
#
# def test_multiply_identity():
#     assert 1 * 99 == 99
#
# def test_multiply_zero():
#     assert 0 * 100 == 100
#
#
# def test_one_plus_one():
#     assert 1 + 1 == 2

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

# we use this to pass the parametrized values into the test function
# it uses the british english spelling, so its parametrized. not the
# american english spelling parameterized
# this is a decorator

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product

# def test_one_plus_one():
#     assert 1 + 1 == 2


#
# def test_one_plus_two():
#     a = 1
#     b = 2
#     c = 3
#     assert a + b == c
#
#
# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError) as e:
#         num = 1 / 0
#
#     assert 'division by zero' in str(e.value)