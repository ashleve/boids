from Vector import Vector2d
from pyglet.gl import (
    glPushMatrix, glPopMatrix, glBegin, glEnd, glColor3f,
    glVertex2f, glTranslatef, glRotatef,
    GL_LINE_LOOP, GL_LINES, GL_TRIANGLES)


from pyglet.gl import (
    Config,
    glEnable, glBlendFunc, glLoadIdentity, glClearColor,
    GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_COLOR_BUFFER_BIT)



class Boid():

    def __init__(self, x, y):
        self.position = Vector2d(x,y)
        self.velocity = [2.0, 2.0]
        self.acceleration = [0.0, 0.0]
        self.size = 5
        self.color = [1.0, 1.0, 1.0]
        self.bounds = [800, 600]


    def find_neighbours(self, boids, radius):
        neighbours = []
        for b in boids:
            dist = b.distance(position)
            if dist <= radius:
                neighbours.append(b)
        return neighbours


    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, 0.0)

        glRotatef(self.velocity[0], 0.0, 0.0, -1.0)
        # glRotatef(math.degrees(math.atan2(self.velocity[0], self.velocity[1])), 0.0, 0.0, -1.0)

        glBegin(GL_TRIANGLES)
        glColor3f(*self.color)

        glVertex2f(-self.size, 0.0)
        glVertex2f(self.size, 0.0)
        glVertex2f(0.0, self.size * 3.0)


        glEnd()

        glPopMatrix()


    def update(self):
        self.position += Vector2d(1,1)
        self.velocity[0] += 3
        self.velocity[1] += 0.1





