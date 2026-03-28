# complex_sub.py

def format_complex(real, imag):
    """
    Formats complex number into a+bi form string
    """
    if imag >= 0:
        return f"{real}+{imag}j"
    else:
        return f"{real}{imag}j"


def subtract_complex(c1, c2):
    """
    Subtracts two complex numbers (c1 - c2)
    c1, c2 -> tuples (real, imag)
    """
    if not (isinstance(c1, tuple) and isinstance(c2, tuple)):
        raise ValueError("Inputs must be tuples")

    r1, i1 = c1
    r2, i2 = c2

    real = r1 - r2
    imag = i1 - i2

    return format_complex(real, imag)