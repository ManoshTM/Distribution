# Probability distribution functions
# Manosh T Manohharan
# Department of Physics and Centre for Particle Physics
# CUSAT, India. 
# Start date: 14 Jan, 2020.

import numpy as np
import math

# START
# Binomial distribution
class Binomial:
	def __init__(self,RandomVariable,Trial,Success):
		self.n = RandomVariable
		self.N = Trial
		self.p = Success
	def Binomial_PDF(self):
		f_n = (math.factorial(self.N)/(math.factorial(self.n)*math.factorial(self.N-self.n)))*(self.p**(self.n))*(1-self.p)**(self.N-self.n)
		return f_n
# END

# START
# Trinomial distribution
class Trinomial:
	def __init__(self,RandomVariable1,RandomVariable2,Trial,Success1,Success2):
		self.n1 = RandomVariable1
		self.n2 = RandomVariable2
		self.N = Trial
		self.p1 = Success1
		self.p2 = Success2
	def Trinomial_PDF(self):
		f_n = (math.factorial(self.N)/(math.factorial(self.n1)*math.factorial(self.n2)*math.factorial(self.N-(self.n1+self.n2))))*(self.p1**self.n1)*(self.p2**self.n2)*((1-(self.p1+self.p2))**(self.N-(self.n1+self.n2)))
		return f_n
# END

# START
# Chi Square distribution
class ChiSquare:
	def __init__(self,RandomVariable,DegreesOfFreedom):
		self.z = RandomVariable
		self.n = DegreesOfFreedom
	def ChiSquare_PDF(self):
		f_n = (1/((2**(self.n/2))*math.gamma(self.n/2)))*self.z**((self.n/2)-1)*np.exp(-1*self.z/2)
		return f_n
# END

# START
# Exponential distru=ibution
class Exponential:
	def __init__(self,RandomVariable,Parameter):
		self.x = RandomVariable
		self.e = Parameter
	def Exponential_PDF(self):
		f_n = (1/self.e)*np.exp(-1*self.x/self.e)
		return f_n
# END
