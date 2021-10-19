from Challenge3_MATHLIB import *
from Challenge3_myutils import header
import os
# Only use for 1 variable. Program works for real number domain only. Tests MATHLIB module.
##################################################################################################
os.system('cls')
rnd = 4 # rounding d.p.
testfunction = "6x^-3 + -3.2x^-2 + 0.7x + -2x^2 + -x^3 + x^4 + 77" # feel free to change!
testvar = -8 # test variable value for test function ^
quadraticfunction = "6x^2 + 11x + -35"
header("Function Analyzer")
print(f"f({varfind(testfunction)}) = {testfunction}")
print(f'f\'({varfind(testfunction)}) = {diff(testfunction, rnd)}')
print(f'integral_d{varfind(testfunction)} = {indef_integrate(testfunction, rnd)}')
print(f"{varfind(testfunction)} = {testvar}")
try:
    print(f'f({varfind(testfunction)}) = {evals(testfunction, testvar, rnd)}')
    print(f'({varfind(testfunction)}, f({varfind(testfunction)})) = {coords(testfunction, testvar, rnd)}')
    print(f'm = {gradient(testfunction, testvar, rnd)}')
    print(f'Tangent Equation : {tangent(testfunction, testvar, rnd)}')
    print(f'Normal Equation : {normal(testfunction, testvar, rnd)}')
    print(f'Definite integral_d{varfind(testfunction)} solution (limits: 5 => 7) = {def_integrate(testfunction, 5, 7, rnd)}')
except TypeError:
    print("\nPlease check the terms of function or x value given. Program cannot handle complex numbers.\nIf using negative x value, do not put decimal exponents in function.\n")
print(f"\n**All values rounded to {rnd} d.p.\n")
inp = input(f"\nPress Enter to solve the following quadratic equation: {quadraticfunction} = 0 or enter your own in the same form.\n")
os.system('cls')

if " = 0" in inp:
    quadraticfunction = inp.replace(" = 0", "").strip()
elif " =0" in inp:
    quadraticfunction = inp.replace(" =0", "").strip()
elif "= 0" in inp:
    quadraticfunction = inp.replace("= 0", "").strip()
elif "=0" in inp:
    quadraticfunction = inp.replace("=0", "").strip()
elif inp.strip() != "":
    quadraticfunction = inp.strip()
else:
    pass

quad = quadratic(quadraticfunction)
header("Quadratic equation Analyzer", char = "#")
print(f"Quadratic equation: {quadraticfunction} = 0")
print(f'\n{varfind(quadraticfunction)}1 = {quad.quadraticsolve(rnd)[0]}; {varfind(quadraticfunction)}2 = {quad.quadraticsolve(rnd)[1]}')
print(f'y-intercept is at (0, {quad.yintercept(rnd)})')
print(f'The {quad.tpstyle} is at {quad.turningpoint(rnd)}')
print(f"\n**All values rounded to {rnd} d.p.\n")
##################################################################################################
# Tips:
# We can use *(tuple) to unpack tuple into series of arguments when calling function.
# E.g. tangent(func, *coords(testfunction, 5, 3)) with def tangent(func, x, y, rnd = 20)
input("Press Enter to quit (and clear screen)...")
os.system('cls')
#sys.exit(0)
