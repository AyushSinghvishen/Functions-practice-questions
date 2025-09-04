# area_of_rectangle.py

def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width


def main():
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers.")
        else:
            area = calculate_area(length, width)
            print(f"The area of the rectangle is: {area}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
