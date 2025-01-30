import turtle as t
import math

__version__ = 2

if __version__ == 1:
    t.write('PYTHON' , font=('Arial', 35, 'normal'))

    # Låt fönstret stanna kvar tills användaren stänger det
    t.mainloop()

elif __version__ == 2:
    def calc_angle_distance(a,b):
        return math.sqrt(a**2+b**2)

    def calc_angle(angle_distance, x_offset):
        return math.degrees(math.asin(x_offset/angle_distance))
    


    # funktion som ritar bokstaven "P"
    def letter_p():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        t.right(90)
        t.forward(20)
        t.circle(-50,180)
        t.forward(20)
    

    # funktion som ritar bokstaven "Y"
    def letter_y():
        t.setheading(0)
        t.left(90)
        height = 170
        t.forward(height*0.6)
        angle_distance = calc_angle_distance(height-height*0.6,height/3)
        angle = calc_angle(angle_distance, height/3)
        t.left(angle)
        t.forward(angle_distance)
        t.penup()
        t.backward(angle_distance)
        t.pendown()
        t.right(angle*2)
        t.forward(angle_distance)


    # funktion som ritar bokstaven "T"
    def letter_t():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        t.left(90)
        t.forward(60)
        t.left(180)
        t.forward(120)
        

    # funktion som ritar bokstaven "H"
    def letter_h():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        t.penup()
        t.backward(85)
        t.pendown()
        t.right(90)
        t.forward(85)
        t.left(90)
        t.penup()
        t.forward(85)        
        t.pendown()
        t.right(180)
        t.forward(170)


    # funktion som ritar bokstaven "O"
    def letter_o():
        t.setheading(0)
        t.left(180)
        t.circle(-50,90)
        t.forward(70)
        t.circle(-50,180)
        t.forward(70)     
        t.circle(-50,90)


    # funktion som ritar bokstaven "N"
    def letter_n():
        t.setheading(0)
        t.left(90)
        t.forward(170)
        angle_distance = calc_angle_distance(170,85)
        angle = calc_angle(angle_distance, 85)
        t.right(180-angle)
        t.forward(angle_distance)
        t.left(180-angle)
        t.forward(170)

    
    # funktion som flyttar pennan lämplig punkt, utan att rita
    def bring_to_point(x=-400, y=0, x_offset=0, y_offset=0):
        t.penup()
        t.setheading(0)
        t.setpos(x + x_offset, y + y_offset)
        t.pendown()
        
    
    t.speed('fastest')
    bring_to_point()
    letter_p()
    bring_to_point(x_offset=120)
    letter_y()
    bring_to_point(x_offset=250)
    letter_t()
    bring_to_point(x_offset=320)
    letter_h()
    bring_to_point(x_offset=468)
    letter_o()
    bring_to_point(x_offset=530)
    letter_n()
    

    # Låt fönstret stanna kvar tills användaren stänger det
    t.mainloop()