user_input=input("Provide a Celsius temperature, and will convert to Fahrenheit\n")

new_temp = (float(user_input) * 1.8) + 32

print(f"The equivalent of {user_input} degrees Celsius is {new_temp:.1f} degrees Fahrenheit.")

# change line #8 to cause conflict #
print("Unfortunatly, I can't convert back. Math is hard.")
print(f"Extra line to cause trouble :)")
print("One more time.")
print(user_intput+42)
