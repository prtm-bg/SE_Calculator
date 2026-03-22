# SE Calculator — Feature 5.6: Binary Number System

Group 6 | Branch: FeatureA_6 | Process: Classical Waterfall

## Project Structure
SE_CALCULATOR/
├── calculator.py         # Base calculator (add, sub, mul, div)
├── test_calculator.py    # Base unit tests
├── modules/
│   ├── __init__.py       # Re-exports public API
│   ├── binary.py         # Binary operations
│   └── exceptions.py     # Custom exceptions
├── tests/
│   ├── __init__.py
│   └── testbinary.py     # Unit tests for binary module
└── .github/workflows/    # CI pipeline

## Features
- Binary ↔ Decimal conversion
- Binary arithmetic (add, sub, mul, div)
- 1's and 2's complement
- Input validation with custom exceptions

## Running Tests
    pytest tests/testbinary.py -v

## Input Format
- Binary: B'1010
- Decimal: D'10