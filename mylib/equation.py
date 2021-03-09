from .exceptions import InvalidExpression
from .complex import ComplexNumber

class Equation:

    def __init__(self, line):
        line = line.replace(" ", "").replace("-", "+-")
        sides = [s.split('+') for s in line.split("=")]
        if len(sides) < 2:
            sides.append(["0"])
        elif len(sides) > 2:
            raise InvalidExpression(f"Too many '=' signs found in expression '{line}'")
        tmp_left = [ComplexNumber.fromString(s) for s in sides[0]]
        tmp_right = [ComplexNumber.fromString(s) for s in sides[1]]

        self.expressions = [0, 0, 0]
        self.result = ComplexNumber(0, 0)
        # regroup complexs to the left side:
        for n in tmp_right:
            if n.exp > 0:
                self.expressions[n.exp] -= n.val
            else:
                self.result += n
        for n in tmp_left:
            if n.exp > 0:
                self.expressions[n.exp] += n.val
            else:
                self.result -= n

    def __str__(self):
        numbers = []
        for i in range(len(self.expressions)):
            if self.expressions[i] != 0.0:
                numbers.append(ComplexNumber(self.expressions[i], i))
        return f"{' + '.join(str(n) for n in numbers)} = {str(self.result)}"

    def __repr__(self):
        return self.__str__()
