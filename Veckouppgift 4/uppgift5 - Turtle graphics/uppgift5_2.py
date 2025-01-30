import turtle as t

# funktion som ritar en kvadrat
def square(side=50):
    for i in range(4):
        t.forward(side)
        t.left(90)

# funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita
def move_next(distance=100):
    t.penup()
    t.forward(distance)
    t.pendown()


# Ritar 5 kvadrater 
for x in range(5):
    square()
    move_next()

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()