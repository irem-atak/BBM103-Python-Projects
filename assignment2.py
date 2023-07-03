import sys

arglist = sys.argv
arglist.remove(sys.argv[0])
a = arglist
b = ''.join(a)
for character in arglist:
    if b.isalpha() == False :
        print("All arguments should be words")
        exit()
if len (sys.argv) != 3 :
    print ("Please run with 3 arguments")
elif len(a[0]) == len(a[1]):
    print("Arguments should be different length")
elif len(a[0]) == len(a[2]):
    print("Arguments should be different length")
elif len(a[1]) == len(a[2]):
    print("Arguments should be a different length")
else:
    print("Find longest word using letters given below")
    print(sorted(filter(lambda x: str.isalpha(x), str(''.join(a)))))
    n = str(input("Guess a longest word: "))
    if len(n) == len(max(a, key=len )):
        print("You found a word from the list")
        print("You won 50 points")
    elif not n in arglist:
        print("The word you guessed is not in the list")
        print("You lost !")
    elif len(n) == len(min(a, key=len)):
        print("You found a word from the list")
        print("You won 10 points")
    else:
        print("You found a word from the list")
        print("You won 30 points")

