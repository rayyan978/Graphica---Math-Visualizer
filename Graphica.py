import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.widgets import CheckButtons

THEMES = {
    "light": {
        "bg": "white",
        "axes": "black",
        "grid": "gray",
        "text": "black",
        "line": "red",
        "slider_bg": "#f2f2f2"
    },
    "dark": {
        "bg": "#121212",
        "axes": "white",
        "grid": "#444444",
        "text": "white",
        "line": "#00ffcc",
        "slider_bg": "#1e1e1e"
    }
}

# ------------------ GRAPH FUNCTIONS ------------------

# ------------------ LINEAR PLOTTER ------------------
def plot_linear(a0, b0, c0, theme="light"):
    colors = THEMES[theme]

    fig = plt.figure(facecolor=colors["bg"])

    # ------------------ GRAPH AREA ------------------
    ax = fig.add_axes([0.1, 0.4, 0.8, 0.55], facecolor=colors["bg"])

    # Initial line
    if a0 != 0:
        x_val = (c0 - b0) / a0
    else:
        x_val = 0

    line = ax.axvline(x=x_val, color=colors["line"], linewidth=2)

    # Axes styling
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.spines['left'].set_color(colors["axes"])
    ax.spines['bottom'].set_color(colors["axes"])
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', colors=colors["text"])

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    ax.grid(True, linestyle="--", alpha=0.5, color=colors["grid"])

    ax.set_title(
        "Interactive Linear Graph",
        fontsize=16,
        color=colors["text"],
        fontweight='bold',
        pad=10
    )

    # ------------------ SLIDER PANEL ------------------
    slider_bg = fig.add_axes([0.1, 0.05, 0.8, 0.25], facecolor=colors["slider_bg"])
    slider_bg.set_xticks([])
    slider_bg.set_yticks([])
    slider_bg.set_navigate(False)

    # Sliders
    ax_a = fig.add_axes([0.2, 0.22, 0.6, 0.03], facecolor=colors["slider_bg"])
    ax_b = fig.add_axes([0.2, 0.16, 0.6, 0.03], facecolor=colors["slider_bg"])
    ax_c = fig.add_axes([0.2, 0.10, 0.6, 0.03], facecolor=colors["slider_bg"])

    ax_a.set_navigate(False)
    ax_b.set_navigate(False)
    ax_c.set_navigate(False)

    s_a = Slider(ax_a, 'a', -50, 50, valinit=a0)
    s_b = Slider(ax_b, 'b', -50, 50, valinit=b0)
    s_c = Slider(ax_c, 'c', -50, 50, valinit=c0)

    if theme == "dark":
        for s in [s_a, s_b, s_c]:
            s.label.set_color("white")
            s.valtext.set_color("white")

    # ------------------ UPDATE ------------------
    def update(val):
        a = s_a.val
        b = s_b.val
        c = s_c.val

        if a == 0:
            line.set_visible(False)
            ax.set_title("a = 0 (invalid)", color='red')
        else:
            x_val = (c - b) / a
            line.set_xdata([x_val, x_val])
            line.set_visible(True)
            ax.set_title(f"x = {round(x_val, 2)}", color=colors["text"])

        fig.canvas.draw_idle()

    s_a.on_changed(update)
    s_b.on_changed(update)
    s_c.on_changed(update)

    plt.show()

# ------------------ QUADRATIC PLOTTER ------------------
def plot_quadratic(a0, b0, c0, theme="light"):
    
    colors = THEMES[theme]
    x = np.linspace(-100, 100, 10000)

    fig = plt.figure(facecolor=colors["bg"])

    # ------------------ GRAPH ------------------
    ax = fig.add_axes([0.1, 0.4, 0.8, 0.55], facecolor=colors["bg"])

    y = a0*x**2 + b0*x + c0
    curve, = ax.plot(x, y, color=colors["line"], linewidth=2)

    # Axes styling
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_color(colors["axes"])
    ax.spines['bottom'].set_color(colors["axes"])
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', colors=colors["text"])
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle="--", alpha=0.5, color=colors["grid"])

    # ------------------ SLIDER PANEL ------------------
    slider_bg = fig.add_axes([0.1, 0.05, 0.8, 0.28], facecolor=colors["slider_bg"])
    slider_bg.set_xticks([])
    slider_bg.set_yticks([])
    slider_bg.set_navigate(False)

    # Sliders for a, b, c
    ax_a = fig.add_axes([0.2, 0.25, 0.6, 0.03], facecolor=colors["slider_bg"])
    ax_b = fig.add_axes([0.2, 0.19, 0.6, 0.03], facecolor=colors["slider_bg"])
    ax_c = fig.add_axes([0.2, 0.13, 0.6, 0.03], facecolor=colors["slider_bg"])

    # Tangent slider
    ax_t = fig.add_axes([0.2, 0.07, 0.6, 0.03], facecolor=colors["slider_bg"])

    for a in (ax_a, ax_b, ax_c, ax_t):
        a.set_navigate(False)

    s_a = Slider(ax_a, 'a', -50, 50, valinit=a0)
    s_b = Slider(ax_b, 'b', -50, 50, valinit=b0)
    s_c = Slider(ax_c, 'c', -50, 50, valinit=c0)
    s_t = Slider(ax_t, 'x (tangent)', -10, 10, valinit=0)

    # Dark mode slider fix
    if theme == "dark":
        for s in (s_a, s_b, s_c, s_t):
            s.label.set_color("white")
            s.valtext.set_color("white")
            s.track.set_color("#555555")
            s.poly.set_color(colors["line"])

    # ------------------ CHECKBOX ------------------
    check_ax = fig.add_axes([0.75, 0.2, 0.15, 0.12], facecolor=colors["slider_bg"])
    check_ax.set_navigate(False)

    check = CheckButtons(check_ax, ["Points", "Tangent"], [True, True])

    if theme == "dark":
        for label in check.labels:
            label.set_color("white")

    # ------------------ EXTRA PLOTS ------------------
    roots_plot, = ax.plot([], [], 'o', color='yellow')
    vertex_plot, = ax.plot([], [], 'o', color='cyan')
    tangent_line, = ax.plot([], [], linestyle='--', color='orange')

    # ------------------ UPDATE ------------------
    def update(val):
        a = s_a.val
        b = s_b.val
        c = s_c.val
        t = s_t.val

        y = a*x**2 + b*x + c
        curve.set_ydata(y)

        show_points, show_tangent = check.get_status()

        # ---- Vertex ----
        if a != 0:
            xv = -b / (2*a)
            yv = a*xv**2 + b*xv + c
        else:
            xv, yv = None, None

        # ---- Roots ----
        D = b**2 - 4*a*c

        if show_points and a != 0:
            vertex_plot.set_data([xv], [yv])

            if D >= 0:
                r1 = (-b + np.sqrt(D)) / (2*a)
                r2 = (-b - np.sqrt(D)) / (2*a)
                roots_plot.set_data([r1, r2], [0, 0])
            else:
                roots_plot.set_data([], [])
        else:
            roots_plot.set_data([], [])
            vertex_plot.set_data([], [])

        # ---- Tangent ----
        if show_tangent:
            m = 2*a*t + b
            yt = a*t**2 + b*t + c

            tangent_y = m*(x - t) + yt
            tangent_line.set_data(x, tangent_y)
        else:
            tangent_line.set_data([], [])

        # Title
        ax.set_title(
            f"y = {round(a,2)}x² + {round(b,2)}x + {round(c,2)}",
            color=colors["text"]
        )

        fig.canvas.draw_idle()

    s_a.on_changed(update)
    s_b.on_changed(update)
    s_c.on_changed(update)
    s_t.on_changed(update)

    plt.show()
    
   

# ------------------ INEQUALITY PLOTTER ------------------
def plot_inequality(a, b, sign, c):
    x = np.linspace(-100, 100, 10000)

    plt.figure()

    ax = plt.gca()

    # Case 1: normal line (b ≠ 0 → y in terms of x)
    if b != 0:
        y = (c - a*x) / b

        # Boundary line
        plt.plot(x, y, color='red', linewidth=2)

        # Shade region
        if sign in ["<", "<="]:
            plt.fill_between(x, y, -100, alpha=0.3)
        else:
            plt.fill_between(x, y, 100, alpha=0.3)

    # Case 2: vertical line (b = 0 → x = constant)
    else:
        x_val = c / a
        plt.axvline(x_val, color='red', linewidth=2)

        if sign in ["<", "<="]:
            plt.fill_betweenx(np.linspace(-100, 100, 10000), -100, x_val, alpha=0.3)
        else:
            plt.fill_betweenx(np.linspace(-100, 100, 10000), x_val, 100, alpha=0.3)

    # Axes styling (same theme)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', colors='black')

    plt.title("Inequality Graph")
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.show()

# ------------------ TWO VARIABLE PLOTTER ------------------
def plot_two_variables(a1, b1, c1, a2, b2, c2):
    x = np.linspace(-100, 100, 10000)

    # Handle lines (avoid division by zero)
    if b1 != 0:
        y1 = (c1 - a1*x) / b1
    else:
        y1 = None

    if b2 != 0:
        y2 = (c2 - a2*x) / b2
    else:
        y2 = None

    plt.figure()

    # Plot first line (red)
    if y1 is not None:
        plt.plot(x, y1, color='red', linewidth=2, label="Equation 1")
    else:
        plt.axvline(c1/a1, color='red', linewidth=2, label="Equation 1")

    # Plot second line (blue)
    if y2 is not None:
        plt.plot(x, y2, color='blue', linewidth=2, label="Equation 2")
    else:
        plt.axvline(c2/a2, color='blue', linewidth=2, label="Equation 2")

    # Axes styling (same as before)
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', colors='black')

    plt.title("System of Equations")
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Intersection point
    determinant = a1*b2 - a2*b1
    if determinant != 0:
        x_int = (c1*b2 - c2*b1)/determinant
        y_int = (a1*c2 - a2*c1)/determinant
        plt.scatter(x_int, y_int, color='black', zorder=5)
        plt.text(x_int, y_int, f" ({round(x_int,2)}, {round(y_int,2)})")

    plt.legend()
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
    theme = input("Choose theme (light/dark): ").lower()
    if theme not in ["light", "dark"]:
      theme = "light"

    plot_linear(a,b,c, theme)



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
        print("Two complex roots")
        root = math.sqrt(-D)
        real_part = -b/(2*a)
        imag_part = root/(2*a)
        print(f"Solution: x1 = {real_part} + {imag_part}i")
        print(f"x2 = {real_part} - {imag_part}i")

    # Vertex
    vx = -b/(2*a)
    vy = a*vx**2 + b*vx + c

    print(f"Vertex = ({vx}, {vy})")
    theme = input("Choose theme (light/dark): ").lower()
    if theme not in ["light", "dark"]:
      theme = "light"

    plot_quadratic(a, b, c, theme)



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
    plot_two_variables(a1, b1, c1, a2, b2, c2)

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

    plot_inequality(a, b, sign, c)


# ------------------ MENU ------------------
def main_menu():
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

main_menu()