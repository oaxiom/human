"""

Python PCA

"""

import os, sys, glob
from glbase3 import *
sys.path.append("../../sam_annotations/")
import sam_map

config.draw_mode = "pdf"

expn = glload("../../te_counts/genes_ntc_expression.glb")
expn.log(2,.1)

sam_map.remap_expn_sample_names(expn)

#expn = expn.filter_high_expressed(5000,9)
pca = expn.get_pca(feature_key_name='name', whiten=True)
pca.train(10)

print(expn.getConditionNames())

cols = sam_map.get_colours(expn.getConditionNames())

size= (18,18)
bar_size = [4,8]

pca.explained_variance(filename="loading.png")
pca.scatter3d(filename="scatter123.png", x=1, y=2, z=3, figsize=[6,5], stem=True, label_font_size=6, depthshade=True, label=True, spot_cols=cols)
pca.scatter(filename="scatter12.png", x=1, y=2, label=True, spot_cols=cols, figsize=size, label_font_size=4, adjust_labels=True)
pca.scatter(filename="scatter23.png", x=2, y=3, label=True, spot_cols=cols, figsize=size, label_font_size=4, adjust_labels=True)
pca.scatter(filename="scatter24.png", x=2, y=4, label=True, spot_cols=cols, figsize=size, label_font_size=4, adjust_labels=True)
pca.scatter(filename="scatter25.png", x=2, y=5, label=True, spot_cols=cols, figsize=size, label_font_size=4, adjust_labels=True)

if not os.path.exists('glbs'):
    os.mkdir('glbs')

for interesing_pc in range(1,6):
    # Make sure dirs are around and empty:
    if not os.path.exists('barh_pc%s_bot' % (interesing_pc,)):
        os.mkdir('barh_pc%s_bot' % (interesing_pc,))
    if not os.path.exists('barh_pc%s_top' % (interesing_pc,)):
        os.mkdir('barh_pc%s_top' % (interesing_pc,))

    [os.remove(f) for f in glob.glob('barh_pc%s_bot/*.pdf' % (interesing_pc,))]
    [os.remove(f) for f in glob.glob('barh_pc%s_top/*.pdf' % (interesing_pc,))]

    lod = pca.loading(PC=interesing_pc, label_key='name', filename='load_pc1_top.png', top=100, bot=0)
    lod.heatmap(filename='heat_pc%s_top.png' % interesing_pc, row_label_key='name', bracket=[5, 15],
        row_font_size=6,col_font_size=6, heat_hei=0.008*len(lod), heat_wid=0.78, figsize=[22,12],
        col_colbar=cols)
    lod.boxplot('box_pc%s_top.png' % interesing_pc, size=[10,12])
    lod.unlog(2,.1)
    lod.save('glbs/pc%s_top.glb' % interesing_pc)
    for g in lod:
        lod.barh_single_item(value=g['name'], key="name", vert_space=0.8,
            filename="barh_pc%s_top/%s.png" % (interesing_pc, g['name'].replace('/', '-')),
            size=bar_size, yticklabel_fontsize=6, xticklabel_fontsize=6)

    lod = pca.loading(PC=interesing_pc, label_key='name', filename='load_pc%s_bot.png' % interesing_pc, top=0, bot=100)
    lod.heatmap(filename='heat_pc%s_bot.png' % interesing_pc, row_label_key='name', bracket=[5, 15],
        row_font_size=6,col_font_size=6, heat_hei=0.008*len(lod), heat_wid=0.78, figsize=[22,12],
        col_colbar=cols)
    lod.boxplot('box_pc%s_bot.png' % interesing_pc, size=[10,12])
    lod.unlog(2,.1)
    lod.save('glbs/pc%s_bot.glb' % interesing_pc)
    for g in lod:
        lod.barh_single_item(value=g['name'], key="name", vert_space=0.8,
            filename="barh_pc%s_bot/%s.png" % (interesing_pc, g['name'].replace('/', '-')),
            size=bar_size, yticklabel_fontsize=6, xticklabel_fontsize=6)



