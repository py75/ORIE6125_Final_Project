from bullscows import BullsCows
import unittest

class TestBullsCows(unittest.TestCase):
	def test_init(self):
		bc1 = BullsCows(4, 10, False)
		temp = True
		digits = ''.join(str(c) for c in range(10))
		s = set(digits)
		if len(bc1.secret) != 4:
		    temp = False
		else:
			for i in range(4):
				if bc1.secret[i] not in s:
					temp = False
					break
				else:
					secret.difference(bc1.secret[i])
		self.assertEqual(temp, True)

		bc2 = BullsCows(5, 6, True)
		temp = True
		digits = ''.join(str(c) for c in range(6))
		s = set(digits)
		if len(bc2.secret) != 5:
		    temp = False
		else:
			for i in range(5):
				if bc2.secret[i] not in s:
					temp = False
		self.assertEqual(temp,True)

	def test_ans(self):
		bc1 = BullsCows(4, 10, False, '2417')
		self.assertEqual(bc1.answer('1407'), (2, 1))
		
		bc2 = BullsCows(5, 6, True, '1102')
		self.assertEqual(bc2.answer('1027'), (1, 2))

if __name__ == '__main__':
	unittest.main()
