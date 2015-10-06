input = raw_input("how big do you want the square: ")
x = 0
try:
    x = int(input)
except ValueError:
    print("that's not a number")

y = int(x)

for i in range(x):
    for j in range(y):
        print("x"),
    print("\n"),