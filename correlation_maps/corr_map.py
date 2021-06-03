
import sys, os
from glbase3 import *
sys.path.append("../sam_annotations/")
import sam_map

config.draw_mode = "pdf"

expn = glload("../te_counts/genes_ntc_expression.glb")
sam_map.remap_expn_sample_names(expn)

expn.log(2, 0.1)
expn.tree(filename="tree.png", color_threshold=0.0, label_size=4, size=(5,14))

expn.correlation_heatmap(filename="corr_heatmap.png",
    bracket=(0.0,1.0),
    size=(14,10),
    heat_wid=0.57,
    heat_hei=0.925,
    row_font_size=4)
