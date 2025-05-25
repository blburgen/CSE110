# Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V**0.16) + 0.4275T(V**0.16)
# Where,T= Air Temperature (ºF) V= Wind Speed (mph)

"""
Your assignment is to write a program that asks the user for a temperature and then shows the wind chill 
values for various wind speeds at that temperature.

Your program should compute and display the wind chill for wind speeds of 5, 10, 15, ..., 60 miles per 
hour, just like the National Weather Service chart does. To help users who are more familiar with Celsius, 
your program should allow temperature to be entered in either Celsius or Fahrenheit, and if needed, convert 
the Celsius temperature to Fahrenheit before using the formula.

The following are the required components of this assignment:

Write a function to calculate and return the wind chill based on a given temperature and wind speed.

Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the 
Celsius temperature by (9/5) and then add 32.

Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert 
it to Fahrenheit before using the formula above.

Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind 
chill for each of these wind speeds.

Display the wind chill value to 2 decimals of precision.

"""

def wind_chill(temperature, wind_speed):
    return 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed**0.16)) + (0.4275 * temperature * (wind_speed**0.16))

def C_to_F(temperature):
    return temperature * (9 / 5) + 32

def F_to_C(temperature):
    return (temperature - 32) * (5 / 9)

wind_speed = 5
temperature = float(input("\nWhat is the temperature? "))
F_or_C = input("Fahrenheit or Celsius (F/C)? ").lower()

if F_or_C[0] == "f":
    while wind_speed <= 60:
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed:<2} mph, the windchill is: {wind_chill(temperature,wind_speed):.2f}F")
        wind_speed += 5
        
if F_or_C[0] == "c":
    temperature = temperature * (9 / 5) + 32
    while wind_speed <= 60:
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed:<2} mph, the windchill is: {wind_chill(temperature,wind_speed):.2f}F or {F_to_C(wind_chill(temperature,wind_speed)):.2f}C")
        wind_speed += 5
