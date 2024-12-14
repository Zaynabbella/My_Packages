"""
Advanced mathematical operations module.
"""

import math

def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent."""
    return math.pow(base, exponent)

def square_root(x: float) -> float:
    """Calculate the square root of a number."""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)