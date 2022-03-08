
import sys, os
from glbase3 import *
sys.path.append('../../../sam_annotations/')
import sam_map

config.draw_mode = "pdf"

arr = glload("../../../te_counts/genes_ntc_expression.glb")

print(arr.getConditionNames())

conds_to_get = []
for c in arr.getConditionNames():
    if 'iPSC' in c: continue

    # Whitelist
    if 'microglia' in c: conds_to_get.append(c)
    elif 'astrocyte' in c: conds_to_get.append(c)
    elif 'oligodendrocyte' in c: conds_to_get.append(c)

print()
print('\n'.join(sorted(conds_to_get)))
print()

expn = arr.sliceConditions(conds_to_get)
expn = expn.filter_low_expressed(39.81072 , 1) # check 2a.gc_norm.R for the most recent number
expn.save("expn.glb")
expn.saveTSV("expn.tsv", key_order=['ensg', 'name'])

expn.tree(filename='tree.pdf', figsize=[5,3],)

