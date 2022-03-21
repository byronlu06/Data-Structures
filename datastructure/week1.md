{% include navigation.html  %}

## Week 1 [Replit Link](https://replit.com/@ByronLu/TT0#main.py)

<br>

## Code

<br>

### Sub Menu
```
import time
from week1.lists import tester
from week1.factorial import factorial
from week0.animation import ship

main_menu = [
]

week0_sub_menu = [
    ["Swap", "week0/swap.py"],
    ["Matrix", "week0/matrix.py"],
    ["Animation", ship],
    ["Tree", "week0/tree.py"],
]

week1_sub_menu = [
    ["Lists", tester],
    ["Factorial", factorial],
    ["Fibonacci", "week1/fibonacci.py"],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", week0_submenu])
    menu_list.append(["Week 1", week1_submenu])
    buildMenu(title, menu_list)

def week0_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week0_sub_menu)
def week1_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, week1_sub_menu)
def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
```

### Lists
```
InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Jasmine",
    "LastName": "Lu",
    "DOB": "October 17",
    "Residence": "San Diego",
    "Email": "jasmine06258@gmail.com",
    "Hobbies": ["Polo and Reading",]
})

InfoDb.append({
    "FirstName": "Byron",
    "LastName": "Lu",
    "DOB": "September 24",
    "Residence": "San Diego",
    "Email": "byronlu06@gmail.com",
    "Hobbies": ["Soccer and Chess",]
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Hobbies: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Hobbies"]))  # join allows printing a string list with separator
    print()



# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return  # exit condition

```

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

### Fibonacci
```
nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
```











