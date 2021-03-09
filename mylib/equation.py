from .exceptions import InvalidExpression
from .complex import ComplexNumber

class Equation:

    def __init__(self, line):
        line = line.replace(" ", "").replace("-", "+-")
        sides = [s.split('+') for s in line.split("=")]

        # case of leading - (now "+-"): split at '+' would create an empty value
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

    @staticmethod
    def __non_null_complexs(exp_list):
        numbers = []
        for i in range(len(exp_list)):
            if exp_list[i] != 0:
                numbers.append(ComplexNumber(exp_list[i], i))
        if len(numbers) == 0:
            numbers.append(ComplexNumber(0, 0))
        return numbers

    def __str__(self):
        numbers = Equation.__non_null_complexs(self.expressions)
        return f"{' + '.join(str(n) for n in numbers)} = 0"

    def __repr__(self):
        return self.__str__()

    def solve(self, verbose):
        def step(left, right):
            step.iteration += 1
            numbers = Equation.__non_null_complexs(left)
            if verbose:
                print( f"\tStep {step.iteration: 2}:\t{' + '.join(str(n) for n in numbers)} = {right}")

        def d0(left, right):
            if right == 0:
                print("All real numbers are a solution.")
            else:
                print("There is something really wrong with your mathematics: The sum of the 2 sides of an equation should equal zero, this is the whole point of the thing!")

        def d1(left, right):
            if right == 0:
                print("The solution is 0.")
            else:
                right /= left[1]
                left[1] = 1
                step(left, right)
                print(f"The solution is {right}.")

        def d2(left, right):
            return NotImplemented

        step.iteration = 0

        left, right = self.expressions, -self.expressions[0]
        left[0] = 0.0
        step(left, right)

        fun = (d0, d1, d2)

        return fun[self.degree](left, right)
