class Solver:
	'''Base class for solver
	'''
	def __init__(self, _npos, _ndigit, _rep):
		self.npos = _npos
		self.ndigit = _ndigit
		self.rep = _rep
		self.reset()
	def reset(self):
		raise NotImplementedError()
	def query(self):
		raise NotImplementedError()
	def update(self, a, b):
		raise NotImplementedError()