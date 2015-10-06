input = raw_input("how many layers does the pyramid need to have? ")
x = 0
output = ""

try:
    x = int(input)
except ValueError:
    print("you did not enter a number!")

counter = x
xcount = 1

for i in range(x):
    for j in range(counter):
        output += " "
    for k in range(xcount):
        output += "*"
    output += "\n"
    
    if counter >= 0:
        counter -= 1
    if xcount <= x + x:
        xcount += 2

print(output)
