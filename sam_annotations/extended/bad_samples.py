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
    # SS Petropoulos Human embryo
    "embryo_E6_12_1296", "embryo_E6_12_1297", "embryo_E6_13_1385",
    "embryo_E6_14_1405", "embryo_E6_14_1415", "embryo_E6_17_1571", "embryo_E6_17_1621",
    "embryo_E6_18_1627", "embryo_E6_18_1634", "embryo_E6_18_1642", "embryo_E6_2_104",
    "embryo_E6_6_721", "embryo_E7_11_846", "embryo_E7_14_906", "embryo_E7_15_1094",
    "embryo_E7_16_1109", "embryo_E7_17_1331", "embryo_E7_19_1567", "embryo_E6_2_107",
    "embryo_E7_12_866",
    # Outliers:
    'embryo_E4_3_481', 'embryo_E3_2_466', 'embryo_E3_2_467', 'embryo_E3_3_456', 'embryo_E3_3_458',
    'embryo_E3_3_459', 'embryo_E4_10_1221', 'embryo_E4_10_1223', 'embryo_E4_10_1230',
    'embryo_E4_10_1232', 'embryo_E4_11_1258', 'embryo_E4_1_1',
    'embryo_E4_24_5_0_4_7', 'embryo_E4_2_10', 'embryo_E4_2_13', 'embryo_E4_31_5_1_11',
    'embryo_E4_31_5_1_2', 'embryo_E4_31_5_1_6', 'embryo_E4_31_5_1_8', 'embryo_E4_31_5_1_9',
    'embryo_E4_3_481', 'embryo_E4_3_486', 'embryo_E4_3_490', 'embryo_E4_3_491',
    'embryo_E4_7_642', 'embryo_E4_7_643', 'embryo_E4_7_644', 'embryo_E4_8_1171',
    'embryo_E5_10_934' ,'embryo_E5_10_935', 'embryo_E5_10_936', 'embryo_E5_10_940',
    'embryo_E5_10_941', 'embryo_E5_10_943' ,'embryo_E5_10_944', 'embryo_E5_10_945',
    'embryo_E5_10_947', 'embryo_E5_10_949', 'embryo_E5_10_950', 'embryo_E5_11_951',
    'embryo_E5_11_953' ,'embryo_E5_11_955', 'embryo_E5_11_957', 'embryo_E5_11_959',
    'embryo_E5_11_960', 'embryo_E5_11_961' ,'embryo_E5_11_962', 'embryo_E5_11_963',
    'embryo_E5_11_964', 'embryo_E5_11_965', 'embryo_E5_11_966', 'embryo_E5_12_1028',
    'embryo_E5_12_1029', 'embryo_E5_14_1785', 'embryo_E5_14_1791',
    'embryo_E5_14_1793', 'embryo_E5_14_1794', 'embryo_E5_14_1797',
    'embryo_E5_14_1798', 'embryo_E5_14_1802', 'embryo_E5_14_1808', 'embryo_E5_14_1811',
    'embryo_E5_15_1820', 'embryo_E5_15_1821', 'embryo_E5_15_1822', 'embryo_E5_15_1824',
    'embryo_E5_15_1825', 'embryo_E5_15_1826', 'embryo_E5_15_1827',
    'embryo_E5_15_1829', 'embryo_E5_15_1830', 'embryo_E5_15_1831', 'embryo_E5_15_1836',
    'embryo_E5_15_1837', 'embryo_E5_16_1885', 'embryo_E5_16_1900', 'embryo_E5_37_3247',
    'embryo_E5_39_3266', 'embryo_E5_3_52',
    'embryo_E6_10_1051', 'embryo_E6_11_1065', 'embryo_E6_11_1068', 'embryo_E6_11_1068',
    'embryo_E6_11_1070', 'embryo_E6_11_1074', 'embryo_E6_13_1371', 'embryo_E6_16_1500',
    'embryo_E6_1_72', 'embryo_E6_2_105',
    'embryo_E7_16_1169', 'embryo_E7_17_1307', 'embryo_E7_17_1308',
    'embryo_E7_2_147', 'embryo_E7_2_151',
    ])

