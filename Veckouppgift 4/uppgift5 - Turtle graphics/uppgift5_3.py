import turtle as t

def move(loops, forward, right_angle):
    for x in range(loops):
        t.forward(forward)
        t.right(right_angle)

def circle(size):
    move(loops=360,forward=size/100.0,right_angle=1)


# Ritar en cirkel
circle(100)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()