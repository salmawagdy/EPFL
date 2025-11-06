convert = True

def to_liters(gallons):
    return gallons * 3.78541

def to_miles(meters):
    return meters * 0.000621371

def to_celsius(fer):
    return (fer - 32) * 5 / 9

while convert:
    user_input = input("Do you want to convert? (yes/no): ").lower()

    if user_input == "no":
        convert = False
        print("Goodbye!")
        break

    if user_input == "yes":
        converter_type = input("Choose converter: liters, miles, or celsius: ").lower()
        value = float(input("Please enter the value: "))

        if converter_type == "liters":
            print(str(value) + " gallons = " + str(to_liters(value)) + " liters")
        elif converter_type == "miles":
            print(str(value) + " meters = " + str(to_miles(value)) + " miles")
        elif converter_type == "celsius":
            print(str(value) + "F = " + str(to_celsius(value)) + "C")
        else:
            print("Converter not supported")
