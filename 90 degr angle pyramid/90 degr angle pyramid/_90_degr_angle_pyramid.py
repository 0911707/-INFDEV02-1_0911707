input = raw_input("how many layers does the triangle need to have? ")
x = 0
output = ""

counter = 1
try:
    x = int(input)
except ValueError:
    print("you did not enter a number!")

x = abs(x)

for i in range(x):
    for j in range(counter):
         output += "*"   
    output += "\n"
    if counter <= x:        #this increases the for j ... loop by one which ads an extra *
        counter += 1

print (output)

