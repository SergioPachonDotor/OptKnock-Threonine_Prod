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

path = f'./genome/{genome}.xml'
dest_path = f'./genome/E_coli_yaml/'
model = load_model(path)
model.solver = 'gurobi'

wt_solution = model.optimize()
growth = wt_solution.fluxes["BIOMASS_Ec_iAF1260_core_59p81M"]
thr_production = wt_solution.fluxes["THRS"]

optknock = OptKnock(model, fraction_of_optimum=0.1)

knock_outs = 2
results = [optknock.run(max_knockouts=i, target=objective_id, biomass=biomass) for i in range(1, knock_outs + 1)]

[results[i].data_frame.to_csv(f'./results/iAF1260_core_59p81M_THRS_{i + 1}_knockouts.csv') for i in range(knock_outs)]