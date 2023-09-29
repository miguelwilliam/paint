"""Paint, for drawing shapes.

Exercises

1. Add a color. COMPLETO
2. Complete circle. COMPLETO
3. Complete rectangle. COMPLETO
4. Complete triangle. COMPLETO
5. Add width parameter. COMPLETO
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circulo(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    raio = abs(end.x - start.x) + abs(end.y - start.y)
    circle(raio/2)

    end_fill()


def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()

    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)


def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    #goto(end.x, start.y)
    #goto(((end.x-start.x)/2)+start.x, end.y)
    #goto(start.x, start.y)

    goto(end.x*2-start.x, start.y)
    goto(end.x, end.y)
    goto(start.x, start.y)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: width(1), '1')
onkey(lambda: width(2), '2')
onkey(lambda: width(3), '3')
onkey(lambda: width(4), '4')
onkey(lambda: width(5), '5')
onkey(lambda: width(6), '6')
onkey(lambda: width(7), '7')
onkey(lambda: width(8), '8')
onkey(lambda: width(9), '9')
onkey(lambda: color('black'), 'k')
onkey(lambda: color('white'), 'w')
onkey(lambda: color('green'), 'g')
onkey(lambda: color('blue'), 'b')
onkey(lambda: color('red'), 'r')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
