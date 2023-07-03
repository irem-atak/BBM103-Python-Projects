import sys
arr = []
x = open(sys.argv[1])
for line in x.readlines():
    arr.append([])
    for i in line.split():
        arr[-1].append(int(i))

first_score=0
def first_output(arr):
    for b in arr:
     for c in b:
          print(c,end = " ")
     print()
    print("Your score is: ",first_score)
first_output(arr)

n, m = input("Please enter a row and column number: ").split()
row = int(n)-1
col = int(m)-1
a = arr[row][col]

def removing(row,col,a):
    if arr[row][col] == a:
        arr[row][col] = " "
        if col!= 0:
            removing(row,col-1,a)
        if col!= len(arr[0])-1:
            removing(row,col+1,a)
        if row!= 0:
            removing(row-1,col,a)
        if row!= len(arr)-1:
            removing(row+1,col,a)
removing(row,col,a)

def counting():
    count=0
    for r in arr:
        for c in r:
            if c==" ":
                count+=1
    return count
from math import sqrt
def fibonacci(z):
        return ((1+sqrt(5))**z-(1-sqrt(5))**z)//(2**z*sqrt(5))
counter1 = counting()
first_score  += fibonacci(counter1)*a

def sliding():
    for row2 in range(1,len(arr)):
        for col2 in range(1,len(arr[0])):
            if arr[row2][col2]== " " and row2!=0:
                if isinstance(arr[row2-1][col2], int):
                    arr[row2][col2], arr[row2-1][col2] = arr[row2-1][col2], arr[row2][col2]
                    return sliding()
    return first_output(arr)
    return counting()
sliding()
n, m = input("Please enter a row and column number: ").split()
row = int(n)-1
col = int(m)-1
a = arr[row][col]
def controlling():
    try:
        if a != " ":
            return removing(row,col,a)
    except IndexError:
        print("Please enter a correct size")
removing(row,col,a)
def counting():
    count=0
    for r in arr:
        for c in r:
            if c==" ":
                count+=1
    return count

counter2= counting()
first_score  += fibonacci(counter2-counter1)*a
sliding()

n, m = input("Please enter a row and column number: ").split()
row = int(n)-1
col = int(m)-1
a = arr[row][col]
removing(row,col,a)
def counting():
    count=0
    for r in arr:
        for c in r:
            if c==" ":
                count+=1
    return count

counter3 = counting()
first_score  += fibonacci(counter3-counter2)*a
sliding()


n, m = input("Please enter a row and column number: ").split()
row = int(n)-1
col = int(m)-1
a = arr[row][col]
removing(row,col,a)
def counting():
    count=0
    for r in arr:
        for c in r:
            if c==" ":
                count+=1
    return count

counter4 = counting()
first_score  += fibonacci(counter4-counter3)*a
sliding()


n, m = input("Please enter a row and column number: ").split()
row = int(n)-1
col = int(m)-1
a = arr[row][col]
removing(row,col,a)
def counting():
    count=0
    for r in arr:
        for c in r:
            if c==" ":
                count+=1
    return count

counter5 = counting()
first_score  += fibonacci(counter5-counter4)*a
sliding()












