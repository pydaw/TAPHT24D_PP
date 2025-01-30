import turtle as t

# Upprepa 3 gånger
for x in range(3):
    t.forward(100)
    t.left(120)

# Lyft pennan för att flytta utan att rita
t.penup()
t.forward(200)
t.pendown()
t.dot(10, "red")
t.color("blue")
t.forward(50)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()