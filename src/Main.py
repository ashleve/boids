import pyglet
from random import randint
import time
from Boid import Boid

from pyglet.gl import (
    glPushMatrix, glPopMatrix, glBegin, glEnd, glColor3f,
    glVertex2f, glTranslatef, glRotatef,
    GL_LINE_LOOP, GL_LINES, GL_TRIANGLES)


from pyglet.gl import (
    Config,
    glEnable, glBlendFunc, glLoadIdentity, glClearColor,
    GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_COLOR_BUFFER_BIT)



score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
level_label = pyglet.text.Label(
    text="My Amazing Simulation",
    x=400, y=575,
    anchor_x='center'
)


# image = pyglet.resource.image('pika.jpg')

bounds = [800, 600]
game_window = pyglet.window.Window(*bounds)

boids = [Boid(bounds) for i in range(100)]


@game_window.event
def on_draw():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    game_window.clear()
    glLoadIdentity()

    level_label.draw()
    score_label.draw()

    for b in boids:
        b.update(boids)
        b.draw()


def eloelo(dt):
    pass

if __name__ == '__main__':
    # glEnable(GL_BLEND)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    pyglet.clock.schedule(eloelo)
    pyglet.app.run()

