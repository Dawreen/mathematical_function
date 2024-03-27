import pytest
import math

from mathematical_function.Fibonacci import fibonacci
from mathematical_function.Factorial import factorial

def test_exec():
    assert fibonacci.run(0) == 0
    assert fibonacci.run(1) == 1
    assert fibonacci.run(2) == 1
    assert fibonacci.run(3) == 2
    assert fibonacci.run(4) == 3
    assert fibonacci.run(5) == 5
    assert fibonacci.run(6) == 8

    assert fibonacci.run_rec(0) == 0
    assert fibonacci.run_rec(1) == 1
    assert fibonacci.run_rec(2) == 1
    assert fibonacci.run_rec(3) == 2
    assert fibonacci.run_rec(4) == 3
    assert fibonacci.run_rec(5) == 5
    assert fibonacci.run_rec(6) == 8

    assert fibonacci.run_fast(0) == 0
    assert fibonacci.run_fast(1) == 1
    assert fibonacci.run_fast(2) == 1
    assert fibonacci.run_fast(3) == 2
    assert fibonacci.run_fast(4) == 3
    assert fibonacci.run_fast(5) == 5
    assert fibonacci.run_fast(6) == 8

    for n in range(10):
        assert factorial.run_rec(n) == math.factorial(n)
    
    for n in range(10):
        assert factorial.run(n) == math.factorial(n)
