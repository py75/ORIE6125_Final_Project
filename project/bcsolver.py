class Solver:
	def __init__(self):
		self.reset()
	def reset(self):
		raise NotImplementedError()
	def query(self):
		raise NotImplementedError()
	def answer(self, a, b):
		raise NotImplementedError()