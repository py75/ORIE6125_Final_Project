from bullscows import BullsCows
from solver_hm import Solver_HM

game = BullsCows(4, 10, False)
#print game.secret
solver = Solver_HM(4, 10, False)
steps = game.play(solver)
print "Finished in", steps, "steps."