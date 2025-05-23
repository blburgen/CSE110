# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
import math

print("\nWelcome to the velocity calculator. Please enter the following.\n")

mass_in_kg = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time_in_seconds = float(input("Time (in seconds): "))
density_of_fluid = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_sectional_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

value_c = (1 / 2) * density_of_fluid * cross_sectional_area * drag_constant
velocity_at_time = math.sqrt(mass_in_kg * gravity / value_c) * (1 - math.exp(-math.sqrt(mass_in_kg * gravity * value_c) / mass_in_kg * time_in_seconds))

print(f"\nThe inner value of c is: {value_c: .3f}")
print(f"The velocity after {time_in_seconds: .1f} seconds is: {velocity_at_time: .3f} m/s\n")