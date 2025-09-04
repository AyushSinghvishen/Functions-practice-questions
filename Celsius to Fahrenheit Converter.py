# celsius_to_fahrenheit.py

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit.

    Formula: (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32


def main():
    print("🌡️ Celsius to Fahrenheit Converter 🌡️")
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")


if __name__ == "__main__":
    main()
