import turtle
import random
from spiro import Spiro


class SpiroAnimator:

    def __init__(self, n):
        """
        A class for animating Spirographs

        :param n: counter variable

        """

        self.deltaT = 10                                  # deltaT: Timer value in milliseconds
        self.width = turtle.window_width()
        self.height = turtle.window_height()

        self.spiros = []                                   # creating spiro objects
        for i in range(n):
            r_params = self.gen_random_params()
            spiro = Spiro(*r_params)                       # * converts tuple to list
            self.spiros.append(spiro)

            turtle.ontimer(self.update, self.deltaT)

    def gen_random_params(self):                            # generate random parameters
        width, height = self.width, self.height
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width // 2, width // 2)
        yc = random.randint(-height // 2, height // 2)
        col = (random.random(), random.random(), random.random())

        return (xc, yc, col, R, r, l)

    def restart(self):
        for spiro in self.spiros:
            spiro.clear()
            r_params = self.gen_random_params()
            spiro.setparams(*r_params)
            spiro.restart()

    def update(self):
        num_complete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawing_complete:
                num_complete += 1

        if num_complete == len(self.spiros):
            self.restart()
        turtle.ontimer(self.update, self.deltaT)

    def toggle_turtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()

