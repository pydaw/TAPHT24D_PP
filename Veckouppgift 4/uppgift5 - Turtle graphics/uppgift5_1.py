import turtle as t

# funktion som ritar en kvadrat, default längd på sida är 100px
def sqare(side=100):
    for i in range(4):
        t.forward(side)
        t.left(90)


# Ritar en kvadrat med en sida på 100px
sqare(100)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()