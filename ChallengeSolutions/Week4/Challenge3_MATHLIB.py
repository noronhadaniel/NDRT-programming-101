import re, math, sys
# from myutils import header
"""
PYTHON 3.6+
Personal library of math functions (incl. Calculus)
"""
def evals(func, x, rnd = 20):
    """
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter value for x
    Optional round argument at end to give decimal point precision (dp)
    Evaluates function by substituting x
    """
    func = str(func)
    if re.search(r'[a-zA-z]', func) == None:
        return round(eval(func), rnd)
    termslst = func.strip().split(' + ')
    outlst = []
    for t in termslst:
        if re.search(r'[a-zA-z]', t):
            if re.search(r'(\d+\.\d+|\d+|-\d+\.\d+|-\d+|-)[a-zA-z]', t):
                co = re.search(r'(\d+\.\d+|\d+|-\d+\.\d+|-\d+|-)[a-zA-z]', t).group()
                co = re.search(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+|-', co).group()
                if co == "-":
                    co = -1
                out = f"{co}*({x})"
                if "^" in t:
                    power = re.search(r'\^(\d+\.\d+|\d+|-\d+\.\d+|-\d+)', t).group()
                    power = re.search(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+', power).group()
                    out = f"{co}*(({x})**{power})"
            elif re.search(r'[a-zA-z]\^', t):
                power = re.search(r'\^(\d+\.\d+|\d+|-\d+\.\d+|-\d+)', t).group()
                power = re.search(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+', power).group()
                out = f"({x})**{power}"
            else:
                out = str(x)
        else:
            out = str(t)
        outlst.append(out)
    toeval = " + ".join(outlst)
    ans = eval(toeval)
    return round(ans, rnd)

def diff(func, rnd = 20):
    """
    Finds the derivative of 'func'. Returns derivative as string.
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter function like 4x and use ^ for exponent.
    Simplify the function terms before entering.
    Optional round argument at end to give decimal point precision (dp)
    """
    termlst = func.strip().split(' + ')
    outlst = []
    if re.search(r'[a-zA-z]', func):
        d = re.search(r'[a-zA-z]', func).group(0)
    else:
        d = "x"
    for n in termlst:
        if re.search(rf'-{d}', n):
            co = '-1'
        elif re.search(rf'^{d}', n):
            co = '1'
        elif re.search(rf'\d+\.\d+{d}|\d+{d}|-\d+\.\d+{d}|-\d+{d}', n):
            co = re.search(rf'\d+\.\d+{d}|\d+{d}|-\d+\.\d+{d}|-\d+{d}', n).group()
            co = re.search(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+', co).group()
        else:
            co = re.search(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+', n).group()
        if f'{d}^' in n:
            power = re.search(rf"{d}\^\d+\.\d+|{d}\^-\d+\.\d+|{d}\^-\d+|{d}\^\d+", n).group()
            power = re.search(r"\d+\.\d+|-\d+\.\d+|\d+|-\d+", power).group()
        elif d in n:
            power = '1'
        else:
            power = '0'
        nco = float(co) * float(power)
        npower = float(power) - 1.0

        if npower == 0.0:
            out = f"{round(nco, rnd)}"
        elif nco == 0.0:
            out = '0'
        elif nco == 1.0 and npower == 1.0:
            out = f"{d}"
        elif nco == 1.0:
            out = f"{d}^{round(npower, rnd)}"
        elif npower == 1.0:
            out = f"{round(nco, rnd)}{d}"
        else:
            out = f"{round(nco, rnd)}{d}^{round(npower, rnd)}"

        outlst.append(out)
        if '0' in outlst:
            outlst.pop()

    x = " + ".join(outlst)
    if len(outlst) == 0:
        return 0
    return x

def indef_integrate(func, rnd = 20):
    """
    Finds the integral of 'func'. Returns integral as string.
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter function like 4x and use ^ for exponent.
    Simplify the function terms before entering.
    "c" is the constant of integration ("" used to differentiate from variable c if used).
    Optional round argument at end to give decimal point precision (dp)
    """
    termlst = func.strip().split(' + ')
    outlst = []
    if re.search(r'[a-zA-z]', func):
        d = re.search(r'[a-zA-z]', func).group(0)
    else:
        d = "x"
    for n in termlst:
        if re.search(rf'-{d}', n):
            co = '-1'
        elif re.search(rf'^{d}', n):
            co = '1'
        elif re.search(rf'\d+\.\d+{d}|\d+{d}|-\d+\.\d+{d}|-\d+{d}', n):
            co = re.search(rf'\d+\.\d+{d}|\d+{d}|-\d+\.\d+{d}|-\d+{d}', n).group()
            co = re.search(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+', co).group()
        else:
            co = re.search(r'\d+\.\d+|\d+|-\d+\.\d+|-\d+', n).group()

        if f'{d}^' in n:
            power = re.search(rf"{d}\^\d+\.\d+|{d}\^-\d+\.\d+|{d}\^-\d+|{d}\^\d+", n).group()
            power = re.search(r"\d+\.\d+|-\d+\.\d+|\d+|-\d+", power).group()
        elif d in n:
            power = '1'
        else:
            power = '0'
        if power == '-1' and co == '1':
            out = f'ln(|{d}|)'
            outlst.append(out)
            continue
        elif power == '-1' and co == '-1':
            out = f'-ln(|{d}|)'
            outlst.append(out)
            continue
        elif power == '-1':
            out = f'{round(float(co), rnd)}ln(|{d}|)'
            outlst.append(out)
            continue
        nco = float(co) / (float(power) + 1.0)
        npower = float(power) + 1.0
        if nco == 0.0:
            out = '0'
        elif nco == 1.0 and npower == 1.0:
            out = f"{d}"
        elif nco == 1.0:
            out = f"{d}^{round(npower, rnd)}"
        elif npower == 1.0:
            out = f"{round(nco, rnd)}{d}"
        else:
            out = f"{round(nco, rnd)}{d}^{round(npower, rnd)}"
        outlst.append(out)
        if '0' in outlst:
            outlst.pop()
    x = " + ".join(outlst)
    ans = f"{x} + \"c\""
    if ans == " + \"c\"":
        ans = "\"c\""
    return ans

def gradient(func, x, rnd = 20):
    """
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter function like 4x and use ^ for exponent.
    Simplify the function terms before entering.
    Enter a single number for x
    Optional round argument at end to give decimal point precision (dp)
    Differentiates and evaluates dy/dx with x (returns gradient)
    """
    return evals(diff(func), x, rnd)

def coords(func, x, rnd = 20):
    """
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter function like 4x and use ^ for exponent.
    Enter x coordinate, returns y
    Optional round argument at end to give decimal point precision (dp)
    """
    y = evals(func, float(x))
    return round(float(x), rnd), round(y, rnd)

def tangent(func, x, rnd = 20):
    """
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter function like 4x and use ^ for exponent.
    Enter x coordinate, returns equation of line / tangent at a point in y = mx + c form
    Optional round argument at end to give decimal point precision (dp)
    """
    if re.search(r'[A-Za-z]', func) == None:
        return 0
    y = evals(func, x)
    m = gradient(func, x)
    c = y - m * x
    var = re.search(r'[A-Za-z]', func).group()
    out = f'f({var}) = {round(m, rnd)}{var} + {round(c, rnd)}'
    return out

def normal(func, x, rnd = 20):
    """
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter function like 4x and use ^ for exponent.
    Enter x coordinate, returns equation of normal at a point in y = mx + c form
    Optional round argument at end to give decimal point precision (dp)
    """
    if re.search(r'[A-Za-z]', func) == None:
        return float("inf")
    y = evals(func, x)
    m = (-1.0)/gradient(func, x)
    c = y - m * x
    var = re.search(r'[A-Za-z]', func).group()
    out = f'f({var}) = {round(m, rnd)}{var} + {round(c, rnd)}'
    return out

def def_integrate(func, ll, ul, rnd = 20):
    """
    Enter function as string (simplified) and use ' + ' to separate terms
    (e.g. 'A + B...' or 'A + -B...')
    Enter function like 4x and use ^ for exponent.
    Enter lower limit(ll) and upper limit(ul) as well.
    Optional round argument at end to give decimal point precision (dp)
    Returns definite integral answer.
    """
    f = indef_integrate(func)
    if " + \"c\"" not in f:
        return 0
    if "ln" in f:
        return "Cannot solve! Please remove x^-1 term from function!"
    fn = f.replace(' + \"c\"', '')
    f2 = evals(fn, ul)
    f1 = evals(fn, ll)
    ans = f2 - f1
    return round(ans, rnd)

def varfind(func):
    if re.search(r'[A-Za-z]', func) == None:
        return "x"
    else:
        return re.search(r'[A-Za-z]', func).group()

class quadratic(object):
    def __init__(self, func):
        """
        Enter function as string (simplified) and use ' + ' to separate up to THREE terms
        [Standard] FORM: ax^2 + bx + c OR -ax^2 + -bx + -c (is considered as = 0) [any variable may be used instead of x]
        ^Note that a, b, and c are constants
        1st term must be x^2 term
        Optional round argument at end to give decimal point precision (dp)
        Returns 2 solutions for x or any variable (may be repeated) using quadratic formula
        """
        if re.search(r'[A-Za-z]\^2', func) == None:
            print("ERROR:", "Invalid input. This is not a quadratic function.")
            sys.exit(1)
        else:
            var = re.search(r'[A-Za-z]+', func).group()
        if len(var) > 1:
            print("ERROR:", "Invalid input. Enter only 1 variable.")
            sys.exit(1)
        termlst = func.strip().split(' + ')
        if len(termlst) > 3:
            print("ERROR:", "Invalid input. Enter no more than 3 terms.")
            sys.exit(1)
        if len(termlst) == 0:
            print("ERROR:", "No function provided.")
            sys.exit(1)
        if "^2" not in termlst[0]:
            print("ERROR:", f"Incorrect form used. {var}^2 term must be first.")
            sys.exit(1)
        elif termlst[0] == f"{var}^2":
            a = 1
        elif termlst[0] == f"-{var}^2":
            a = -1
        else:
            a = re.search(rf'\d+\.\d+{var}|\d+{var}|-\d+\.\d+{var}|-\d+{var}', termlst[0]).group()
            a = float(re.search(rf'\d+\.\d+|\d+|-\d+\.\d+|-\d+', termlst[0]).group())
        if len(termlst) == 3:
            if termlst[1] == f"{var}":
                b = 1
            elif termlst[1] == f"-{var}":
                b = -1
            elif re.search(rf'(\d+\.\d+{var}|\d+{var}|-\d+\.\d+{var}|-\d+{var})$', termlst[1]) == None:
                print("ERROR:", f"Second term must be in the form b{var}, where b is a constant.")
                sys.exit(1)
            else:
                b = float(re.search(rf'\d+\.\d+|\d+|-\d+\.\d+|-\d+', termlst[1]).group())
            if var in termlst[2]:
                print("ERROR:", f"Third term must be a constant (c). Remove the variable.")
                sys.exit(1)
            else:
                c = termlst[2]
        elif len(termlst) == 2:
            if var not in termlst[1]:
                b = 0
                c = termlst[1]
            elif (var in termlst[1]) and ("^" in termlst[1]):
                print("ERROR:", f"Second term must be in the form b{var}, where b is a constant.")
                sys.exit(1)
            else:
                b = float(re.search(rf'\d+\.\d+|\d+|-\d+\.\d+|-\d+', termlst[1]).group())
                c = 0
        else:
            b = c = 0
        self.func = func
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.var = var
        if "-" in str(a):
            self.tpstyle = "Maximum"
        else:
            self.tpstyle = "Minimum"

    def quadraticsolve(self, rnd = 20):
        """
        Optional round argument at end to give decimal point precision (dp)
        Returns 2 solutions for x or any variable (may be repeated) using quadratic formula
        """
        try:
            ans1 = (-self.b + math.sqrt((self.b) ** 2 -4 * self.a * self.c)) / (2 * self.a)
            ans2 = (-self.b - math.sqrt((self.b) ** 2 -4 * self.a * self.c)) / (2 * self.a)
        except ValueError:
            return "NO REAL ROOT!", "NO REAL ROOT!"
        return round(ans1, rnd), round(ans2, rnd)
    
    def yintercept(self, rnd = 20):
        # return self.c
        return evals(self.func, 0, rnd)
    
    def turningpoint(self, rnd = 20):
        # tpy = (-(self.b / (2 * self.a)) ** 2) + self.c
        tpx = -(self.b / (2 * self.a))
        tpy = evals(self.func, tpx)
        return round(tpx, rnd), round(tpy, rnd)


"""
# CALLING/TESTING:
import os
#Only use for 1 variable. Program works for real number domain only. Tests MATHLIB module.
##################################################################################################
os.system('cls')
rnd = 3 # rounding d.p.
testfunction = "6x^-3 + -3.2x^-2 + 0.7x + -2x^2 + -x^3 + x^4 + 77" # feel free to change!
testvar = -8 # test variable value for test function ^
quadraticfunction = "6b^2 + 11b + -35"
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

"""

