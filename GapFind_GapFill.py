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

def import_existing_model(ex_model_path='E_coli_sbml/ecoli_core_model.xml', destination_path='./genome/E_coli_yaml/'):
    os.system(f'psamm-import sbml --source {ex_model_path} --dest {destination_path}')


def gapfind_and_gapcheck(solver='gurobi', model_path='./genome/E_coli_yaml/', deep_check=False, results_path='../../results/', file_name='gapcheck', file_extension='txt'):
    
    os.chdir(model_path)

    if deep_check == True:
        os.system(f'psamm-model gapcheck --method prodcheck --solver name={solver} > {results_path}{file_name}_prodcheck.{file_extension}')
        os.system(f'psamm-model gapcheck --method sinkcheck --unrestricted-exchange --solver name={solver} > {results_path}{file_name}_sinkcheck_unrestricted-exchange.{file_extension}')
        os.system(f'psamm-model gapcheck --method gapfind --unrestricted-exchange --solver name={solver} > {results_path}{file_name}_gapfind_unrestricted-exchange.{file_extension}')

    if deep_check == False:
        os.system(f'psamm-model gapcheck --method gapfind --unrestricted-exchange --solver name={solver} > {results_path}{file_name}_gapfind_unrestricted-exchange.{file_extension}')


def gapfill(model_path='./genome/E_coli_yaml/'):
    os.chdir(model_path)
    os.system('psamm-model gapfill')

if __name__ == '__main__':
    gapfill()
