"""

Python PCA

"""

import os, sys, glob, numpy
sys.path.append('../sam_annotations/')
import sam_map
from glbase3 import *

config.draw_mode="pdf"

expn = glload("../te_counts/genes_ntc_expression.glb")

expn_no_log = expn.deepcopy()

expn.log(2, .1)
#expn.stats.print_stats()

#expn = expn.filter_high_expressed(5000,9)
pca = expn.get_pca(feature_key_name='name', whiten=True)
pca.train(8)

print(expn.getConditionNames())

cols = sam_map.get_colours(expn.getConditionNames())

genes = ['HNRNPU', ]

for gene in genes:
    spot_size = numpy.array(expn_no_log.get(key='name', value=gene)[0]['conditions']) / 100

    print(spot_size)

    pca.scatter(filename="scatter12-{0}.png".format(gene), x=1, y=2, figsize=[5,5],
        label=False, spot_size=spot_size,
        spot_cols=cols, label_font_size=5, adjust_labels=False)

