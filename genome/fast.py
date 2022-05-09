from cameo import load_model
from cobra.flux_analysis import gapfill
import cobra

model = load_model('./iAF1260.xml')
model.solver = 'gurobi'
model.objective='THRS'

print(model.optimize().objective_value)
print(model.metabolites.get_by_id('thr__L_c'))

with model:
    # model.objective = model.add_boundary(model.metabolites.thr__L_c)
    solution = gapfill(model, iterations=4)
    for reaction in solution[0]:
        print(reaction.id)