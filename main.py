import turtle
from datetime import datetime
from PIL import Image
import argparse
from spiro import Spiro
from spiro_animator import SpiroAnimator


def save_drawing():
    turtle.hideturtle()
    date_str = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    filename = 'spiro-' + date_str
    print('saving drawing to {0}.eps/png'.format(filename))
    canvas = turtle.getcanvas()

    canvas.postscript(file = filename + '.eps')
    img = Image.open(filename + '.eps')
    img.save(filename + '.png', 'PNG')
    turtle.showturtle()


def main():
    desc_str = """"
    This program creates Spirographs using the Turtle module.
    When run with no arguments, this program draws random Spirographs.
    
    Terminology:
    
    R: Radius of outer circle
    r: Radius of inner circle
    l: Ratio of hole distance to r
    """
    parser = argparse.ArgumentParser(description=desc_str)
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
                        help="The three arguments in sparams: R, r, l.")

    args = parser.parse_args()

    turtle.setup(width=0.8)
    turtle.shape('turtle')
    turtle.title("Sprirographs!")
    turtle.onkey(save_drawing, "s")
    turtle.listen()

    turtle.hideturtle()

    if args.sparams:
        params = [float(x) for x in args.sparams]
        col = [0.0, 0.0, 0.0]
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()

    else:
        spiro_anim = SpiroAnimator(4)
        turtle.onkey(spiro_anim.toggle_turtles, 't')
        turtle.onkey(spiro_anim.restart, 'r')

    turtle.mainloop()


if __name__ == '__main__':
    main()
