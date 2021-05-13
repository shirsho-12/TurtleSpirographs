import turtle
import math


class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
        """
        :param xc:  x-distance of centre of inner circle
        :param yc:  y-distance of centre of inner circle
        :param col: Color of the turtle pen
        :param R: Radius of larger outer circle
        :param r: Radius of smaller inner circle
        :param l: Distance of pen tip from centre of small circle

        """
        
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5                               # step width in angles. Lower the step, finer the image
        self.drawing_complete = False

        self.setparams(xc, yc, col, R, r, l)

        self.restart()

    def setparams(self, xc, yc, col, R, r, l):      # setting the parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        gcd_val = math.gcd(self.r, self.R)
        self.num_rotations = self.r // gcd_val
        self.k = r / float(R)
        self.t.color(*col)

        self.a = 0                                  # initial angle = 0

    def restart(self):
        self.drawing_complete = False
        self.t.showturtle()
        self.t.up()
        a = 0.0
        self.calc(a)
        self.t.down()

    def calc(self, a):
        R, k, l = self.R, self.k, self.l
        x = R * ((1 - k) * math.cos(a) + 1 * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - 1 * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)

    def draw(self):
        for i in range(0, 360 * self.num_rotations + 1, self.step):
            a = math.radians(i)
            self.calc(a)
        self.t.hideturtle()

    def update(self):                                # Individual iteration turtle movement
        if self.drawing_complete:
            return
        self.a  += self.step
        a = math.radians(self.a)
        self.calc(a)

        if self.a >= 360 * self.num_rotations:
            self.drawing_complete == True
            self.t.hideturtle()

    def clear(self):
        self.t.clear()