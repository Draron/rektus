from random import *
class Person():
	def __init__(self, heightp0, heightp1, gen):
		self.sex = randint(0, 1)
		self.health = randint(0, 1000)
		self.height = generate_height(heightp0, heightp1, self.sex) 
		self.special = [gen, self.sex, self.height, self.health]
def generate_height(heightp0, heightp1, sex):
	par_s = sex
	par_temp = (heightp0 + heightp1) / 2
	if(par_s == 1):
		par_temp += 50
	else:
		par_temp -= 50
	return par_temp - 80 + randint(0,160)