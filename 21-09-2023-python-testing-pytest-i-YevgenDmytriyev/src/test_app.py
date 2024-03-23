import pytest

from app import squared

# TODO: add tests below to be run by pytest.


def test_squared_of_1_is_1():
    
    assert squared(1) == 1


def test_squared_of_10_is_100():
    
    assert squared(10) == 100


def test_squared_of_negative_two_is_not_negative_four():
    
    assert squared(-2) != -4


def test_squared_is_a_function():
    
    assert callable(squared)


def test_squared_of_20_returns_integer():
    
    assert isinstance(squared(20), int)


def test_squared_of_string_raises_type_error():
    
    with pytest.raises(TypeError):
        squared("string")


# dci-student  21-09-2023-python-testing-pytest-i-Lightmaker777  ➜ ( main)  ♥ 14:54  pytest
# ============================================== test session starts ===============================================
# platform linux -- Python 3.11.4, pytest-7.2.1, pluggy-1.0.0+repack
# rootdir: /home/dci-student/21-09-2023-python-testing-pytest-i-Lightmaker777, configfile: pytest.ini
# collected 6 items                                                                                                

# src/test_app.py ......                                                                                     [100%]

# =============================================== 6 passed in 0.02s ================================================
