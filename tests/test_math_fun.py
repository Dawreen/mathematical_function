import pytest
from mathematical_function import MathFun

def test_exec():
    res = MathFun.exec(3)
    assert res == 3
