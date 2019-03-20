from Vector import Point
import random
import math

from pyglet.gl import (
    glPushMatrix, glPopMatrix, glBegin, glEnd, glColor3f,
    glVertex2f, glTranslatef, glRotatef,
    GL_LINE_LOOP, GL_LINES, GL_TRIANGLES, GL_POLYGON)


from pyglet.gl import (
    Config,
    glEnable, glBlendFunc, glLoadIdentity, glClearColor,
    GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_COLOR_BUFFER_BIT)



class Boid():

    def __init__(self, bounds):
        self.bounds = Point(*bounds)
        # self.position = self.center()
        # self.position = self.center() + Point().randomize_dir(400)
        self.position = Point().randomize(*bounds)

        self.velocity = Point().randomize_dir(3)
        self.acceleration = Point()

        self.size = 5
        self.color = [random.uniform(0,1), 1,random.uniform(0,1)]
        self.max_speed = 3


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

        steering = avg - self.velocity
        return steering


    def cohesion(self, boids):
        perception_radius = 100
        neighbours = self.find_neighbours(boids, perception_radius)
        avg = Point()

        if len(neighbours) == 0:
            return avg

        for b in neighbours:
            avg += b.position
        avg /= len(neighbours)

        steering = avg - self.position
        return steering
      



    def update(self, boids):
        self.position += self.velocity
        self.velocity += self.acceleration
        self.acceleration = self.cohesion(boids) + self.alignment(boids)
        self.acceleration.set_magnitude(0.3)
        self.velocity.set_magnitude(self.max_speed)
        self.edges()







    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, 0.0)

        glRotatef(math.degrees(math.atan2(self.velocity.x, self.velocity.y)), 0.0, 0.0, -1.0)

        glBegin(GL_POLYGON)
        glColor3f(*self.color)


        glVertex2f(self.size, 0.0)
        glVertex2f(-self.size , 0.0)
        glVertex2f(0.0 , self.size * 3.0)


        glEnd()

        glPopMatrix()


        





