
def binary_add(a: str, b: str) -> str:
    """
    Add two binary numbers.
    e.g. binary_add("B'011", "B'010") -> "B'101"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    return decimal_to_binary(f"D'{da + db}")


def binary_subtract(a: str, b: str) -> str:
    """
    Subtract two binary numbers.
    e.g. binary_subtract("B'101", "B'010") -> "B'011"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    if da < db:
        raise NegativeBinaryResultError()
    return decimal_to_binary(f"D'{da - db}")


def binary_multiply(a: str, b: str) -> str:
    """
    Multiply two binary numbers.
    e.g. binary_multiply("B'011", "B'010") -> "B'110"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    return decimal_to_binary(f"D'{da * db}")


def binary_divide(a: str, b: str) -> str:
    """
    Integer divide two binary numbers.
    e.g. binary_divide("B'110", "B'010") -> "B'11"
    """
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    if db == 0:
        raise ValueError("Binary division by zero")
    return decimal_to_binary(f"D'{da // db}")