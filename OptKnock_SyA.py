from cameo import load_model
from cameo.strain_design.deterministic.linear_programming import OptKnock

genome_dict = {
                'iML1515': 'BIOMASS_Ec_iML1515_core_75p37M', 
                'iAF1260': 'BIOMASS_Ec_iAF1260_core_59p81M', 
                'e_coli_core': 'BIOMASS_Ecoli_core_w_GAM', 
                'iJO1366': 'BIOMASS_Ec_iJO1366_WT_53p95M'
                }

genome = 'iAF1260'
objective_id = 'THRS'
biomass="BIOMASS_Ec_iAF1260_core_59p81M"

path = f'../../genome/{genome}.xml'
model = load_model(path)
model.solver = 'gurobi'

wt_solution = model.optimize()
growth = wt_solution.fluxes["BIOMASS_Ec_iAF1260_core_59p81M"]
thr_production = wt_solution.fluxes["THRS"]

optknock = OptKnock(model, fraction_of_optimum=0.1)

# result = optknock.run(max_knockouts=1, target=objective_id, biomass=biomass)
# print(result)

print(optknock)