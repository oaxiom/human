
import itertools
from collections import defaultdict, Counter
from glbase3 import glload
import glbase3

from extended import bad_samples, unpublished

sample_description = {
    "Embryo2C E1 C1": "Embryo 2C",
    'Embryo4C E1 C1': 'Embryo 4C',
    'Embryo8C E1 C1': 'Embryo 8C',
    'B cells CD20p': 'B cells CD20p',
    'Bladder': 'Bladder',
    'CD34p progenitor cells': 'CD34p progenitor cells',
	'CD4p T cells' : 'CD4p T cells',
	'Cord blood CD34p CD38m' : 'Cord blood CD34p CD38m',
	'Chondrocytes': 'Chondrocytes',
	'Cortex' : 'Cortex',
	'Dermal fibroblasts' : 'Dermal fibroblasts',
	'Dermal lymphatic endothelium' : 'Dermal lymphatic endothelium',
	'Early basophilic erythroblast' : 'Early basophilic erythroblast',
	'Endometrial stromal cells' : 'Endometrial stromal cells',
	'Fetal retinal pigment epithelium' : 'Fetal retinal pigment epithelium',
	'Hair follicle dermal papilla' : 'Hair follicle dermal papilla',
	'Heart left ventrical' : 'Heart left ventrical',
	'hESC H1' : 'hESC H1',
	'Human skeletal muscle myoblasts' : 'Human skeletal muscle myoblasts',
	'iMSC' : 'iMSC' ,
	'Keratinocytes' : 'Keratinocytes',
	'Kidney proximal tubule cell' :'Kidney proximal tubule cell' ,
	'Late basophilic erythroblast' : 'Late basophilic erythroblast',
	'Liver' : 'Liver',
	'Lung fibroblast' : 'Lung fibroblast',
	'Mammary epithelial cells' : 'Mammary epithelial cells',
	'Mononuclear cells peripheral blood' : 'Mononuclear cells peripheral blood',
	'MSC adipose' : 'MSC adipose',
	'MSC bone marrow' : 'MSC bone marrow',
	'MSC umbilical cord' : 'MSC umbilical cord',
	'naive B cells' : 'naive B cells',
	'Neonatal dermal blood vascular endothelial cells' : 'Neonatal dermal blood vascular endothelial cells',
	'Neural crest cells' : 'Neural crest cells',
	'NPC' : 'NPC',
	'Orthochromatic erythroblast' : 'Orthochromatic erythroblast',
	'Pancreatic islets' : 'Pancreatic islets',
	'Placental epithelial' : 'Placental epithelial',
	'Placental pericytes' : 'Placental pericytes',
	'Polychromatic erythroblast' : 'Polychromatic erythroblast',
	'Proerythroblast' : 'Proerythroblast', # Temporary.
	'Prostate' : 'Prostate',
	'Prostate endothelial cell' : 'Prostate endothelial cell',
	'Skeletal muscle myotube' : 'Skeletal muscle myotube',
	'Sperm' : 'Sperm',
	'Umbilical vein endothelial cells' : 'Umbilical vein endothelial cells',
	'Villious mesenchymal fibroblasts 2' : 'Villious mesenchymal fibroblasts',# Temporary.
	'White preadipocytes' : 'White preadipocytes',
	'Late blastocyst E1 C1 pTE' : 'Late blastocyst E1 C1 pTE',
	'Late blastocyst E1 C4 mTE' : 'Late blastocyst E1 C4 mTE',
	'Late blastocyst E2 C1 EPI' : 'Late blastocyst E2 C1 EPI',
	'Late blastocyst E3 C2 PE' : 'Late blastocyst E3 C2 PE',
	'Morula E1 C1' : 'Morula E1 C1',
	'Oocyte E1 C1' : 'Oocyte E1 C1',
	'Zygote E1 C1' : 'Zygote E1 C1',
    }

desc_to_id = {v: k for k, v in zip(sample_description.keys(), sample_description.values())}

# See also: http://en.wikipedia.org/wiki/Cell_type
gene_layer = {"Embryonic":
        ['Embryo2C E1 C1', 'Embryo4C E1 C1', 'Embryo8C E1 C1', 'Morula E1 C1', 'Oocyte E1 C1',
        'Zygote E1 C1', 'Late blastocyst E1 C1 pTE', 'Late blastocyst E1 C4 mTE', 'Late blastocyst E2 C1 EPI',
        'Late blastocyst E3 C2 PE', 'hESC H1', 'Embryo 2C', 'Embryo 4C', 'Embryo 8C', 'hESCs 3iL',
        #'hESCs H18',
        #'hESCs primed', 'hESCs reset',
        'Morula', 'Oocyte', 'Placental epithelial', 'Placental pericytes', 'Pronuclei',
        'Zygote',
        'ESC H1', 'ESC H9',
        'rsESC H1' , 'rsESC H9'
        #'hESC cortical neuron d0 hESC',
        #'hESCs H1 18',
        ],
    "Germ cells":
        ['Sperm', 'Testes',
        ],
    "Mesoderm":
        ['Adipose', 'White preadipocytes', 'Kidney', 'Skeletal muscle','mesoderm invitro',
        'Ovary', 'Thyroid', 'Bladder', 'Human skeletal muscle myoblasts', 'Skeletal muscle myotube',
        'Heart', 'Lymph node', 'Achilles tendon', 'Adrenal gland', # Mixed mesoderm/neural crest though?
        'Airway smooth muscle', 'Cardiac resident MSC cKitp', 'Cardiac resident MSC W8B2p',
        'Bone marrow MSC W8B2p', 'Dermal fibroblasts', 'iMSC', 'Lung fibroblast',
        'MSC adipose', 'MSC bone marrow' , 'MSC umbilical cord' ,
        ],
    "Blood mesoderm":
        ['B cells CD20p', 'CD4p T cells', 'naive B cells', 'Monocytes CD14p', 'Neutrophil',
        'Bone marrow',
        'Early basophilic erythroblast', 'Late basophilic erythroblast',
        'Orthochromatic erythroblast', 'Polychromatic erythroblast',
        'Mononuclear cells peripheral blood',
        'CD34p progenitor cells', 'germinal B cells', 'Granulocytes', 'Macrophage M1', 'Macrophage M2',
        'Megakaryocytes', 'Monocytes', 'Proerythroblast', 'Platelets', 'CD4T naive',
        'CD4T Teffector', 'CD4T Tfh', 'Macrophages CD14p', 'Macrophages CD14p TNFp',
        'CD34p bone marrow cells', 'CD4T memory', 'CD4T Th1', 'CD4T Th17', 'CD4T Th17 effector',
        'CD4T Th1 effector', 'CD4T Th2', 'CD4T Th2 effector',
        'Bone marrow IL3Rahi precursors', 'Bone marrow IL3Ralo precursors',
        'Erythroid progenitor', 'iPSC microglia', 'microglia adult', 'microglia fetal', 'microglia fetal conditioned medium',
        'microglia induced', 'microglia induced conditioned medium', 'iPSC macrophages',
        'iPSC reprogramming CD34pCB D0' # Basically CD34+ CB precursors
        ],
    "Endoderm":
        ['Hepatocyts', 'Liver', 'Colon', 'Ileum', 'Lung normal', 'definitive endoderm invitro',
        'Pancreatic islets', 'Prostate', 'hESC liver diff d21 hepatocyte', 'hESC liver diff d13 hepatocyte',
        'hESC liver diff d11 hepatoblast', 'Pancreatic bud', 'Pancreatic bud invitro',
        'Lung 2', 'Gastric tissue', 'Airway basal cells', 'Bronchial epithelial cells',

        ],
    "Neurectoderm":
        ['NPC', 'Retina', 'Brain', 'Dorsolateral prefrontal cortex', 'ectoderm invitro',
        'hESC cortical neuron d12 cortical specification', 'hESC cortical neuron d19 cortical specification',
        'hESC cortical neuron d26 deep layer', 'hESC cortical neuron d33 deep layer',
        'hESC cortical neuron d49 deep layer', 'hESC cortical neuron d63 upper layer',
        'hESC cortical neuron d7', 'hESC cortical neuron d77 upper layer','induced cortical neuron',
        'Motor neuron sod av4p',  'Motor neuron sod pp', 'Cortex 2', 'invitro DA neurons',
        'Corneal endothelial cells adult', 'Corneal endothelial cells fetal',
        'Fetal retinal pigment epithelium', # neural crest?
        'Astrocytes', 'neocortex inner subventricular zone', 'neocortex cortical plate' ,
        'neocortex outer subventricular zone' , 'neocortex ventricular zone', 'NPC invitro',
        'NPC neuroepithelium', 'Radial glial early', 'Radial glial late' , 'Radial glial mid' ,
        'cortical neuron wta ctrl 0h', 'neurons',
        ],
    "Neural crest":
        ['Neural crest cells', 'Epidermal melanocytes', 'Epidermal melanocytes juvenile' ,
        'Epidermal melanocytes neonatal', 'chondrogenic ectomesenchyme'
        ],
    "Surface ectoderm":
        ['Keratinocytes', 'Epidermal keratinocytes', 'Hair follicle dermal papilla',
        # I think, but not sure:
        'Corneal endothelial cells adult', 'Corneal endothelial cells fetal',
        'Fetal retinal pigment epithelium',
        ],
    "Unassigned": [
        ]}

colour_guide = {"Embryonic": "orange",
    "Germ cells": "yellow",
    "Mesoderm": "green",
    "Blood mesoderm": "red",
    "Endoderm": "purple",
    "Neurectoderm": "blue",
    "Surface ectoderm": "cyan",
    "Neural crest": "magenta",
    "Mixed": "grey",
    "Unassigned": "grey"}

sample_colours = {} # coloured by germ layer
for k in sorted({x for v in gene_layer.values() for x in v}):
    sample_colours[k] = "grey" # no layer
    for gl in gene_layer:
        if k in gene_layer[gl]:
            sample_colours[k] = colour_guide[gl]

sample_gse = defaultdict(lambda: '?', {
    })

all_gses = [sample_gse[k] for k in sample_gse]
all_gses = set([x for sublist in all_gses for x in sublist])

gse_reference = defaultdict(lambda: '?',
    {
    })

pmid_gse = defaultdict(lambda: '?',
    {
    })

def get_colours(condition_names):
    cols = []
    for s in condition_names:
        if s in sample_colours:
            cols.append(sample_colours[s])
        else:
            print("sam_map.get_colours(): Not found:", s)
            cols.append("grey")
    return(cols)

def get_details(sample_name):
    gses = sample_gse[sample_name]
    refs = "; ".join([gse_reference[gse] for gse in gses])
    pmids = ", ".join([pmid_gse[gse] for gse in gses])
    gses = ", ".join(gses)
    # get the germ lineage:
    germ = "?"
    for k in gene_layer:
        if sample_name in gene_layer[k]:
            germ = k
            break
    return({"name": sample_name, "GEO": gses,
        "PMID": pmids, "Reference": refs, "germ layer": germ,
        "Description": sample_description[sample_name]})

def remap_expn_sample_names(expn):
    """
    Super-specific method to remap the sample names.
    """
    names = expn.getConditionNames()
    new_names = []
    for n in names:
        if n in sample_description:
            new_names.append(sample_description[n])
        else:
            new_names.append(n)
    expn.setConditionNames(new_names)

def get_citation_list(list_of_gses):
    """
    Get a citation list e.g.

    GSE0000000 (Smith et al., 2012; PMID: 000000000), ...

    """
    gses = list(set(sum([sample_gse[k] for k in list_of_gses], [])))
    gses.sort()
    r = ", ".join(["%s (%s, PMID:%s)" % (gse, gse_reference[gse], pmid_gse[gse]) for gse in gses])
    return(r)

if __name__ == "__main__":
    expn = glload("../te_counts/genes_ntc_expression.glb") # Only check against the publishable set

    print(expn.getConditionNames())

    print("Testing coherence")
    print("\nSample names:")
    # Test that all desc names are actually in the expn and vice versa:
    expn_names = expn.getConditionNames()
    desc_names = sample_description.keys()
    ss1 = set(expn_names) - set(desc_names)
    ss2 = set(desc_names) - set(expn_names)
    if ss1:
        print("Missing in sample_description:")
        for s in sorted(ss1):
            print("'{}',".format(s))
    print()
    if ss2:
        print("Missing in expn:")
        for s in sorted(ss2):
            print("'{}',".format(s))

    print("\nChecking for duplicate formal names in sample_description:")
    print(" failed\n".join([x for x, y in Counter(sample_description.values()).items() if y > 1]))

    print("\nSample GEO:")
    for c in expn.getConditionNames():
        if c not in sample_gse:
            print("Sample '{}' has no GSE entry".format(c))
    print("\nGene layer:")
    all_assigned_to_gene_layer = sorted({x for v in gene_layer.values() for x in v})

    #remap_expn_sample_names(expn)
    for c in expn.getConditionNames():
        if True not in [c == i for i in all_assigned_to_gene_layer]:
            print("ERROR: Sample '%s' has not been assigned to a germ layer" % c)

    print("\nCheck each entry in the germ layers is actually in the expn data:")
    all_conds = expn.getConditionNames()
    for lin in gene_layer:
        for sam in gene_layer[lin]:
            if sam not in all_conds:
                print("ERROR: '%s' entry in germ layer, no actual sample in data" % sam)

    print("Duplicates in germ layer:")
    for l in gene_layer.keys():
        print(" failed\n".join([x for x, y in Counter(gene_layer[l]).items() if y > 1]))

    print("\nNumber of samples in layer")
    for k in gene_layer:
        print(k, len(gene_layer[k]))

    print(set(sum(sample_gse.values(), [])))
    print('Number of unique GSE/study numbers:', len(set(sum(sample_gse.values(), []))))

    print("\nGSE -> PMID")
    for gse in all_gses:
        res = [True, True]
        res_text = []
        if gse not in gse_reference:
            res[0] = False
            #res_text.append("no reference")

        if gse not in pmid_gse:
            res[1] = False
            res_text.append("no pmid")

        if False in res:
            print("'%s': '', has " % (gse) + ", ".join(res_text))

    import csv
    oh = open("sample_map.tsv", "w")
    writer = csv.writer(oh, dialect=csv.excel_tab)
    keys = list(sample_description.keys())
    keys.sort()
    writer.writerow(["Description", "Germ layer", "GEO Accession", "PMID", "Reference(s)"])
    newl = []
    for k in keys:
        d = get_details(k)
        writer.writerow([d["Description"], d["germ layer"], d["GEO"], d["PMID"], d["Reference"]])
        newl.append({"name": k, "geo": d["GEO"], "desc": d["Description"], "lineage": d["germ layer"]})
    oh.close()

    print()
    print("\nCitation:")
    gses = list(gse_reference.keys())
    gses.sort()
    r = ", ".join(["%s (%s:%s)" % (gse, gse_reference[gse], pmid_gse[gse]) for gse in gses])
    print(r)
    print()

    gl = glbase3.genelist()
    gl.load_list(newl)
    gl.save("sample_map.glb")

    print(gl)
    # Print number of categories in each lineage:
    for k in gene_layer:
        print(k, len(gene_layer[k]))
