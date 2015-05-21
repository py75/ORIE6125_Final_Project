from random import randint

class BullsCows:
	def __init__(self, _npos, _ndigit, _rep):
		self.npos = _npos
		self.ndigit = _ndigit
		self.rep = _rep
		sec_tmp = []
		if _rep:
			for i in range(self.npos):
				sec_tmp.append(randint(0, _ndigit - 1))
		else:
			if self.npos > self.ndigit:
				raise Error()
			tmp_rg = range(_ndigit)
			for i in range(self.npos):
				tmp = tmp_rg[randint(0, _ndigit - 1 - i)]
				tmp_rg.remove(tmp)
				sec_tmp.append(tmp)
		self.secret = ''.join(str(c) for c in sec_tmp)

	def play(self, solver):
		solver.reset();
		nsteps = 0
		while True:
			q = solver.query()
			nsteps = nsteps + 1
			(a, b) = self.check(q)
			if a == self.npos:
				return nsteps
			solver.answer(a, b)

	def check(self, query):
		a = 0
		b = 0
		for i in range(self.npos):
			if query[i] == self.secret[i]:
				a = a + 1
			else:
				for j in range(self.npos):
					if query[i] == self.secret[j]:
						b = b + 1
						break
		return (a, b)



