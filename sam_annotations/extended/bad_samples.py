bad_samples = set([
    # <0.5e6 reads
    'Caudate_nucleus_rp1', 'Caudate_nucleus_rp2', 'Caudate_nucleus_rp3', 'Caudate_nucleus_rp4', 'Caudate_nucleus_rp5',
    'Frontal_pole_rp2', 'Frontal_pole_rp6',
    'hESC_H1_rp15',
    'Hippocampus_rp1', 'Hippocampus_rp2', 'Hippocampus_rp3', 'Hippocampus_rp3', 'Hippocampus_rp4', 'Hippocampus_rp5' , 'Hippocampus_rp6',
    'Macrophages_rp1', 'Macrophages_rp2', 'Sperm_rp3',
    'astrocyte_fetal_rp1', 'astrocyte_fetal_rp2', 'astrocyte_fetal_rp3', 'astrocyte_fetal_4', 'astrocyte_fetal_5',
    'astrocyte_fetal_rp6', 'Polarbody_rp2',
    'Oocyte_rp4', 'Oocyte_rp5',
    # others:
    'Airway_basal_cells_rp25', 'Airway_basal_cells_rp26', 'Airway_basal_cells_rp27', # are super outliers. I take the majority vote and delete these
    'Epidermal_keratinocytes_rp6', # sample 6 has a problem, I take the majority vote
    'Large_airway_epithelial_cells_rp2', # looks mangled for some reason
    # Weird outliers:
    'Ileum_rp3', 'Ileum_rp9', 'Ileum_rp13',
    'Retina_rp3',
    'Treg_rp1',
    # Bad embryo:
    'Embryo_8C_rp10',
    # Bad curves:
    'astrocyte_fetal_rp5',
    'CD4p_ILC1_rp4',
    'Cardiac_resident_MSC_W8B2p_rp2',
    'Cortex_rp1',
    'Frontal_pole_rp1', 'Frontal_pole_rp2', 'Frontal_pole_rp3', 'Frontal_pole_rp4', 'Frontal_pole_rp5',
    'Skeletal_muscle_cells_rp1', 'Skeletal_muscle_cells_rp2',
    'Macrophages_rp1', 'Macrophages_rp2',
    # Single cell bads:
    # SS Conceptoid
    "SS_conceptoid_RHT119", "SS_conceptoid_RHT121", "SS_conceptoid_RHT122", "SS_conceptoid_RHT137",
    "SS_conceptoid_RHT138", "SS_conceptoid_RHT145", "SS_conceptoid_RHT146", "SS_conceptoid_RHT153",
    "SS_conceptoid_RHT154", "SS_conceptoid_RHT161", "SS_conceptoid_RHT169", "SS_conceptoid_RHT170",
    "SS_conceptoid_RHT174", "SS_conceptoid_RHT177", "SS_conceptoid_RHT178", "SS_conceptoid_RHT179",
    "SS_conceptoid_RHT182", "SS_conceptoid_RHT183", "SS_conceptoid_RHT184", "SS_conceptoid_RHT185",
    "SS_conceptoid_RHT186", "SS_conceptoid_RHT192", "SS_conceptoid_RHT193", "SS_conceptoid_RHT194",
    "SS_conceptoid_RHT195", "SS_conceptoid_RHT196", "SS_conceptoid_RHT201", "SS_conceptoid_RHT208",
    "SS_conceptoid_RHT209", "SS_conceptoid_RHT163", "SS_conceptoid_RHT205",
    "SS_hESC_RHC076", "SS_hESC_RHC086", "SS_hESC_RHC091", "SS_hESC_RHC099", "SS_hESC_RHC106", "SS_hESC_RHC119",
    "SS_hESC_RHC126", "SS_hESC_RHC133", "SS_hESC_RHC134", "SS_hESC_RHC139", "SS_hESC_RHC146",
    # SS Petropoulos Human embryo
    "SS_embryo_E6_12_1296", "SS_embryo_E6_12_1297", "SS_embryo_E6_13_1385",
    "SS_embryo_E6_14_1405", "SS_embryo_E6_14_1415", "SS_embryo_E6_17_1571", "SS_embryo_E6_17_1621",
    "SS_embryo_E6_18_1627", "SS_embryo_E6_18_1634", "SS_embryo_E6_18_1642", "SS_embryo_E6_2_104",
    "SS_embryo_E6_6_721", "SS_embryo_E7_11_846", "SS_embryo_E7_14_906", "SS_embryo_E7_15_1094",
    "SS_embryo_E7_16_1109", "SS_embryo_E7_17_1331", "SS_embryo_E7_19_1567", "SS_embryo_E6_2_107",
    "SS_embryo_E7_12_866",
    ])

