input = raw_input("how big do you want your hollow square: ")
output = ""
x = 0

try:
    x = int(input)
except ValueError:
    print("that's not a number")

y = int(x)

for i in range(x):
    for j in range(x):
        if j == 0:
            for k in range(x):
                output = output + "*",
                output = output + "\n"
        elif j == (x - 1):
            for l in range(x):
                output += "*"
        else:
            for m in range(x):
                output + "x",

