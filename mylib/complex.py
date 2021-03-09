from .exceptions import MismatchingExponentError, InvalidExpression

class ComplexNumber:
    
    def __init__(self, val=0.0, exp=0):
        if exp > 2:
            raise InvalidExpression(f"This solver can only solve quadratic equations (up to x²), {exp} is > 2 in the expression '{val} * X ^ {exp}'")
        if exp < 0:
            raise InvalidExpression(f"An exponent cannot be negative, {exp} is negative in the expression '{val} * X ^ {exp}'")
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

    def __neg__(self):
        return ComplexNumber(-self.val, self.exp)

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
        def get_x_exponent(expr):
            subcomponents = expr.split('^')
            if len(subcomponents) == 0 or len(subcomponents) > 2:
                raise InvalidExpression("Extraneous '^' found in expression")
            if len(subcomponents) == 1 and (subcomponents[0] == "X" or subcomponents[0] == "x"):
                return 1
            if (subcomponents[0] != "X" and subcomponents[0] != "x"):
                raise InvalidExpression(f"{subcomponents[0]} cannot be exponentiated")
            try:
                return int(subcomponents[1])
            except ValueError as e:
                raise InvalidExpression(f"Invalid X exponent")
        
        if line == "X" or line == "x":
            return ComplexNumber(1, 1)
        components = line.split('*')
        if len(components) > 2 or len(components) == 0:
            raise InvalidExpression(f"Invalid expression: {line}")
        
        # get float
        try:
            val = float(components[0])
        except ValueError as e:
            return ComplexNumber(1, get_x_exponent(components[0]))
            raise InvalidExpression(f"{components[0]} is not a valid real float")
        
        # get exponent
        if len(components) == 1:
            exp = 0
        else:
            exp = get_x_exponent(components[1])
        return ComplexNumber(val, exp)
