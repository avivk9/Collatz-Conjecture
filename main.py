#proves Collatz Conjecture for given range of numbers

#enter amount of numbers
RANGE = 99999

def Collatz_Conjecture(n):
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = (n*3) + 1
    if n == 1:
        return True

if __name__ == "__main__":
    for n in range(1, RANGE):
        print("works on number: " + str(n))
        Collatz_Conjecture(n)
    print("ended")