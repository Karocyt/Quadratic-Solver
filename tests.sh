#! /usr/bin/env sh

echo "No Degree:"
./quadratic_solver -v "5 = 4 + 1"
echo "REAL RESULT: All"
echo
echo "First Degree:"
./quadratic_solver -v "5 + 4x = 4"
echo "REAL RESULT: -0.25"
echo
echo "Second Degree, positive discriminant:"
./quadratic_solver -v "5 + 13x + 3x^2 = 1 + x"
echo "REAL RESULTS: -3.6329931618555 and -0.36700683814455"
echo
echo "Second Degree, null discriminant:"
./quadratic_solver -v "6 + 11x + 5x^2 = 1 + x"
echo "REAL RESULT: -1"
echo
echo "Second Degree, negative discriminant:"
./quadratic_solver -v "5 + 3x +3x^2 = 1 + 0x"
echo "REAL RESULT: No Solution"
echo
echo "Third Degree:"
./quadratic_solver -v "5 + 3x +3x^3 = 1 + 0x"
echo "REAL RESULT: FAIL"
echo
echo "Deg0 not solvable:"
./quadratic_solver -v "5 = 1 + 0x"
echo "REAL RESULT: UNSOLVABLE"
echo
echo "Negative exponent:"
./quadratic_solver -v "5 + 13x + 3x^-2 = 1 + x"
echo "REAL RESULTS: -3.6329931618555 and -0.36700683814455"
