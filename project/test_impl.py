from solver_impl import Solver_impl
import unittest
from unittest import mock

class TestImpl(unittest.TestCase):
	def test_init(self):

	def test_reset(self):

	def test_update(self):


	def test_answer(self):
		secret = mock.MagicMock(return_vale = '2417')
		self.assertEqual(Solver_impl.answer(secret,'1407'), (2,1))
