import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

def test_calculate_subtract():
    assert calculate(3, 2, '-') == 1

def test_calculate_multiply():
    assert calculate(4, 5, '*') == 20