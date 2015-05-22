from bcsolver import Solver
import itertools

class Solver_impl(Solver):
	'''Class for greedy solver
	'''
	def __init__(self, _npos, _ndigit, _rep):
		self.npos = _npos
		self.ndigit = _ndigit
		self.rep = _rep
		self.reset()
		self.A = [(i,j) for i in range(self.npos+1) for j in range(self.npos+1-i)]

	def reset(self):
		self.first = True
		digits = ''.join(str(c) for c in range(self.ndigit))
		if self.rep:
			self.S = [''.join(p) for p in itertools.product(digits, repeat = self.npos)]
		else:
			self.S = [''.join(p) for p in itertools.permutations(digits, self.npos)]
		self.called = set(''.join(str(c) for c in range(self.npos)))

	def query(self):
		if self.first:
			self.first = False
			self.q = ''.join(str(c) for c in range(self.npos))
			return self.q
		best_n = len(self.S) + 1
		equiv_class = []
		for q in self.S:
			eq = ''.join(c if c in self.called else '*' for c in q)
			if eq in equiv_class:
				continue
			equiv_class.append(eq)
			subsets = {}
			for ans in self.A:
				subsets[ans] = 0
			for s in self.S:
				subsets[self.answer(q, s)] += 1
			maxs = max(subsets.values())
			if maxs < best_n:
				best_q = q
				best_n = maxs
		self.q = best_q
		self.called = self.called.union(set(''.join(c) for c in self.q))
		return self.q
		
	def update(self, a, b):
		tS = []
		for s in self.S:
			if self.answer(self.q, s) == (a, b):
				tS.append(s)
		self.S = tS

	def answer(self, query, secret):
		'''Compute the answer to the query.
		'''
		a = 0
		b = 0
		for i in range(self.npos):
			if query[i] == secret[i]:
				a += 1
			else:
				for j in range(self.npos):
					if query[i] == secret[j]:
						b += 1
						break
		return (a, b)
