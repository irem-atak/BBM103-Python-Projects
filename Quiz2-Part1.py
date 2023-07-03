import sys
import math

arglist = sys.argv
arglist.remove(arglist[0])
for i in range(len(arglist)):
    arglist[i] = int(arglist[i])
a = arglist[0]
b = arglist[1]
c = arglist[2]
if (b**2 - 4*a*c) < 0 :
    print("Neither of the solutions are real numbers")
elif (b**2 - 4*a*c ) == 0:
    print("Quadratic has a repeated real number solution")
    x = (-b + (math.sqrt(b ** 2 - 4 * a * c))) / 2 * a
    y = (-b - (math.sqrt(b ** 2 - 4 * a * c))) / 2 * a
    if x == y:
        print("Solution(s):", "%.2f" % x)
elif (b**2 - 4*a*c ) > 0:
    print("There are two solutions")
    x = (-b + (math.sqrt(b**2 - 4*a*c)))/2*a
    y = (-b - (math.sqrt(b**2 - 4*a*c)))/2*a
    print("Solution(s):", "%.2f"% x, "%.2f" % y)
