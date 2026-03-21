# complex.py
from calculator import Calculator
import re
import cmath

def _format_complex(c):
    """
    Helper function to format a Python complex object back into a 
    clean 'a+bj' string without parentheses to match lab requirements.
    """
    res = str(c).replace(' ', '')
    if res.startswith('(') and res.endswith(')'):
        res = res[1:-1]
    return res

def parse_complex_string(expression):
    """
    Parses an input string like '(3+2j) * (5+3j)'.
    Extracts the two complex numbers and the mathematical operator.
    """
    # Regex to capture everything inside the parentheses and the operator between them
    pattern = r'\s*\(([^)]+)\)\s*([+\-*/])\s*\(([^)]+)\)\s*'
    match = re.match(pattern, expression)
    
    if not match:
        raise ValueError("Invalid complex expression format. Expected: '(a+bj) op (c+dj)'")
    
    c1_str, operator, c2_str = match.groups()
    
    # Remove any internal spaces (e.g., '3 + 2j' becomes '3+2j')
    return c1_str.replace(' ', ''), operator, c2_str.replace(' ', '')

def add_complex(c1, c2):
    """
    Member 2: Handles the addition of two complex numbers[cite: 120].
    """
    pass 

def subtract_complex(c1, c2):
    """
    Member 2: Handles the subtraction of c2 from c1[cite: 120].
    """
    pass

def multiply_complex(c1, c2):
    """
    Member 3: Handles the multiplication of two complex numbers[cite: 120].
    """
    
    calc = Calculator()
    
    # 1. Convert the incoming strings to Python complex objects
    c1 = complex(c1_str)
    c2 = complex(c2_str)
    
    a, b = c1.real, c1.imag
    c, d = c2.real, c2.imag
    
    # (a+bi)*(c+di) = (ac - bd) + (ad + bc)i
    real_part = calc.subtract(calc.multiply(a, c), calc.multiply(b, d))
    imag_part = calc.add(calc.multiply(a, d), calc.multiply(b, c))
    
    # 4. Reconstruct into a complex object and format back to a string
    result = complex(real_part, imag_part)
    return _format_complex(result)

def divide_complex(c1, c2):
    """
    Member 3: Handles the division of c1 by c2[cite: 120].
    Must include error handling for division by zero.
    """
    # c1 and c2 are tuples: (real, imag)
    calc = Calculator()
    
    # 1. Convert the incoming strings to Python complex objects
    c1 = complex(c1_str)
    c2 = complex(c2_str)
    
    a, b = c1.real, c1.imag
    c, d = c2.real, c2.imag
    
    # denominator = c^2 + d^2
    denominator = calc.add(calc.multiply(c, c), calc.multiply(d, d))
    if denominator == 0:
        raise ValueError("Division by zero in complex division")
    # real part: (ac + bd) / (c^2 + d^2)
    real_num = calc.add(calc.multiply(a, c), calc.multiply(b, d))
    real_part = calc.divide(real_num, denominator)
    # imag part: (bc - ad) / (c^2 + d^2)
    imag_num = calc.subtract(calc.multiply(b, c), calc.multiply(a, d))
    imag_part = calc.divide(imag_num, denominator)
    
    result = complex(real_part, imag_part)
    return _format_complex(result)

def compute_magnitude(c):
    """
    Member 4: Calculates the magnitude of a single complex number[cite: 122].
    """
    pass

def compute_phase(c):
    """
    Member 4: Calculates the phase (angle) of a single complex number[cite: 122].
    """
    pass

def evaluate_complex_expression(expression):
    """
    Member 5 (Integrator): The main runner function. 
    Takes the raw string, passes it to parse_complex_string, 
    routes the parsed data to the correct math function above, 
    and returns the final string result.
    """
    