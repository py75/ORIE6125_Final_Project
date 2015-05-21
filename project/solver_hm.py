from bcsolver import Solver

class Solver_HM:
	'''Human solver, for testing.
	'''
	def __init__(self, _npos, _ndigit, _rep):
		self.reset()
	def reset(self):
		pass
	def query(self):
		q = raw_input("Query: ")
		qq = q.strip()
		return qq
	def update(self, a, b):
		print 'Answer:', a, b