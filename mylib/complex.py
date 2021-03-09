from .exceptions import MismatchingExponentError, InvalidExpression

class ComplexNumber:
    
    def __init__(self, val=0.0, exp=0):
        if exp > 2:
            raise InvalidExpression(f"This solver can only solve quadratic equations (up to x²), {exp} is > 2 in the expression '{val} ^ {exp}'")
        self.val = val
        self.exp = exp

    def __add__(self, target):
        if type(target) is ComplexNumber and self.exp == target.exp:
            return ComplexNumber(self.val + target.val, self.exp)
        else:
            raise MismatchingExponentError

    def __sub__(self, target):
        if type(target) is ComplexNumber and self.exp == target.exp:
            return ComplexNumber(self.val - target.val, self.exp)
        else:
            raise MismatchingExponentError

    def __mul__(self, target):
        if type(target) is not ComplexNumber or self.exp == 0:
            return ComplexNumber(self.val * target.val, self.exp)
        else:
            raise MismatchingExponentError

    def __div__(self, target):
        if type(target) is not ComplexNumber or self.exp == 0:
            return ComplexNumber(self.val / target.val, self.exp)
        else:
            raise MismatchingExponentError

    def __str__(self):
        if self.exp == 0:
            return f"{self.val}"
        return f"{self.val} * X^{int(self.exp)}"

    def __repr__(self):
        if self.exp == 0:
            return f"{self.val}"
        return f"{self.val}.x^{int(self.exp)}"

    @staticmethod
    def fromString(line):
        components = line.split('*')
        if len(components) > 2 or len(components) == 0:
            raise InvalidExpression(f"Invalid expression: {line}")
        
        # get float
        try:
            val = float(components[0])
        except Exception as e:
            raise InvalidExpression(f"{components[0]} is not a valid real float")
        
        # get exponent
        if len(components) == 1:
            exp = 0
        else:
            subcomponents = components[1].split('^')
            if len(subcomponents) == 0 or len(subcomponents) > 2 or (subcomponents[0] != "X" and subcomponents[0] != "x"):
                raise InvalidExpression(f"{components[1]} is not a valid complex number for this solver")
            try:
                exp = int(subcomponents[1])
            except Exception as e:
                raise InvalidExpression(f"{subcomponents[1]} is not a valid integer (to be an exponent)")
        return ComplexNumber(val, exp)
