from bcsolver import Solver

class Solver_HM:
	def __init__(self):
		self.reset()
	def reset(self):
		pass
	def query(self):
		q = raw_input("Query: ")
		qq = q.strip()
		return qq
	def answer(self, a, b):
		print 'Answer:', a, b