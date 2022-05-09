from cobra.io import write_sbml_model, read_sbml_model

model_name = 'iAF1260_mutant_delta_f6p_c'
model_path_sbml = f'./genome/Mutants/{model_name}.xml'
model_path_yaml= f'./genome/{model_name}/'

def generate_mutant(path=model_path_sbml):

    model = read_sbml_model(path)

    for i in [i.id for i in model.metabolites.f6p_c.reactions]:
        reaction = model.reactions.get_by_id(i)
        model.remove_reactions([reaction])
    return model

def export_model(model ,path='./genome/Mutants/', filename=model_name):
    write_sbml_model(model, f'{path}{filename}.xml')

if __name__ == '__main__':
    mutant = generate_mutant()
    export_model(mutant)