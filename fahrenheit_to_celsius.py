"""
Ex 6. Create a Python script called fahrenheit_to_celsius.py

The script should declare a variable called fahrenheit.
The script should then convert the value of fahrenheit to celsius.
The conversion should be displayed on the screeen in the following format: "32 degrees fahrenheit is equal to 0.0 degree(s) celsius"
"""


Fahrenheit =int(input("Enter temperature in fahrenheit "))

Celsius = (Fahrenheit - 32)*5/9

print(Fahrenheit, "degree(s) fahrenheit is equal to ", Celsius, "degree(s) celsius" )
