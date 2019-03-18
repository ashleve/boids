import math
from random import randint


class Point():

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y


	def randomize(self, x_range=100, y_range=100):
		if x_range < 0 or y_range <0:
			raise Exception("Invalid range")
		self.x = randint(0, x_range)
		self.y = randint(0, y_range)


	def __add__(self, vector):		
		return Point(self.x + vector.x, self.y + vector.y)


	def __iadd__(self, vector):
		self.x += vector.x
		self.y += vector.y
		return self


	def __sub__(self, vector):		
		return Point(self.x - vector.x, self.y - vector.y)


	def __isub__(self, vector):
		self.x -= vector.x
		self.y -= vector.y
		return self



	def __truediv__(self, divider):	
		if type(divider) == Point:
			return Point(self.x / divider.x, self.y / divider.y)
		return Point(self.x / divider, self.y / divider)


	# def __itruediv__(self, divider):
	# 	if type(divider) == Point:
	# 		return Point(self.x / divider.x, self.y / divider.y)
	# 	return Point(self.x / divider, self.y / divider)


	def length(self):
		return math.sqrt(self.x**2 + self.y**2)


	def distance(self, vector):
		dist = math.sqrt((self.x - vector.x)**2 + (self.y - vector.y)**2)
		return dist


	def limit(self, value):
		if self.x > value:
			self.x = value
		elif self.x < -value:
			self.x = -value
		if self.y > value:
			self.y = value	
		elif self.y < -value:
			self.y = -value


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



