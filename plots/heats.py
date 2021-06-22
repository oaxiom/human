


import matplotlib.cm as cm
from glbase3 import *
config.draw_mode = "pdf"

arr = glload("../te_counts/genes_ntc_expression.glb")
arr.log(2,.1)

arrZ = arr.deepcopy()
arrZ.row_Z()

gene_lists = {
    "Foxies": ['FOXA1', 'FOXA2', 'FOXA3', 'FOXB1', 'FOXB2', 'FOXC2',
        'FOXD1', 'FOXD2', 'FOXD3', 'FOXDE1', 'FOXE3', 'FOXF1', 'FOXF2',
        'FOXG1', 'FOXH1', 'FOXI1', 'FOXI2', 'FOXI3', 'FOXJ1' ,'FOXJ2',
        'FOXJ3', 'FOXK1', 'FOXK2', 'FOXL1', 'FOXM1', 'FOXN1', 'FOXN2',
        'FOXN3', 'FOXN4', 'FOXO1', 'FOXO3', 'FOXO4', 'FOXO6', 'FOXP1',
        'FOXP2', 'FOXP3', 'FOXP4', 'FOXQ1', 'FOXR1', 'FOXR2', 'FOXS1',],
    'Nuclear_matrix': ['HNRNPU', 'SAFB', 'MATR3'],
    }

gls = {}
for k in gene_lists:
    gls[k] = genelist()
    gls[k].load_list([{"name": i} for i in gene_lists[k]])

todo = {} # load prepackaged here
todo.update(gls)

for k in todo:
    mm = todo[k].map(genelist=arr, key="name")

    mm.heatmap(filename="heats/%s_heat.png" % k, bracket=[0, 1], row_norm=False,
        row_font_size=5, col_font_size=4, size=[12,4], heat_wid=0.77,
        col_cluster=True, heat_hei=0.015*len(mm),
        colbar_label="rn")

    mm = todo[k].map(genelist=arrZ, key="name")

    mm.heatmap(filename="heats/Z-%s_heat.png" % k, bracket=[-3, 3], row_norm=False,
        row_font_size=5, col_font_size=4, size=[12,4], heat_wid=0.77,
        col_cluster=True, heat_hei=0.015*len(mm),
        colbar_label="Z-score")
