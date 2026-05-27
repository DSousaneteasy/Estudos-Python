import sys
try:
    ##raise ValueError
    print("Raising an Exception.")
except ValueError:
    print("ValueError Exception!")
    sys.exit()
finally:
    print("Talking care of last minute details.")

print("This code will never execute.")
