import sys
M = sys.argv[1]
N = sys.argv[2]
A = M[:].split(",")
B = N[:].split(",")

print("SetA:", A)
print("SetB:", B)
I = []
DBA = []
DAB = []
for i in A:
    if i in B:
        I.append(i)
for i in A:
    if not i in B:
        DAB.append(i)
for i in B:
    if not i in A:
        DBA.append(i)
x = A + DBA
print("Intersection of A and B:", I)
print("Union of A and B:", x)
print("Difference of A and B:", DAB)





