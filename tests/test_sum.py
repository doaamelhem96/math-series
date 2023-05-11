import pytest
from Mathematics.series import sum

def test_sum0():
    actual=sum(0)
    expected=0
    assert actual==expected
def test_sum1():
    actual=sum(1)
    expected=1
    assert actual==expected
def test_sum2():
    actual=sum(2)
    expected=1
    assert actual==expected
def test_sum3():
    actual=sum(3)
    expected=2
    assert actual==expected


def test_sum_other0():
    actual = sum(0, 3, 5)
    expected = 3
    assert actual == expected
def test_sum_other1():
    actual = sum(1, 3, 5)
    expected = 5
    assert actual == expected
def test_sum_other2():
    actual = sum(2, 3, 5)
    expected = 8
    assert actual == expected
def test_sum_other3():
    actual = sum(3, 3, 5)
    expected = 13
    assert actual == expected

    # assert sum(0, 3, 4) == 3
    # assert sum_series(1, 3, 4) == 4
    # assert sum_series(2, 3, 4) == 7
    # assert sum_series(3, 3, 4) == 11
    # assert sum_series(4, 3, 4) == 18
    # assert sum_series(5, 3, 4) == 29