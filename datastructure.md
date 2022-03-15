{% include navigation.html  %}

## [Replit Link](https://replit.com/@ByronLu/TT0#main.py)

## Code

### Menu
```
main_menu = [
    ["Swap", "swap.py"],
    ["Matrix", "matrix.py"], 
    ["Tree", "tree.py"],
    ["Animation", "animation.py"],
]


border = "=" * 25
banner = f"\n{border}\nWhich option would you like?\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice> ")


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
        print(f"Invalid Choice: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Invalid Choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
```

### Animation
```
import time

ANSI_CLEAR_SCREEN =  lambda: print('\n' * 150)
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u""
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def drive(position):
    print('\n' * 100)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "          ----------------------      ")
    print(sp + "          |                    |      ")
    print(sp + "          |                    |      ")
    print(sp + "       -----------------------------  ")
    print(sp + "       | ------------------------- |  ")
    print(sp + "       | ------------------------- |  ")
    print(sp + "       -----------------------------  ")
    print(sp + "         0   0               0   0    ")
    print(RESET_COLOR)

def animation():

    start = 0
    distance = 30
    step = 1


    for position in range(start, distance, step):
        drive(position)
        time.sleep(.1)

animation()
```
### Tree
```
def tree(x):
    print("\n".join([f"{'*'*(2* n + 1):^{2*x+1}}" for n in range(x)]))

def trunk(n):
      for i in range(n):
        for j in range(n-1):
            print('      ', end=' ')
        print('***')

tree(1)
trunk(3)
```
