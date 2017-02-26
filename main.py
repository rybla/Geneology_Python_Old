import geneology_manager
import parameters

NAME = "Test_Geneology"

GENERATIONS = 15

CHILDREN_PER_GENERATION = 5

PARENTS_PER_PROCREATION = 2

# strength of trait over other traits
INHERITED_TRAIT_WEIGHTS = {
    "color": 1
}
AQUIRED_TRAIT_WEIGHTS = {
    "generation": 1,
    "children": 50
}

# strength of inherited trait values over other possible values
INHERITED_TRAIT_ADVANTAGES = {
    "color": {
        1: 1,
        # 2: 1
    }
}

def main():
    gen_man = geneology_manager.GeneologyManager()

    params = parameters.Parameters(NAME,GENERATIONS,CHILDREN_PER_GENERATION,PARENTS_PER_PROCREATION,INHERITED_TRAIT_WEIGHTS,AQUIRED_TRAIT_WEIGHTS,INHERITED_TRAIT_ADVANTAGES)
    gen_man.create(params)

main()