

import matplotlib.cm as cm
from glbase3 import *
config.draw_mode = "pdf"

arr = glload("../te_counts/genes_ntc_expression.glb")

tree = arr.tree(filename="tree.pdf", row_names=arr["name"], color_threshold=0.0)

gene_list = [
    'LTR:ERV1:HERVE-int',
    'LTR:ERV1:L1TD',
    'ERVH48-1',

    'ZRSR2',

    'WRN', 'CAT', 'ATP7B', # Werner syndrome gene
    'ESR1', 'HNRNPU', 'SAFB', 'MATR3',
    'MCCC1', 'RELA', 'NFKB1',
    # MSC single--cell genes
    'ACTB', 'GAPDH', 'COL2A1', 'SOX9', 'CEBPA', 'PLIN1', 'COL1A1', 'RUNX2', 'PTGES', 'PTGES2',
    'NOS2', 'IDO1', 'IDO2', 'MMP2' ,'MMP9', 'GREM1', 'TGFB1', 'PDGFRA',
    'VEGFA', 'HGF', 'FGF2', 'NGF', 'NTF4',
    'KITLG', # SCF
    'IL4', 'IL6',
    'CXCL8', # IL-8
    'IL12A', 'IL12B',
    'IL17A', 'IL17B', 'IL17C',
    'TIMP1', 'TIMP2',
    'TNFRSF11B', #OPG
    'TNFSF10', # TRAIL4?
    'CCL2', 'CCL5', 'CCL16', 'CCL22', 'CCL28', 'CXCL1', 'CXCL12',
    'CCR1', 'CCR4' ,'CCR5', 'CCR7', 'CXCR3', 'CXCR4', 'CXCR6', 'CX3CR1',
    # Foxies:
    'FOXA1', 'FOXA2', 'FOXA3', 'FOXB1', 'FOXB2', 'FOXC2',
    'FOXD1', 'FOXD2', 'FOXD3', 'FOXDE1', 'FOXE3', 'FOXF1', 'FOXF2',
    'FOXG1', 'FOXH1', 'FOXI1', 'FOXI2', 'FOXI3', 'FOXJ1' ,'FOXJ2',
    'FOXJ3', 'FOXK1', 'FOXK2', 'FOXL1', 'FOXM1', 'FOXN1', 'FOXN2',
    'FOXN3', 'FOXN4', 'FOXO1', 'FOXO3', 'FOXO4', 'FOXO6', 'FOXP1',
    'FOXP2', 'FOXP3', 'FOXP4', 'FOXQ1', 'FOXR1', 'FOXR2', 'FOXS1',
    ]

for g in gene_list:
    arr.barh_single_item(value=g, key="name", filename="barh/%s.pdf" % g,
        tree=tree, yticklabel_fontsize=3, size=(5,17))


