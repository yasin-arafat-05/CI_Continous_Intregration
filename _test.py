import pytest


# function for test squre:
def squre(n):
    return n**2 


# function for test cuve:
def squre(n):
    return n**3


# function for test five:
def squre(n):
    return n**5


# ====== Testing all the function: ======
def test_squre(n):
    assert squre(2)==4, "Test failed square of 2 should be 4"
    assert squre(3)==9, "Test failed square of 3 should be 9"
    
def test_cuve(n):
    assert squre(2)==8, "Test failed cuve of 2 should be 8"
    assert squre(3)==27, "Test failed cuve of 3 should be 27"
    
def test_fith(n):
    assert squre(2)==32, "Test failed 2^5  of 2 should be 32"
    assert squre(3)==243, "Test failed 3^5 of 3 should be 243"
    
    
# test for invalid input:
def test_invalid_input():
    with pytest.raises(TypeError):
        squre("string")
        