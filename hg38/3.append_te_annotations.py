"""

mm10 set up the features and binary version of the knowngene db

"""

import sys, os, csv, gzip
sys.path.append(os.path.expanduser("~"))
from glbase3 import *

version = 32

ensg = glload('hg38_gencode_ensg_v{}.glb'.format(version))

print(ensg)

tes = genelist(filename='../repeats/hg38_repeats_gc.tsv', format={'force_tsv': True, 'ensg': 0, 'name': 0})
tes.addEmptyKey('transcript_type', 'TE')

m = ensg + tes

m = m.removeDuplicates('ensg')

print(m)

m.save('hg38_gencode_ensg_tes_v{}.glb'.format(version))
m.saveTSV('hg38_gencode_ensg_tes_v{}.tsv'.format(version), key_order=['ensg', 'name', 'transcript_type'])
