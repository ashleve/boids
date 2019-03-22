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

        self.velocity = Point().randomize_dir(2)
        self.acceleration = Point()

        self.size = 6
        self.color = [random.uniform(0,1), 1,random.uniform(0,1)]
        self.max_speed = 2
        self.max_force = 0.02


    def center(self):
        x = self.bounds.x/2
        y = self.bounds.y/2
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



    def update(self, boids):
        self.position += self.velocity
        self.velocity += self.acceleration

        self.acceleration = self.calculate_acc(boids)
        self.acceleration += self.boundaries()
        self.velocity.limit_magnitude(self.max_speed)
        self.edges()




    def calculate_acc(self, boids):
        coh_radius = 100
        sep_radius = 35
        ali_radius = 50


        acc = Point(0,0)
        coh_force = Point(0,0)
        sep_force = Point(0,0)
        ali_force = Point(0,0)

        it_coh = 0
        it_sep = 0
        it_ali = 0

        for b in boids:

            if b == self:
                continue

            dist = b.position.distance(self.position)
            if dist < coh_radius:
                coh_force += b.position
                it_coh += 1
            if dist < sep_radius:
                diff = self.position - b.position
                # diff /= (dist*dist)
                sep_force += diff
                it_sep += 1
            if dist < ali_radius:
                ali_force += b.velocity
                it_ali += 1


        #cohesion
        if it_coh > 0:
            coh_force /= it_coh
            coh_force -= self.position
            coh_force.set_magnitude(self.max_speed)
            coh_force -= self.velocity
            coh_force.limit_magnitude(self.max_force)

        #separation
        if it_sep > 0:
            sep_force.set_magnitude(self.max_speed)
            sep_force -= self.velocity
            sep_force.limit_magnitude(self.max_force)

        #alignment
        if it_ali > 0:
            ali_force.set_magnitude(self.max_speed)
            ali_force -= self.velocity
            ali_force.limit_magnitude(self.max_force)


        acc = coh_force + sep_force + ali_force
        return acc



    def boundaries(self):
        v = Point(0.0,0.0)
        if self.position.x > self.bounds.x - 50:
            v.x = -1
        elif self.position.x < 0 + 50:
            v.x = 1
        if self.position.y > self.bounds.y - 50:
            v.y = -1
        elif self.position.y < 0 + 50:
            v.y = 1
        v.set_magnitude(1.5 * self.max_force)
        return v





    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, 0.0)

        glRotatef(math.degrees(math.atan2(self.velocity.x, self.velocity.y)), 0.0, 0.0, -1.0)

        glBegin(GL_TRIANGLES)
        glColor3f(*self.color)


        glVertex2f(self.size, 0.0)
        glVertex2f(-self.size , 0.0)
        glVertex2f(0.0 , self.size * 3.0)


        glEnd()

        glPopMatrix()


        





