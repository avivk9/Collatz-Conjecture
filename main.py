#proves Collatz Conjecture for given range of numbers

#enter amount of numbers
RANGE = 10

def Collatz_Conjecture(n):
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = (n*3) + 1
    if n == 1:
        return True

def Collatz_Conjecture_Path(n):
    path = str(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2
            path += ("->" + str(n))
        else:
            n = (n*3) + 1
            path += ("->" + str(n))
    if n == 1:
        return path

if __name__ == "__main__":
    for n in range(1, RANGE):
        print("works on number: " + str(n))
        Collatz_Conjecture(n)
        print("path: " + Collatz_Conjecture_Path(n))
    print("ended")