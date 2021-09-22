# Challenge 1 - Quadratic Equation Solver (09/16/2021)
import math
import sys
###QUADRATIC EQUATION PARAMETERS###
if len(sys.argv) > 4:
    print(f"\nToo many arguments provided (only 3 were required but {len(sys.argv) - 1} were provided).\nIgnoring extra arguments.")
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except IndexError:
    a = 6
    b = 11
    c = -35
    print(f"\nInsufficient program arguments provided. Using defaults for a, b, and c as defined in the program:\na = {a}, b = {b}, c = {c}")
except ValueError:
    print("\nPlease enter rational numbers for program arguments.\n")
    sys.exit()
###################################
if (b < 0) & (c < 0):
    print(f"\nEquation: f(x) = {a}x^2 - {-b}x - {-c}")
elif b < 0:
    print(f"\nEquation: f(x) = {a}x^2 - {-b}x + {c}")
elif c < 0:
    print(f"\nEquation: f(x) = {a}x^2 + {b}x - {-c}")
else:
    print(f"\nEquation: f(x) = {a}x^2 + {b}x + {c}")
""""""
def turningpoint(a,b,c,rnd = 3):
    """
    Function that finds the minimum or maximum of a quadratic function using its derivative: 2ax + b = 0
    """
    x = (-b/(2*a))
    if x == 0:
        x = -x
    y = (a*(x**2)+b*x+c)
    if a < 0:
        return ["maximum",round(x,rnd),round(y,rnd)]
    else:
        return ["minimum",round(x,rnd),round(y,rnd)]

def discriminant(a,b,c):
    """
    Function that calculates the discriminant for a quadratic equation given a, b, c from ax^2 + bx + c = 0
    """
    return ((b ** 2) - 4 * a * c)
""""""
def solvequadratic(a,b,c,rnd = 3):
    """
    Function that solves quadratic equations given a, b, c from ax^2 + bx + c = 0
    Only finds real roots!
    """
    x1 = (-b + math.sqrt(((b ** 2) - 4 * a * c))) / (2 * a)
    x2 = (-b - math.sqrt(((b ** 2) - 4 * a * c))) / (2 * a)
    return [round(x1,rnd),round(x2,rnd)]

if a == 0:
    print("This is not a quadratic equation. Please ensure that a does not equal 0 in ax^2 + bx + c.\n")
    sys.exit()

print("Discriminant = " + str(discriminant(a,b,c)))
if discriminant(a,b,c) < 0:
    print("This quadratic equation has no real roots.")
elif discriminant(a,b,c) == 0:
    print(f"This quadratic equation has 1 repeated root: x = {solvequadratic(a,b,c)[0]}")
elif (solvequadratic(a,b,c)[0] > 0) & (solvequadratic(a,b,c)[1] > 0):
    print(f"This quadratic equation has 2 positive roots: x = {solvequadratic(a,b,c)[0]} and x = {solvequadratic(a,b,c)[1]}")
elif (solvequadratic(a,b,c)[0] > 0) & (solvequadratic(a,b,c)[1] < 0):
    print(f"This quadratic equation has a positive root at x = {solvequadratic(a,b,c)[0]} and a negative root at x = {solvequadratic(a,b,c)[1]}")
elif (solvequadratic(a,b,c)[0] < 0) & (solvequadratic(a,b,c)[1] > 0):
    print(f"This quadratic equation has a positive root at x = {solvequadratic(a,b,c)[1]} and a negative root at x = {solvequadratic(a,b,c)[0]}")
else:
    print(f"This quadratic equation has 2 negative roots: x = {solvequadratic(a,b,c)[0]} and x = {solvequadratic(a,b,c)[1]}")

print(f"Its {turningpoint(a,b,c)[0]} is at the point ({turningpoint(a,b,c)[1]}, {turningpoint(a,b,c)[2]})")
print(f"Its y-intercept is at the point (0.0, {float(c)})\n")

#END OF PROGRAM#

