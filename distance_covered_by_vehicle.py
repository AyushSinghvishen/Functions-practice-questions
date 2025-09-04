# distance_covered.py

def calculate_distance(speed, time):
    """Return the distance covered given speed and time."""
    return speed * time


def main():
    try:
        speed = float(input("Enter the speed of the vehicle (km/h): "))
        time = float(input("Enter the time traveled (hours): "))

        if speed < 0 or time < 0:
            print("Speed and time must be non-negative values.")
        else:
            distance = calculate_distance(speed, time)
            print(f"The vehicle covered {distance} km.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
