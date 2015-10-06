input = raw_input("how big do you want your hollow square: ")
output = ""

i = 0

try:
    i = int(input)
except ValueError:
    print("that's not a number")

j = int(i)

for x in range(i):
    for y in range(j):
        if (x == 0) or (y == 0) or (x == (i - 1)) or (y == (j - 1)):
            output += "*"
        else:
            output += " "
    output += "\n"
print(output)

