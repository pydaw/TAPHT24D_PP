import turtle as t

def get_mid(p1, p2):
    return ((p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2)

def draw_triangle(t, vertices, color):
    t.fillcolor(color)
    t.up()
    t.goto(vertices[0][0], vertices[0][1])
    t.down()
    t.begin_fill()
    t.goto(vertices[1][0], vertices[1][1])
    t.goto(vertices[2][0], vertices[2][1])
    t.goto(vertices[0][0], vertices[0][1])
    t.end_fill()

def draw_sierpinski(t, vertices, depth):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    color = depth % len(colormap)
    draw_triangle(t, vertices, colormap[color])
    if depth > 0:
        draw_sierpinski(t, [vertices[0],
                            get_mid(vertices[0], vertices[1]),
                            get_mid(vertices[0], vertices[2])],
                       depth - 1)
        draw_sierpinski(t, [vertices[1],
                            get_mid(vertices[0], vertices[1]),
                            get_mid(vertices[1], vertices[2])],
                       depth - 1)
        draw_sierpinski(t, [vertices[2],
                            get_mid(vertices[2], vertices[1]),
                            get_mid(vertices[0], vertices[2])],
                       depth - 1)


# Set up the drawing canvas
t.setup(800, 600)
window = t.Screen()
window.bgcolor("white")
window.title("Sierpinski Triangle")

# Creating the Turtle to draw the triangle
sierpinski = t.Turtle()
sierpinski.speed('fastest')

points = [[-200, -100], [0, 200], [200, -100]]  # Define the main triangle points
draw_sierpinski(sierpinski, points, 5)  # Change the depth as needed

t.done()
