from solver_impl import Solver_impl
import unittest

class TestImpl(unittest.TestCase):
	def test_init(self):
		solver = Solver_impl(4, 10, False)
		self.assertEqual(len(solver.A), 15)

	def test_reset(self):
		solver1 = Solver_impl(4, 10, False)
		self.assertEqual(len(solver1.S), 5040)

		solver2 = Solver_impl(5, 6, True)
		self.assertEqual(len(solver2.S), 6**5)

	def test_answer(self):
		solver1 = Solver_impl(4, 10, False)
		self.assertEqual(solver.answer('1407', '2417'), (2,1))

		solver2 = Solver_impl(5, 6, True)
		self.assertEqual(solver.answer('1207', '1102'), (1,2))

	def test_update(self):
		S1 = Set['1203', '2473', '9874']
		solver1 = Solver_impl(4, 10, False)
		solver1.q = '1207'
		self.assertEqual(solver1.update(3,0),['1203'])

		S2 = Set['1102', '2304', '1722']
		solver2 = Solver_impl(5, 6, True)
		solver2.q = '2204'
		self.assertEqual(solver2.update(3,0),['2304'])
	
if __name__ == '__main__':
	unittest.main()
