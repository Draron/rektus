from random import *
class Person():
	instances = 0

	def __init__(self, heightp0, heightp1, gen):
		self.sex = randint(0, 1)
		self.health = gauss(5000, 3500)					#thx gauss säuglingssterblichkeit is now a thing
		self.height = generate_height(heightp0, heightp1, self.sex) 
		self.special = [gen, self.sex, self.height, self.health]
		Person.instances += 1

	def all_ever():
		return Person.instances

def generate_height(heightp0, heightp1, sex):
	par_s = sex
	par_temp = (heightp0 + heightp1) / 2
	if(par_s == 1):
		par_temp += 50
	else:
		par_temp -= 50
	return par_temp + gauss(0, 53)#- 80 + randint(0, 160)