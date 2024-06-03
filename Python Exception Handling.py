# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:27:44 2024

@author: Loren
"""



# 1. Exceptional Weather Forecast



# def get_temperature():
#     while True:
#         try:
#             temp = float(input("Enter the temperature in Fahrenheit: "))
#             return temp
#         except ValueError:
#             print("Invalid input. Please enter a numerical value for the temperature.")
            
            
# Task 2: Temperature Conversion



# def fahrenheit_to_celsius(fahrenheit):
#     try:
#         celsius = (fahrenheit - 32) * 5 / 9
#         return celsius
#     except (OverflowError, ZeroDivisionError) as e:
#         print(f"An error occurred during the conversion: {e}")
#         return None
    
    
# Task 3: User Experience


# def main():
#     print("Welcome to the Weather Forecast Application!")

#     temperature_fahrenheit = get_temperature()

#     try:
#         temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
#         if temperature_celsius is not None:
#             print(f"The temperature in Celsius is {temperature_celsius:.2f}°C.")
#     else:
#         print("The temperature conversion was successful.")
#     finally:
#         print("Thank you for using the Weather Forecast Application!")

# if __name__ == "__main__":
#     main()





# 2. The Recipe Ratio Adjuster


# def get_servings():
#     while True:
#         try:
#             original_servings = int(input("Enter the number of servings the recipe is originally for: "))
#             desired_servings = int(input("Enter the number of servings you wish to make: "))
#             return original_servings, desired_servings
#         except ValueError:
#             print("Invalid input. Please enter valid numbers for servings.")


# Task 2: 

# def calculate_adjustment_factor(original_servings, desired_servings):
#     try:
#         adjustment_factor = desired_servings / original_servings
#         return adjustment_factor
#     except (ZeroDivisionError, OverflowError) as e:
#         print(f"An error occurred during the calculation: {e}")
#         return None
    
    
# Task 3: 
    
    
# def main():
#     print("Welcome to the Recipe Ratio Adjuster!")

#     original_servings, desired_servings = get_servings()

#     try:
#         adjustment_factor = calculate_adjustment_factor(original_servings, desired_servings)
#         if adjustment_factor is not None:
#             print(f"The adjustment factor for the recipe is {adjustment_factor:.2f}. Adjust your ingredient quantities accordingly.")
#     else:
#         print("The quantity adjustment calculation was successful.")
#     finally:
#         print("Enjoy your cooking!")

# if __name__ == "__main__":
#     main()



