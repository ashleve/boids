import pyglet
from random import randint
import time
import Boid

from pyglet.gl import (
    glPushMatrix, glPopMatrix, glBegin, glEnd, glColor3f,
    glVertex2f, glTranslatef, glRotatef,
    GL_LINE_LOOP, GL_LINES, GL_TRIANGLES)


from pyglet.gl import (
    Config,
    glEnable, glBlendFunc, glLoadIdentity, glClearColor,
    GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_COLOR_BUFFER_BIT)


game_window = pyglet.window.Window(800, 600)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
level_label = pyglet.text.Label(
    text="My Amazing Simulation",
    x=400, y=575,
    anchor_x='center'
)


# image = pyglet.resource.image('pika.jpg')



boids = [Boid.Boid(randint(0, 800), randint(0, 600)) for i in range(100)]
b = Boid.Boid(100, 200)

@game_window.event
def on_draw():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    game_window.clear()
    glLoadIdentity()

    level_label.draw()
    score_label.draw()

    # pyglet.graphics.draw_indexed(2, pyglet.gl.GL_POINTS,
    #                              [0, 1],
    #                              ('v2i', (100, 105, 300, 350)))

    for b in boids:
        b.update()
        b.draw()


def eloelo(dt):
    a = 2
    # print(dt)


if __name__ == '__main__':
    # glEnable(GL_BLEND)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    pyglet.clock.schedule(eloelo)
    pyglet.app.run()

