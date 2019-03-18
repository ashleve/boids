from Vector import Point
import random
from math import sqrt, sin, cos

from pyglet.gl import (
    glPushMatrix, glPopMatrix, glBegin, glEnd, glColor3f,
    glVertex2f, glTranslatef, glRotatef,
    GL_LINE_LOOP, GL_LINES, GL_TRIANGLES)


from pyglet.gl import (
    Config,
    glEnable, glBlendFunc, glLoadIdentity, glClearColor,
    GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_COLOR_BUFFER_BIT)



class Boid():

    def __init__(self, bounds):
        self.bounds = Point(*bounds)
        self.position = self.center() + self.rand_vec(200) + self.rand_vec(100) + self.rand_vec(50) 
        # self.position = self.center()

        self.velocity = self.rand_vec(3)
        # self.acceleration = self.rand_vec(length=0.1)
        self.acceleration = Point()

        self.size = 5
        self.color = [1.0, 1.0, 1.0]


    def center(self):
        x = self.bounds.x/2
        y = self.bounds.y/2
        return Point(x,y)


    def find_neighbours(self, boids, radius):
        neighbours = []
        for b in boids:
            if b != self:
                dist = b.position.distance(self.position)
                if dist <= radius:
                    neighbours.append(b)
        return neighbours


    def rand_vec(self, length):
        a = random.uniform(0, 2*3.1415)
        x = length*sin(a)
        y = length*cos(a)
        return Point(x,y)


    def edges(self):
        if self.position.x > self.bounds.x:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.bounds.x
        if self.position.y > self.bounds.y:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.bounds.y


    def alignment(self, boids):
        perception_radius = 50
        neighbours = self.find_neighbours(boids, perception_radius)
        avg = Point()

        if len(neighbours) == 0:
            return avg

        for b in neighbours:
            avg += b.velocity
        avg /= len(neighbours)

        return avg - self.velocity



    def update(self, boids):
        self.position += self.velocity
        self.velocity += self.acceleration
        self.acceleration = self.alignment(boids)
        self.acceleration.limit(0.1)
        self.velocity.limit(3)
        self.edges()







    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, 0.0)

        glRotatef(self.velocity[0], 0.0, 0.0, -1.0)
        # glRotatef(math.degrees(math.atan2(self.velocity[0], self.velocity[1])), 0.0, 0.0, -1.0)

        glBegin(GL_TRIANGLES)
        # glColor3f(*self.color)

        glVertex2f(-self.size, 0.0)
        glVertex2f(self.size, 0.0)
        glVertex2f(0.0, self.size * 3.0)


        glEnd()

        glPopMatrix()


        





