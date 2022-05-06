# For using this module, you have to create a virtual environment.
# Once created, you run the following command:
# pip install git+https://github.com/zhanglab/psamm-import.git
# 
# Or you can follow this tutorial (useful for further information):
# https://psamm.readthedocs.io/en/latest/index.html
#
# If attribute error due to fractions has no attribute "gcd", then modify the file
# fractions.py importing gcd as follows:
# from math import gcd
#
# Author: Sergio Pachón Dotor 
# Github: https://github.com/SergioPachonDotor

import os
import cobra
import cobra.test
from cobra.flux_analysis import gapfill

def import_existing_model(ex_model_path='E_coli_sbml/ecoli_core_model.xml', destination_path='./genome/E_coli_yaml/'):
    os.system(f'psamm-import sbml --source {ex_model_path} --dest {destination_path}')


def gapfind_and_gapcheck(solver='gurobi', model_path='./genome/E_coli_yaml/', deep_check=False, results_path='../../results/', file_name='gapcheck', file_extension='txt'):
    
    os.chdir(model_path)

    if deep_check == True:
        os.system(f'psamm-model gapcheck --method prodcheck --solver name={solver} > {results_path}{file_name}_prodcheck.{file_extension}', objective= 'thr__L_c')
        os.system(f'psamm-model gapcheck --method sinkcheck --unrestricted-exchange --solver name={solver} > {results_path}{file_name}_sinkcheck_unrestricted-exchange.{file_extension}')
        os.system(f'psamm-model gapcheck --method gapfind --unrestricted-exchange --solver name={solver} > {results_path}{file_name}_gapfind_unrestricted-exchange.{file_extension}')

    if deep_check == False:
        os.system(f'psamm-model gapcheck --method gapfind --unrestricted-exchange --solver name={solver} --objective=ATPM > {results_path}{file_name}_gapfind_unrestricted-exchange.{file_extension}')


def gapfill_psamm(model_path='./genome/E_coli_yaml/', solver='gurobi', results_path='../../results/', file_name='gapcheck', file_extension='txt'):
    
    os.chdir(model_path)
    os.system(f'psamm-model gapfill --solver name={solver} --epsilon 0.01 --compound thr__L_c > {results_path}{file_name}_gapfill.{file_extension}')
    # os.system('psamm-model gapfill --no-implicit-sinks')
    # os.system(f'psamm-model fastgapfill --solver name={solver}')
    # fastgapfill
    # --db-penalty

# def gapfill_cobrapy(model_path='./genome/', model_name='iAF1260', results_path='../../results/'):
#     model = cobra.io.read_sbml_model(f'{model_path}{model_name}.xml')
#     model.solver = 'gurobi'
#     model.objective = 'THRS'
#     wt_sol = model.optimize().objective_value
#     print(wt_sol)
#     consistent_model = cobra.flux_analysis.fastcc(model)
#     print(len(consistent_model.reactions))
    
#     blocked = cobra.flux_analysis.find_blocked_reactions(consistent_model)
#     print(len(blocked))
#     new_solution = consistent_model.optimize()
#     print(new_solution.objective_value)

#     # universal = cobra.Model('universal_reactions')
#     # universal.add_reactions(blocked)
    

#     # with model:
#     #     model.objective = model.add_boundary(model.metabolites.get_by_id('thr__L_c'), type='demand')
    
#     # solution = gapfill(model, demand_reactions=False, iterations=4) #.to_csv(f'gapfill_{results_path}{model_name}.csv')
#     # print(solution)
#     # # print(solution)
#     # # return solution


if __name__ == '__main__':
    # gapfind_and_gapcheck(file_extension='tsv')
    # gapfill_cobrapy()
    gapfill_psamm()
    
