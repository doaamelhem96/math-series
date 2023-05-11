import pytest  #to use pytest dependencies
from Mathematics.series import fibonacci , sum

# to write a test by function as:
''' 
test_fibonacci
n=0 ==>fibonacci (0)=0
n=1 ==>fibonacci (1) =1
n=2 ==>fibonacci (2) =1
n=3 ==>fibonacci (3) =2

'''
def test_fibonacci0():
    actual=fibonacci (0)
    expected=1
    assert actual==expected
def test_fibonacci1():
    actual=fibonacci (1)
    expected=1
    assert actual==expected
def test_fibonacci2():
    actual=fibonacci (2)
    expected=2
    assert actual==expected

def test_fibonacci3():
     actual=fibonacci (3)
     expected=3
     assert actual==expected
def test_fibonacci4():
    actual=fibonacci (4)
    expected=5
    assert actual==expected

def test_sum_fibonacci0():
    actual=sum (0)
    expected=0
    assert actual==expected
def test_sum_fibonacci1():
    actual=sum (1)
    expected=1
    assert actual==expected
def test_sum_fibonacci2():
    actual=sum (2)
    expected=1
    assert actual==expected
def test_sum_fibonacci3():
    actual=sum (3)
    expected=2
    assert actual==expected
def test_sum_fibonacci4():
    actual=sum (4)
    expected=3
    assert actual==expected

    # assert sum(0) == 0
    # assert sum(1) == 1
    # assert sum(2) == 1
    # assert sum(3) == 2
    # assert sum(4) == 3
    # assert sum(5) == 5

# def test_fibonacci():
#     assert fibonacci(-1) == "error"
#     # assert fibbonachi(0) == 1
#     # assert fibbonachi(1) == 1
#     # assert fibbonachi(2) == 2
#     # assert fibbonachi(3) == 3
#     # assert fibbonachi(4) == 5
    
     


# def test_fibonacci():
#     """
#     Test that the fibonacci function returns the correct values for different inputs.
#     """
#     assert fibonacci(0) == 0
#     assert fibonacci(1) == 1
#     assert fibonacci(2) == 1
#     assert fibonacci(3) == 2
