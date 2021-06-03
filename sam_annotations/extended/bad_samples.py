bad_samples = set([ 
    # <0.5e6 reads
    'Caudate_nucleus_1', 'Caudate_nucleus_2', 'Caudate_nucleus_3', 'Caudate_nucleus_4', 'Caudate_nucleus_5',
    'Frontal_pole_2', 'Frontal_pole_6', 
    'hESC_H1_15', 
    'Hippocampus_1', 'Hippocampus_2', 'Hippocampus_3', 'Hippocampus_3', 'Hippocampus_4', 'Hippocampus_5' , 'Hippocampus_6',
    'Macrophages_1', 'Macrophages_2', 'Sperm_3',
    'astrocyte_fetal_1', 'astrocyte_fetal_2', 'astrocyte_fetal_3', 'astrocyte_fetal_4', 'astrocyte_fetal_5', 
    'astrocyte_fetal_6', 'Polarbody_2', 
    'Oocyte_4', 'Oocyte_5',
    # others:
    'Airway_basal_cells_25', 'Airway_basal_cells_26', 'Airway_basal_cells_27', # are super outliers. I take the majority vote and delete these
    'Epidermal_keratinocytes_6', # sample 6 has a problem, I take the majority vote 
    'Large_airway_epithelial_cells_2', # looks mangled for some reason
    # Weird outliers:
    'Ileum_3', 'Ileum_9', 'Ileum_13', 'Retina_3',
    # Bad embryo:
    'Embryo_8C_10', 
    # Bad curves:
    'Skeletal_muscle_cells_1', 'Skeletal_muscle_cells_2', 
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

