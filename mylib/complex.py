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
        if self.val == 1 and self.exp == 1:
            return f"x"
        if self.val == -1 and self.exp == 1:
            return f"-x"
        if self.val == 1:
            return f"x^{self.exp}"
        if self.val == -1:
            return f"-x^{self.exp}"
        if self.exp == 1:
            return f"{self.val}x"
        return f"{self.val}x^{self.exp}"

    def __repr__(self):
        return str(self)

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
        
        # get val
        try:
            val = int(components[0])
        except ValueError as e:
            if len(components) == 1:
                # natural hack, disgusting:
                tmp = components[0].split('^')
                if len(tmp) == 2 and len(tmp[0]) > 1 and (tmp[0][-1] == 'x' or tmp[0][-1] == 'X'):
                    nb = tmp[0][:-1]
                    if len(nb) == 1 and nb[0] == '-':
                        nb = -1
                    return ComplexNumber(int(nb), int(tmp[1]))
                if len(tmp) == 1 and len(tmp[0]) > 1 and (tmp[0][-1] == 'x' or tmp[0][-1] == 'X'):
                    nb = tmp[0][:-1]
                    if len(nb) == 1 and nb[0] == '-':
                        nb = -1
                    return ComplexNumber(int(nb), 1)
                return ComplexNumber(1, get_x_exponent(components[0]))
            else:
                raise e
        

        print(3)
        
        # get exponent
        if len(components) == 1:
            exp = 0
        else:
            exp = get_x_exponent(components[1])
        return ComplexNumber(val, exp)
