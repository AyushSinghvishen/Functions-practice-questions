# lift_rounds.py

def calculate_rounds(n, capacity):
    """Return the number of rounds the lift must make."""
    rounds = n // capacity   # full rounds
    if n % capacity != 0:    # extra round if remainder
        rounds += 1
    return rounds


def main():
    try:
        n = int(input("Enter total number of people: "))
        capacity = int(input("Enter lift capacity: "))

        if n <= 0 or capacity <= 0:
            print("Both n and capacity must be positive integers.")
        else:
            rounds = calculate_rounds(n, capacity)
            print(f"The lift needs {rounds} rounds.")
    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()
