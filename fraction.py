from fractions import Fraction

class FractionCalculator:

    def calculate(self, expression: str):
        """
        Takes input like '4/5+3/5' or '4/5 + 3/5'
        Returns simplified fraction result
        """

        expression = expression.replace(" ", "")

        # detect operator
        if '+' in expression:
            a, b = expression.split('+')
            return self._operate(a, b, '+')

        elif '-' in expression:
            a, b = expression.split('-')
            return self._operate(a, b, '-')

        elif '*' in expression:
            a, b = expression.split('*')
            return self._operate(a, b, '*')

        elif '/' in expression:
            # careful: division operator between fractions
            parts = expression.split('/')
            if len(parts) == 4:
                a = parts[0] + "/" + parts[1]
                b = parts[2] + "/" + parts[3]
                return self._operate(a, b, '/')

        raise ValueError("Invalid expression")

    def _operate(self, a, b, operator):
        try:
            f1 = Fraction(a)
            f2 = Fraction(b)
        except ZeroDivisionError:
            raise ValueError("Invalid fraction (zero denominator)")

        if operator == '+':
            result = f1 + f2
        elif operator == '-':
            result = f1 - f2
        elif operator == '*':
            result = f1 * f2
        elif operator == '/':
            if f2 == 0:
                raise ValueError("Division by zero fraction")
            result = f1 / f2

        return f"{result.numerator}/{result.denominator}"