import pytest
from Mathematics.series import lucas, sum

def test_lucas0():
    actual=lucas (0)
    expected=2
    assert actual==expected

def test_lucas1():
    actual=lucas (1)
    expected=1
    assert actual==expected

def test_lucas2():
    actual=lucas (2)
    expected=3
    assert actual==expected

def test_lucas3():
    actual=lucas (3)
    expected=4
    assert actual==expected
def test_lucas4():
    actual=lucas (4)
    expected=7
    assert actual==expected
def test_sum_lucs0():
    actual=sum (0, 2, 1)
    expected=2
    assert actual==expected
def test_sum_lucs1():
    actual=sum (1, 2, 1)
    expected=1
    assert actual==expected
def test_sum_lucs2():
    actual=sum (2, 2, 1)
    expected=3
    assert actual==expected
def test_sum_lucs3():
    actual=sum (3, 2, 1)
    expected=4
    assert actual==expected