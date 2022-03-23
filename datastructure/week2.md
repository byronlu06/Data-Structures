{% include navigation.html  %}

## Week 2 [Replit Link](https://replit.com/@ByronLu/TT0#main.py)

<br>

## Code

<br>

### Factorial
```
# this is test driver or code that plays when executed directly, versus import which will not run these statements
# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n - 1)

def factorial():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
```

### Math

#### Square
```
num = float(input(" Enter a number: "))
square = math.pow(num, 2.0)
# determines the square of given value
print("The square of a given number {0} = {1}".format(num, square)) 
# prints the square
```

#### Square Root
```
num = float(input(" Enter a number: "))
sqRoot = math.pow(num, 0.5)
# determines the square root of given value
print("The square root of a given number {0} = {1}".format(num, sqRoot)) 
# prints the square root
```

#### Cube
```
num = float(input(" Enter a number: "))
sqRoot = math.pow(num, 3)
# determines the cube of given value
print("The square root of a given number {0} = {1}".format(num, sqRoot)) 
# prints the cube
```

#### Cube Root
```
num = float(input(" Enter a number: "))
cubeRoot = math.pow(num, 1/3)
# determines the cube root of given value
print("The square root of a given number {0} = {1}".format(num, cubeRoot)) 
# prints the cube root
```

### Palindrome
```
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


# Driver Code

s = str(input("Enter a word: "))
ans = isPalindrome(s)

if ans:
	print(s, "is a palindrome")

else:
	print(s, "is not a palindrome")
```
