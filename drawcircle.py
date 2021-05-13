import math
import turtle


def draw_circle(x, y, r):
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


draw_circle(100,100,50)
turtle.mainloop()