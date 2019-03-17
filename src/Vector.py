import math
from random import randint


class Vector2d():

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y


	def randomize(self, x_range=100, y_range=100):
		if x_range < 0 or y_range <0:
			raise Exception("Invalid range")
		self.x = randint(0, x_range)
		self.y = randint(0, y_range)


	def __add__(self, vector):
		return Vector2d(self.x + vector.x, self.y + vector.y)


	def __iadd__(self, vector):
		self.x += vector.x
		self.y += vector.y
		return self


	def length(self):
		return math.sqrt(self.x**2 + self.y**2)


	def distance(self, vector):
		dist = sqrt((self.x - vector.x)**2 + (self.y - vector.y)**2)
		return dist


	def __getitem__(self, key):
		if key == 0:
			return self.x
		elif key == 1:
			return self.y
		else:
			raise Exception("Invalid vector index")


	def __setitem__(self, key, value):
		if key == 0:
			self.x = value
		elif key == 1:
			self.y = value
		else:
			raise Exception("Invalid vector index")		


	def __str__(self):
		return "({}, {})".format(self.x, self.y)



