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




# image = pyglet.resource.image('pika.jpg')

bounds = [1200, 600]
game_window = pyglet.window.Window(*bounds)

score_label = pyglet.text.Label(
    text="Score: 0", 
    x=10, y=575
)
level_label = pyglet.text.Label(
    text="My Amazing Simulation",
    x=bounds[0]/2, y=bounds[1]-25,
    anchor_x='center'
)


boids = [Boid(bounds) for i in range(150)]


@game_window.event
def on_draw():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    game_window.clear()
    glLoadIdentity()

    level_label.draw()
    score_label.draw()

    for b in boids:
        b.draw()


def update(dt):
    for b in boids:
        b.update(boids)


if __name__ == '__main__':
    # glEnable(GL_BLEND)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    pyglet.clock.schedule(update)
    pyglet.app.run()
