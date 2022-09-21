import numbers
import pytest 

from average_calculator.calc import rounded_average


def test_average_of_two_numbers_is_properly_computed():
    actual = rounded_average([4, 6])

    assert actual == 5
    # Delete the skip and write the proper assertion here!


def test_average_of_empty_list_raises_ValueError():
    numbers = rounded_average([])


    pytest.raises(ValueError)

