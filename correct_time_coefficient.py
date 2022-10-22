import copy
import sys
from itertools import islice
from functools import reduce

# demo_before_ks = 'demo.csv'
demo_before_ks = sys.argv[1]


before_species_ks = {}
before_divergence_ks = {}

for line in islice(open(demo_before_ks), 1, None):
    lines = line.strip().split(',')
    if '_' in lines[0]:
        before_divergence_ks[lines[0]] = lines[1:][0]
    else:
        before_species_ks[lines[0]] = lines[1:]


def wgd_correct(species_ks, divergence_ks, lowest):
    new_species_ks, new_divergence_ks, coefficient = {}, {}, {}
    lowest_ks = species_ks[lowest][0]
    for key in species_ks:
        if len(species_ks[key]) > 1:
            coeff = float(lowest_ks)/float(species_ks[key][0])
            coefficient[key] = coeff
            new_species_ks[key] = []

            for k in species_ks[key][1:]:
                new_ks = coeff*float(k)
                new_species_ks[key].append(new_ks)

        else:
            coeff = float(lowest_ks)/float(species_ks[key][0])
            coefficient[key] = coeff

    for key in divergence_ks:
        spec1, spec2 = key.split('_')
        coeff = (float(coefficient[spec1])+float(coefficient[spec2]))/2
        coefficient[key] = coeff
        new_divergence_ks[key] = float(divergence_ks[key])*coeff

    return new_species_ks, new_divergence_ks, coefficient


def divergence_correct(species_ks, divergence_ks, lowest):
    new_species_ks, new_divergence_ks, coefficient = {}, {}, {}
    midd_div, middle_div_r, midd_ks = {}, {}, []
    lowest_spec = lowest.replace('_', '')
    coefficient[lowest_spec] = 1

    for key in divergence_ks:
        if lowest in key:
            midd_div[key] = divergence_ks[key]
            midd_ks.append(float(divergence_ks[key]))
        else:
            middle_div_r[key] = divergence_ks[key]

    low_ks = min(midd_ks)
    for k, v in midd_div.items():
        spec1, spec2 = k.split("_")
        coeff = low_ks/float(divergence_ks[k])
        coefficient[spec2] = 2*coeff-1
        coefficient[k] = coeff
    
    for key in species_ks:
        for s in species_ks[key]:
            new_ks = coefficient[key]*float(s)
            if key not in new_species_ks:
                new_species_ks[key] = [new_ks]
            else:
                new_species_ks[key].append(new_ks)

    for k, v in middle_div_r.items():
        spec1, spec2 = k.split('_')
        coeff = (float(coefficient[spec1])+float(coefficient[spec2]))/2
        coefficient[k] = coeff
        new_divergence_ks[k] = float(divergence_ks[k])*coeff

    return new_species_ks, new_divergence_ks, coefficient

def pprint_(*args):
    print(f'spec/div\tafter_ks')
    for k, v in args[0].items():
        print(f'{k}\t{v}')
    for k, v in args[1].items():
        print(f'{k}\t{v}')
    print(f'spec/div\tcoefficient')
    for k, v in args[2].items():
        print(f'{k}\t{v}')

def pprint_coefficient(name, coefficient):
    format_ = '{:^20}'*len(name)
    print(format_.format(*name))
    for k, v in coefficient.items():
        v.insert(0, k)
        # print('{:^15}'.format(k))
        format_ = '{:^20}'*len(v)
        print(format_.format(*v))

# print(before_species_ks)
middle_wgd, middle_div = before_species_ks, before_divergence_ks
spec_ks, div_ks, coeff = '', '', ''
middle_coefficient = {}
middle_name = ['name']

while True:
    lowest= input("Please enter the species with the lowest Ks value:[spec/end]")

    if lowest == 'end':
        break
    
    low_ks = input("Please enter the lowest Ks value[ks_value/no]:")
    
    if low_ks != 'no':
        middle_wgd[lowest] = [low_ks]
    middle_name.append(lowest)

    if '_' not in lowest:
        spec_ks, div_ks, coeff = wgd_correct(middle_wgd, middle_div, lowest)
        middle_wgd, middle_div = spec_ks, div_ks
        for k, v in coeff.items():
            if k in middle_coefficient:
                middle_coefficient[k].append(v)
            else:
                middle_coefficient[k] = [v]
        pprint_(middle_wgd, middle_div, middle_coefficient)
    else:
        spec_ks, div_ks, coeff = divergence_correct(middle_wgd, middle_div, lowest)
        middle_wgd, middle_div = spec_ks, div_ks
        for k, v in coeff.items():
            if k in middle_coefficient:
                middle_coefficient[k].append(v)
            else:
                middle_coefficient[k] = [v]
        pprint_(middle_wgd, middle_div, middle_coefficient)


print("\n")
print('###########################')
print("\n")
pprint_coefficient(middle_name, middle_coefficient)

