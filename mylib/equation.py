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
        self.left = [ComplexNumber.fromString(s) for s in sides[0]]
        self.right = [ComplexNumber.fromString(s) for s in sides[1]]
        self.left.sort(key=lambda x: x.exp)
        self.right.sort(key=lambda x: x.exp)

    def __str__(self):
        return f"{' + '.join(str(n) for n in self.left)} = {' + '.join(str(n) for n in self.right)}"

    def __repr__(self):
        return self.__str__()