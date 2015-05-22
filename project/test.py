from bullscows import BullsCows
from solver_impl import Solver_impl

maxn = 0
for i in range(10):
	print i
	game = BullsCows(4, 10, False)
	print game.secret
	solver = Solver_impl(4, 10, False)
	steps = game.play(solver)
	if steps > maxn:
		maxn = steps
		maxs = game.secret
	print "Finished in", steps, "steps.\n"
print maxs
print maxn, 'steps.'