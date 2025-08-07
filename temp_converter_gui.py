def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Converts Celsius to Kelvin."""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """Converts Fahrenheit to Kelvin."""
    return (fahrenheit_to_celsius(fahrenheit)) + 273.15

def kelvin_to_celsius(kelvin):
    """Converts Kelvin to Celsius."""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Converts Kelvin to Fahrenheit."""
    return (kelvin_to_celsius(kelvin) * 9/5) + 32

def main():
    """Main function to run the user-driven temperature conversion program."""
    print("--- Temperature Converter ---")
    print("You can convert between Celsius, Fahrenheit, and Kelvin.")

    while True:
        print("\nWhich unit do you want to convert FROM?")
        print("1. Celsius (C)")
        print("2. Fahrenheit (F)")
        print("3. Kelvin (K)")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '4':
            print("Exiting the program. Goodbye!")
            break

        try:
            temp_value_str = input("Enter the temperature value: ").strip()
            temp_value = float(temp_value_str)
        except ValueError:
            print("Invalid temperature value. Please enter a number.")
            continue # Go back to the start of the loop

        if choice == '1': # Convert FROM Celsius
            print(f"\n--- Converting {temp_value:.2f}°C ---")
            print(f"Fahrenheit: {celsius_to_fahrenheit(temp_value):.2f}°F")
            print(f"Kelvin:     {celsius_to_kelvin(temp_value):.2f}K")
        elif choice == '2': # Convert FROM Fahrenheit
            print(f"\n--- Converting {temp_value:.2f}°F ---")
            print(f"Celsius: {fahrenheit_to_celsius(temp_value):.2f}°C")
            print(f"Kelvin:  {fahrenheit_to_kelvin(temp_value):.2f}K")
        elif choice == '3': # Convert FROM Kelvin
            print(f"\n--- Converting {temp_value:.2f}K ---")
            print(f"Celsius:   {kelvin_to_celsius(temp_value):.2f}°C")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(temp_value):.2f}°F")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()