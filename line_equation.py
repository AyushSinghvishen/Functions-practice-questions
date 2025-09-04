# line_equation.py

def calculate_y(slope, intercept, x):
    """Calculate y using the line equation y = m*x + b."""
    return slope * x + intercept


def main():
    try:
        slope = float(input("Enter the slope (m): "))
        intercept = float(input("Enter the y-intercept (b): "))
        x = float(input("Enter the value of x: "))

        y = calculate_y(slope, intercept, x)
        print(f"The value of y is: {y}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
