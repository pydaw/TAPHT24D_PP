
print("----- 1 -----")
limit = 15
index = 5

while index <= limit:
    print(index)
    index = index + 2


print("----- 2 -----")
for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
    i = i + 1


print("----- 3 -----")
counter = 0
for i in range(6):
    counter += i
print(counter)


print("----- 4 -----")
x = 0
y = 1
while y < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y
    y += 1
    print(f"x: {x}, y: {y}")


print("----- 5 -----")
message = "its_time_to_get_coding"
print(message[3:7])

print(f"detta funkar bättre: {message[4:8]}")


print("----- 6 -----")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y + 1: #<--ändrat detta så kommer den att rita ut strecket ett steg åt höger
            s += "#"
        else:
            s += "."
    print(s)