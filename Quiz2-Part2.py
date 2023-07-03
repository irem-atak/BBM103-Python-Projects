import sys

arglist = sys.argv
arglist.remove(arglist[0])
b = arglist[0].split(",")
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(len(b)):
    if b[i] < 0 :
        b.remove(b[i])
def even_numbers(b):
    even = []
    for n in b:
        if n % 2 == 0:
            even.append(n)
    return even
even = even_numbers(b)
print("Even Numbers:", even_numbers(b))

def sum_of_even(even):
    sum = 0
    sumofe = []
    for m in even:
        sum = sum + m
        sumofe.append(m)
    return sum
sumofe = sum_of_even(even)
print("Sum of Even Numbers:", sum_of_even(even))

def sum_of_all(b):
    sumo = 0
    sumofall = []
    for k in b:
        sumo = sumo + k
        sumofall.append(k)
    return sumo
sumofall = sum_of_all(b)

x = int(sumofe)/int(sumofall)
print("Even Number Rate:", "%.3f" % x)







