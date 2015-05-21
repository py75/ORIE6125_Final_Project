from bullscows import BullsCows
from solver_hm import Solver_HM

game = BullsCows(4, 10, False)
#print game.secret
solver = Solver_HM()
steps = game.play(solver)
print "Finished in", steps, "steps."