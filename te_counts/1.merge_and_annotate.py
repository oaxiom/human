
import sys, os, glob, gzip
import os, sys
sys.path.append("../sam_annotations/")
import sam_map
from glbase3 import *

all = None

conds = []
all_files = glob.glob("data/*.tsv.gz")
all_files.sort()

bad_samples = sam_map.bad_samples # See there for details.

for f in all_files:
    head = os.path.split(f)[1]

    if ".rp" in head:
        head = "_".join(head.split(".")[0:2])
    elif 'Hs_SS' in head:
        head = head.replace('Hs_SS_', '').replace('.tecount.tsv.gz', '').replace('.', '_')
    else:
        head = head.split(".")[0]

    base = head.replace("Hs_", "")

    #if ".rp" in head:
    #    base = "-".join(head.split(".")[0:2]).replace("-rp", "_")

    tbase = base
    n = 1
    while tbase in conds: # Make sure all condition names are unique.
        tbase = "%s_%s" % (tbase, n)
    base = tbase

    if base in bad_samples: # skip the bad samples
        continue

    conds.append(base)

    print("...", base)

    # skip the glbase overhead:
    rsem = []
    oh = gzip.open(f, "rt")
    for line in oh:
        ll = line.strip().split("\t")
        if not "gene_id" in ll[0]:
            rsem.append({"ensg": ll[0], base: int(ll[1])})
    oh.close()

    if not all:
        all = rsem
    else:
        for idx, g in enumerate(all):
            if g["ensg"] == rsem[idx]["ensg"]:
                g[base] = rsem[idx][base]
            else:
                print("Mismatch in ENSGs, break on sample: {}".format(f))
                sys.exit()

cond_names = conds

expn = expression(loadable_list=all, expn=cond_names)
expn.saveTSV("norm_input.tsv")
#expn.save("norm_input.glb") # Only need for QC purposes
