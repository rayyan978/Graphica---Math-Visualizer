import math
import cmath
def solve_quadratic():
    print("Quadratic equation")
    print("Form : ax^2 + bx + c = 0 ")
    try:
      a= int(input("Enter the value of a : "))
      b=int(input("Enter the value of b : "))
      c=int(input("Enter the value of c : "))
    except ValueError:
       print("Invalid Input ")
       return
    print("Your equation is : ")
    print(f"{a}x^2 + {b}X + {c} = 0 ")
    print("First we need to find the discriminant' D = b^2 - 4ac ")
    print(f"Here D = {b}^2 - 4*{a}*{c}")
    D = b**2 - 4*a*c 
    print(f"D = {D}")
    if D <0 :
      print("Here the D < 0 ")
      print("There are no real solutions")
      D_croot = cmath.sqrt(D)
      print(" Use the Quadratic formula : ")
      print("x1 = -b + √D/2a")
      print("x2 = -b - √D/2a")
      print("The formula becomes : ")
      print(f"x1 = -{b}+√{D}/2*{a}")
      print(f"x2= -{b}-√{D}/2*{a}")
      x1=(-b + D_croot)/(2*a)
      x2=(-b - D_croot)/(2*a)
      print(f"Now x1 = {x1} <--- These are imaginary roots")
      print(f"x2 = {x2}")
    elif D >= 0 :
      print(f"Here D = {D}")
      D_root = math.sqrt(D)
      print(" Use the Quadratic formula : ")
      print("x1 = -b + √D/2a")
      print("x2 = -b - √D/2a")
      print("The formula becomes : ")
      print(f"x1 = -{b}+√{D}/2*{a}")
      print(f"x2= -{b}-√{D}/2*{a}")
      x1=(-b + D_root)/(2*a)
      x2=(-b - D_root)/(2*a)
      print(f"Now x1 = {x1}")
      print(f"x2 = {x2}")
def solve_linear():
    print("Linear equation solver ") 
    print("Type : ax + b = c ")  
    try:
     a = int(input("Enter the value of a : "))
     b = int(input("Enter the value of b : "))
     c = int(input("Enter the value of c : "))
    except ValueError:
       print("Invalid Input")
       return 
    print("Your equation is : ")
    print(f"{a}x + {b} = {c}")
    print(f" First we subtract both sides by the constant term ({b})")
    print(f"{a}x + {b}-{b} = {c}-{b} ")
    print(f"Now our equation becomes : ")
    new_c = c-b
    print(f"{a}x = {new_c}")
    print(f"Now divide bothsides by the coefficient of x ({a})")
    print(f"{a}x/{a} = {new_c}/{a}")
    x = new_c/a 
    print(f"Now x = {x} <-- THIS IS CALLED THE SOLUTION")

def solve_two_variables():
    print("\nForm:")
    print("a₁x + b₁y = c₁")
    print("a₂x + b₂y = c₂\n")

    try:
        a1 = float(input("Enter a₁: "))
        b1 = float(input("Enter b₁: "))
        c1 = float(input("Enter c₁: "))

        a2 = float(input("Enter a₂: "))
        b2 = float(input("Enter b₂: "))
        c2 = float(input("Enter c₂: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print("\nYour equations are:")
    print(f"{a1}x + {b1}y = {c1}")
    print(f"{a2}x + {b2}y = {c2}")

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        print("No unique solution (Determinant = 0)")
        return   

    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    print("\nSolution:")
    print(f"x = {x}")
    print(f"y = {y}")


def solve_linear_inequalities():
  try:
      print("Linear Inequalities solver :")
      print("Form : ax + b [<,>,<=,>=] c ")
      a = float(input("Enter the value of a : "))
      b = float(input("Enter the value of b : "))
      sign = input("Choose the inequality [< , > , <= , >= ]")
      c = float(input("Enter the value od c : "))
  except ValueError:
     print("Invalid Input")
     return 
  print("")
  print("Your inequality :")
  print(f"{a}x + {b} {sign} {c}")
  print(f"Now subtract both sides by the constant ({b})")
  print(f"{a}x = {b} - {b} {sign} {c} - {b}")
  new_c = c -b 
  print(f"{a}x {sign} {new_c}")
  if a > 0 :
      x = new_c/a
      print(f"Now divide both sides by the coefficient of x ")
      print(f"Here the coefficient ({a}) is positive so the inequality remains same ")
      print(f"{a}x/{a} {sign} {new_c}/{a}")
      print(f"x {sign} {x}")
  elif a < 0 :
      if sign == "<": sign = ">"
      elif sign == ">": sign = "<"
      elif sign == "<=": sign = ">="
      elif sign == ">=": sign = "<="
      x = new_c/a
      print("Now divide both sides by the coefficient of x ")
      print(f"Here the coefficient ({a}) is negative so the sign of inequality gets flipped ")
      print("The inequality becomes : ")
      print(f"{a}x/{a} {sign} {new_c}/{a}")
      x = new_c/a
      print(f"x {sign} {x}")
   

print("        EQUATION SOLVER        ")
print("==============================")
print("1. Linear Equation (ax + b = c)")
print("2. Quadratic Equation (ax² + bx + c = 0)")
print("3. Two-Variable Equations")
print("4. Linear Inequalities ")
print("5.    Exit   ")
choice = input("\n Choose an option (1-5): ")
if choice == "1":
 solve_linear()
elif choice == "2":
  solve_quadratic()
elif choice == "3":
  solve_two_variables()
elif choice == "4":
  solve_linear_inequalities()
elif choice == "5":
   print("Goodbye 👋")
  
else:
  print("Invalid choice, try again ^_^")
print('Goodbye 👋') 
exit()