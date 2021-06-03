"""

mm10 set up the features and binary version of the knowngene db

"""

import sys, os, csv, gzip
sys.path.append(os.path.expanduser("~"))
from glbase3 import *

valid_chroms = set([str(i) for i in range(1,30)] + ['X', 'Y', 'MT'])

version = 32

enst = []
i = 0

missed_types = set([])

header = None

ensg_gc_percent = {}

fasta = utils.convertFASTAtoDict('gencode.v{}.transcripts.fa.gz'.format(version), gzip_input=True)
print('Loaded %s FASTA entries' % len(fasta))

for entry in fasta:
    header = entry['name'].split('|')
    seq = entry['seq'].lower()

    type = header[7]
    if type not in ('protein_coding', 'lincRNA'):
        if type not in missed_types:
            missed_types.add(type)
        continue

    gc = (seq.count('g') + seq.count('c') ) / len(seq) * 100.0

    if header[5][0:3] == 'MT-': # skip MT genes;
        print('Skipped %s' % header[5])
        continue

    ensg = header[1].split('.')[0]

    newentry = {'ensg': ensg,
        'enst': header[0],
        'type': header[7],
        'name': header[5],
        'gc': gc}
    enst.append(newentry)

    if ensg not in ensg_gc_percent:
        ensg_gc_percent[ensg] = []
    ensg_gc_percent[ensg].append(gc)

    #print(newentry)

    #i += 1
    #if i > 1000:
    #    break

print()
print('Missed types:', missed_types)
print()

enst_gl = genelist()
enst_gl.load_list(enst)
enst_gl = enst_gl.getColumns(['enst', 'gc'])
enst_gl.saveTSV('hg38_gencode_enst_gc_percent_v%s.txt' % version, key_order=['enst', 'gc'])

# save the gc table:
newl = []
for k in ensg_gc_percent:
    newl.append({'ensg': k, 'gc': sum(ensg_gc_percent[k]) / len(ensg_gc_percent[k])})

ensg_gc = genelist()
ensg_gc.load_list(newl)
ensg_gc.saveTSV('hg38_gencode_ensg_gc_percent_v%s.txt' % version, key_order=['ensg', 'gc'])

tes_gc = genelist('../repeats/hg38_repeats_gc.tsv', format={'force_tsv': True, 'ensg': 0, 'gc': 1})

print(tes_gc)
ensg_gc += tes_gc
ensg_gc.saveTSV('hg38_gencode_ensg_tes_gc_percent_v%s.txt' % version, key_order=['ensg', 'gc'])
