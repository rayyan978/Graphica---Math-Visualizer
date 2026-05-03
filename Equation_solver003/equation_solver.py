import math
import cmath
import matplotlib.pyplot as plt
import numpy as np


# ------------------ GRAPH FUNCTIONS ------------------

def plot_linear(a,b,c):
    x = np.linspace(-10,10,400)
    y = (c-b)/a

    y_vals = (c - b)/a * np.ones_like(x)

    plt.plot(x,y_vals,label="solution line")
    plt.axhline(0)
    plt.axvline(0)
    plt.title("Linear Equation Visualization")
    plt.show()


def plot_quadratic(a,b,c):

    x = np.linspace(-10,10,400)
    y = a*x**2 + b*x + c

    plt.plot(x,y)
    plt.axhline(0)
    plt.axvline(0)
    plt.title("Quadratic Graph")
    plt.show()



# ------------------ LINEAR SOLVER ------------------

def solve_linear():

    print("Linear equation solver")
    print("Form: ax + b = c")

    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
    except ValueError:
        print("Invalid input")
        return
    print("your equation is:")
    print(f"{a}x + {b} = {c}")
    if a == 0:
        print("Coefficient a cannot be zero")
        return

    print("Step 1: subtract b from both sides")

    new_c = c - b

    print(f"{a}x = {new_c}")

    print("Step 2: divide both sides by a")

    x = new_c/a

    print(f"x = {x}")

    plot_linear(a,b,c)



# ------------------ QUADRATIC SOLVER ------------------

def solve_quadratic():

    print("Quadratic equation")
    print("Form: ax² + bx + c = 0")

    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
    except ValueError:
        print("Invalid input")
        return
    print("Your equation is : ")
    print(f"{a}x^2 + {b}x + {c} = 0")
    if a == 0:
        print("This becomes a linear equation.")
        return

    print("Step 1: Compute discriminant")

    D = b**2 - 4*a*c

    print(f"D = {D}")

    if D > 0:
        
        root = math.sqrt(D)
        print("Two real roots")
        x1= (-b+root)/(2*a)
        x2= (-b-root)/(2*a)
        print(f"Solution: x1 ={x1}")
        print(f"x2 ={x2} ")

    elif D == 0:
        print("One repeated root")
        x=-b/(2*a)
        print(f"solution : x = {x}")

    elif D < 0:
        c_root = cmath.sqrt(D)
        print("Two complex roots")
        x1 = (-b+c_root)/(2*a)
        x2 = (-b-c_root)/(2*a)
        print(f"Solutions : x1 = {x1}")
        print(f"x2 = {x2}")
        if a > 0 :
           print("Quick Tip : The graph is completely above x-axis ")
        if a < 0 :
            print("QUick Tip : This graph is completely below x-axis ")


    # Vertex
    vx = -b/(2*a)
    vy = a*vx**2 + b*vx + c

    print(f"Vertex = ({vx}, {vy})")

    plot_quadratic(a,b,c)



# ------------------ TWO VARIABLE SOLVER ------------------

def solve_two_variables():

    print("System of equations")

    print("a1x + b1y = c1")
    print("a2x + b2y = c2")

    try:
        a1 = float(input("a1: "))
        b1 = float(input("b1: "))
        c1 = float(input("c1: "))

        a2 = float(input("a2: "))
        b2 = float(input("b2: "))
        c2 = float(input("c2: "))
    except ValueError:
        print("Invalid input")
        return
    print("Your Equations are : ")
    print(f"{a1}x + {b1}y = {c1}")
    print(f"{a2}x + {b2}y = {c2}")
    determinant = a1*b2 - a2*b1

    if determinant == 0:
        print("No unique solution")
        return

    x = (c1*b2 - c2*b1)/determinant
    y = (a1*c2 - a2*c1)/determinant

    print("Solution")
    print(f"x = {x}")
    print(f"y = {y}")



# ------------------ INEQUALITY SOLVER ------------------

def solve_inequality():

    print("Linear Inequality")

    print("Form: ax + b [<,>,<=,>=] c")

    try:
        a = float(input("a: "))
        b = float(input("b: "))
        sign = input("sign (<,>,<=,>=): ")
        c = float(input("c: "))
    except ValueError:
        print("Invalid input")
        return

    if a == 0:
        print("Coefficient a cannot be zero")
        return

    new_c = c - b

    x = new_c/a

    if a < 0:
        if sign == "<": sign = ">"
        elif sign == ">": sign = "<"
        elif sign == "<=": sign = ">="
        elif sign == ">=": sign = "<="

    print(f"Solution: x {sign} {x}")



# ------------------ MENU ------------------

while True:

    print("========================")
    print(" EQUATION SOLVER ")
    print("========================")

    print("1 Linear equation")
    print("2 Quadratic equation")
    print("3 Two variable system")
    print("4 Linear inequality")
    print("5 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        solve_linear()

    elif choice == "2":
        solve_quadratic()

    elif choice == "3":
        solve_two_variables()
        
    elif choice == "4":
        solve_inequality()

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")


