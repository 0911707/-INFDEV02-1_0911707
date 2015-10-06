import math
input = raw_input("what is the radius of the circle? ")
print("\n")

try:
    rad = int(input)
except ValueError:
    print("you did not enter a number")

output = ""
rad = 0

for i in range(-rad, rad + 1):
    for j in range(-rad, rad + 1):
        if float(math.sqrt(i**2 + j**2) >= rad -0.5) and float(math.sqrt(i**2 + j**2) <= rad + 0.5):
            output += "*"
        else:
            output += " "
    output += "\n"
print(output)

