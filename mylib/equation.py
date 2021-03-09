from .exceptions import InvalidExpression
from .complex import ComplexNumber

class Equation:

    def __init__(self, line):
        line = line.replace(" ", "").replace("-", "+-")
        sides = [s.split('+') for s in line.split("=")]
        for i in range(len(sides)):
            if sides[i][0] == "" and len(sides[i]) > 1:
                sides[i] = sides[i][1:]

        if len(sides) < 2:
            sides.append(["0"])
        elif len(sides) > 2:
            raise InvalidExpression(f"Too many '=' signs found in expression '{line}'")
        tmp_left = [ComplexNumber.fromString(s) for s in sides[0]]
        tmp_right = [ComplexNumber.fromString(s) for s in sides[1]]

        self.expressions = [0, 0, 0]
        # regroup to the left side:
        for n in tmp_right:
            self.expressions[n.exp] -= n.val
        for n in tmp_left:
            self.expressions[n.exp] += n.val

    @property
    def degree(self):
        return 2 if self.expressions[2] != 0 else (1 if self.expressions[1] != 0 else 0)

    def __str__(self):
        numbers = []
        for i in range(len(self.expressions)):
            if self.expressions[i] != 0.0:
                numbers.append(ComplexNumber(self.expressions[i], i))
        return f"{' + '.join(str(n) for n in numbers)} = 0.0"

    def __repr__(self):
        return self.__str__()

    def solve(self, verbose):
        print(f"Solving (verbose = {verbose})...")
