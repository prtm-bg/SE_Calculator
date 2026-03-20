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