#takes in a number representing the temperature in Celsius and returns the temperature in Fahrenheit. 
#function that does the opposite (Fahrenheit to Celsius)
def to_fahrenheit(temp):
    fahrenheit = (temp * (9 / 5)) + 32
    return fahrenheit

def to_celsius(temp):
        celsius = (temp - 32) * (5 / 9)
        return celsius
