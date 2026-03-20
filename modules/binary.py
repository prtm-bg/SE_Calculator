# -- Pritam 038 -------------------------------------------------------

from exceptions import InvalidBinaryInputError, NegativeBinaryResultError


def _strip(b: str) -> str:
    """Strip B' prefix and whitespace."""
    b = b.strip().upper()
    if b.startswith("B'"):
        b = b[2:]
    return b


def _validate(b: str) -> None:
    if not b or not all(c in '01' for c in b):
        raise InvalidBinaryInputError(b)


def binary_to_decimal(b: str) -> str:
    """
    Convert binary string to decimal.
    e.g. binary_to_decimal("B'1010") -> "D'10"
    """
    raw = _strip(b)
    _validate(raw)
    return f"D'{int(raw, 2)}"


def decimal_to_binary(d: str) -> str:
    """
    Convert decimal string to binary.
    e.g. decimal_to_binary("D'10") -> "B'1010"
    """
    d = d.strip().upper()
    if d.startswith("D'"):
        d = d[2:]
    n = int(d)
    if n < 0:
        raise ValueError("Negative decimal not supported in basic mode")
    return f"B'{bin(n)[2:]}"

  

# ── Saiyam 037: Arithmetic ──────────────────────────────────────────────────────

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
