"""

post EDASeq clean-up and annotation.


"""

import sys, os, glob
from glbase3 import *

user_path = os.path.expanduser("~")
ensg = glload(os.path.join("../hg38/hg38_gencode_ensg_tes_v32.glb"))
config.draw_mode = 'pdf'

raw_expn = expression(filename="rawtags_gc_normed.tsv", format={"force_tsv": True, "skiplines": 0, "ensg": 0}, expn="column[1:]")
raw_expn.sort_conditions()

'''
# Temp code to get the replicates for the embryo stages;
res = {}
for c in raw_expn.getConditionNames():
    if 'embryo_' in c:
        cl = c.split('_')[1]
        if cl not in res:
            res[cl] = []
        res[cl].append(c)

for cl in res:
    print('[', end="")
    for c in res[cl]:
        print("'{}', ".format(c), end="")
    print('],')
'''

arr = raw_expn.mean_replicates(
    ['Achilles_tendon_rp1','Achilles_tendon_rp2','Achilles_tendon_rp3','Achilles_tendon_rp4'],
    ['Adipose_rp1', 'Adipose_rp2', 'adipose_rp3', 'adipose_rp4', 'adipose_rp5', 'adipose_rp6'],
    ['adult_pancreas_exocrine_rp1', 'adult_pancreas_exocrine_rp2','adult_pancreas_exocrine_rp3','adult_pancreas_exocrine_rp4', 'adult_pancreas_exocrine_rp5','adult_pancreas_exocrine_rp6'],
    ['Adrenal_gland_rp1', 'Adrenal_gland_rp2'],
    ['Airway_basal_cells_rp1', 'Airway_basal_cells_rp2', 'Airway_basal_cells_rp3', 'Airway_basal_cells_rp4', 'Airway_basal_cells_rp5', 'Airway_basal_cells_rp6', 'Airway_basal_cells_rp7', 'Airway_basal_cells_rp8', 'Airway_basal_cells_rp9', 'Airway_basal_cells_rp10', 'Airway_basal_cells_rp11', 'Airway_basal_cells_rp12', 'Airway_basal_cells_rp13', 'Airway_basal_cells_rp14', 'Airway_basal_cells_rp15', 'Airway_basal_cells_rp16', 'Airway_basal_cells_rp17', 'Airway_basal_cells_rp18', 'Airway_basal_cells_rp19', 'Airway_basal_cells_rp20', 'Airway_basal_cells_rp21', 'Airway_basal_cells_rp22', 'Airway_basal_cells_rp23', 'Airway_basal_cells_rp24', 'Airway_basal_cells_rp28', 'Airway_basal_cells_rp29', 'Airway_basal_cells_rp30'],
    ['Airway_smooth_muscle_rp1', 'Airway_smooth_muscle_rp2', 'Airway_smooth_muscle_rp3', 'Airway_smooth_muscle_rp4'],
    ['aorta_rp1', 'aorta_rp2'],
    ['Aortic_adventitial_fibroblasts_rp1', 'Aortic_adventitial_fibroblasts_rp2'],
    ['Aortic_endothelial_cells_rp1', 'Aortic_endothelial_cells_rp2'],
    ['Astrocytes_rp1', 'Astrocytes_rp2'],
    ['aortic_valve_tricuspid_valve_rp1', 'aortic_valve_tricuspid_valve_rp2', 'aortic_valve_tricuspid_valve_rp3', 'aortic_valve_tricuspid_valve_rp4', 'aortic_valve_tricuspid_valve_rp5', 'aortic_valve_tricuspid_valve_rp6', 'aortic_valve_tricuspid_valve_rp7', 'aortic_valve_tricuspid_valve_rp8', 'aortic_valve_tricuspid_valve_rp9', 'aortic_valve_tricuspid_valve_rp10'],
    ['astrocyte_adult_rp1', 'astrocyte_adult_rp10', 'astrocyte_adult_rp11', 'astrocyte_adult_rp12', 'astrocyte_adult_rp2', 'astrocyte_adult_rp3', 'astrocyte_adult_rp4', 'astrocyte_adult_rp5', 'astrocyte_adult_rp6', 'astrocyte_adult_rp7', 'astrocyte_adult_rp8', 'astrocyte_adult_rp9', 'astrocyte_fetal_rp4'],
    ['astrocyte_hippocampus_adult_rp1', 'astrocyte_hippocampus_adult_rp2', 'astrocyte_hippocampus_adult_rp3', 'astrocyte_hippocampus_adult_rp4'],
    ['B_cells_rp1', 'B_cells_rp2'],
    ['B_cells_CD20p_rp1', 'B_cells_CD20p_rp2', 'B_cells_CD20p_rp3', 'B_cells_CD20p_rp4', 'B_cells_CD20p_rp5', 'B_cells_CD20p_rp6'],
    ['Bone_marrow_rp1', 'Bone_marrow_rp2', 'Bone_marrow_rp3', 'Bone_marrow_rp4'],
    ['Bone_marrow_IL3Rahi_precursors_rp1', 'Bone_marrow_IL3Rahi_precursors_rp2', 'Bone_marrow_IL3Rahi_precursors_rp3'],
    ['Bone_marrow_IL3Ralo_precursors_rp1', 'Bone_marrow_IL3Ralo_precursors_rp2', 'Bone_marrow_IL3Ralo_precursors_rp3'],
    ['Bone_marrow_MSC_W8B2p_rp1', 'Bone_marrow_MSC_W8B2p_rp2'],
    ['Brain_rp1', 'Brain_rp2', 'Brain_rp4'],
    ['brain_endothelial_cells_rp1', 'brain_endothelial_cells_rp2'],
    ['Breast_rp2', 'Breast_rp3'],
    ['Bronchial_epithelial_cells_rp1', 'Bronchial_epithelial_cells_rp2'],
    ['Cardiac_resident_MSC_cKitp_rp1', 'Cardiac_resident_MSC_cKitp_rp2', 'Cardiac_resident_MSC_cKitp_rp3'],
    ['Cardiac_resident_MSC_W8B2p_rp1', 'Cardiac_resident_MSC_W8B2p_rp3'],
    ['CD34p_bone_marrow_cells_rp1', 'CD34p_bone_marrow_cells_rp2', 'CD34p_bone_marrow_cells_rp3', 'CD34p_bone_marrow_cells_rp4', 'CD34p_bone_marrow_cells_rp5'],
    ['CD4n_ILC1_rp1', 'CD4n_ILC1_rp2', 'CD4n_ILC1_rp3', 'CD4n_ILC1_rp4'],
    ['CD4p_ILC1_rp1', 'CD4p_ILC1_rp2', 'CD4p_ILC1_rp3'],
    ['CD4p_T_cells_rp1', 'CD4p_T_cells_rp2', 'CD4p_T_cells_rp3', 'CD4p_T_cells_rp4', 'CD4p_T_cells_rp5', 'CD4p_T_cells_rp6', 'CD4p_T_cells_rp7', 'CD4p_T_cells_rp8', 'CD4p_T_cells_rp9', 'CD4p_T_cells_rp10'],
    ['CD4T_memory_rp1', 'CD4T_memory_rp2', 'CD4T_memory_rp3'],
    ['CD4T_naive_rp1', 'CD4T_naive_rp2', 'CD4T_naive_rp3', 'CD4T_naive_rp4', 'CD4T_naive_rp5', 'CD4T_naive_rp6', 'CD4T_naive_rp7'],
    ['CD4T_Teffector_rp1', 'CD4T_Teffector_rp2', 'CD4T_Teffector_rp3'],
    ['CD4T_Tfh_rp1', 'CD4T_Tfh_rp2', 'CD4T_Tfh_rp3'],
    ['CD4T_Th1_rp1', 'CD4T_Th1_rp2'],
    ['CD4T_Th1_effector_rp1', 'CD4T_Th1_effector_rp2'],
    ['CD4T_Th17_rp1', 'CD4T_Th17_rp2'],
    ['CD4T_Th17_effector_rp1', 'CD4T_Th17_effector_rp2'],
    ['CD4T_Th2_rp1', 'CD4T_Th2_rp2'],
    ['CD4T_Th2_effector_rp1', 'CD4T_Th2_effector_rp2'],
    ['CD8p_T_cells_rp1', 'CD8p_T_cells_rp2'],
    ['Chondrocytes_rp1', 'Chondrocytes_rp2', 'chondrocytes_rp3', 'chondrocytes_rp4', 'chondrocytes_rp5'],
    ['chondrogenic_ectomesenchyme_rp1', 'chondrogenic_ectomesenchyme_rp2', 'chondrogenic_ectomesenchyme_rp3'],
    ['Colon_rp1', 'Colon_rp2', 'Colon_rp4', 'Colon_rp5'],
    ['colon_sigmoid_rp1', 'colon_sigmoid_rp2', 'colon_sigmoid_rp3', 'colon_sigmoid_rp4'],
    ['colon_transverse_rp1', 'colon_transverse_rp2', 'colon_transverse_rp3', 'colon_transverse_rp4'],
    ['colon_left_rp1', 'colonic_left_rp2'],
    ['colonic_mucosa_rp1', 'colonic_mucosa_rp2', 'colonic_mucosa_rp3'],
    ['Corneal_endothelial_cells_adult_rp1', 'Corneal_endothelial_cells_adult_rp2', 'Corneal_endothelial_cells_adult_rp3'],#, 'Corneal_endothelial_cells_rp1', 'Corneal_endothelial_cells_rp2'],
    ['Corneal_endothelial_cells_fetal_rp1', 'Corneal_endothelial_cells_fetal_rp2'],
    ['Cortex_rp2', 'Cortex_rp3', 'Cortex_rp4', 'Cortex_rp5'],
    ['cortical_neuron_wta_ctrl_0h', 'cortical_neuron_wtb_ctrl_0h', 'cortical_neuron_wtc_ctrl_0h'],
    ['Cumulus_granulosa_rp1', 'Cumulus_granulosa_rp2', 'Cumulus_granulosa_rp3'],
    ['Cumulus_granulosa_germinal_vesicle_rp1', 'Cumulus_granulosa_germinal_vesicle_rp2'],
    ['Cumulus_granulosa_M2_rp1', 'Cumulus_granulosa_M2_rp2', 'Cumulus_granulosa_M2_rp3'],
    ['decidual_stromal_cells_rp1', 'decidual_stromal_cells_rp2'],
    ['definitive_endoderm_invitro_rp1', 'definitive_endoderm_invitro_rp2', 'definitive_endoderm_invitro_rp3', 'definitive_endoderm_invitro_rp4', 'definitive_endoderm_invitro_rp5', 'definitive_endoderm_invitro_rp6', 'Definitive_endoderm_rp1', 'Definitive_endoderm_rp2', 'Definitive_endoderm_rp3'],
    ['Dermal_fibroblasts_rp1', 'Dermal_fibroblasts_rp2', 'Dermal_fibroblasts_rp3', 'Dermal_fibroblasts_rp4'], # Dermal 3 and 4 appear quite different from 1 and 2.
    ['Dermal_lymphatic_endothelium_rp1', 'Dermal_lymphatic_endothelium_rp2'],
    ['Dorsolateral_prefrontal_cortex_rp1', 'Dorsolateral_prefrontal_cortex_rp2', 'Dorsolateral_prefrontal_cortex_rp3', 'Dorsolateral_prefrontal_cortex_rp4', 'Dorsolateral_prefrontal_cortex_rp5'],
    ['Early_basophilic_erythroblast_rp1', 'Early_basophilic_erythroblast_rp2', 'Early_basophilic_erythroblast_rp3', 'Early_basophilic_erythroblast_rp4', 'Early_basophilic_erythroblast_rp5', 'Early_basophilic_erythroblast_rp6'],
    ['ectoderm_invitro_rp1' ,'ectoderm_invitro_rp2', 'ectoderm_invitro_rp3', 'ectoderm_invitro_rp4', 'ectoderm_invitro_rp5', 'ectoderm_invitro_rp6', 'ectoderm_invitro_rp7', 'ectoderm_invitro_rp8', 'ectoderm_invitro_rp9', 'ectoderm_invitro_rp10', 'ectoderm_invitro_rp11', 'ectoderm_invitro_rp12', 'ectoderm_invitro_rp13', 'ectoderm_invitro_rp14'],
    ['Embryo_2C_rp1', 'Embryo_2C_rp2', 'Embryo_2C_rp3'],
    ['Embryo2C_E1_C1', 'Embryo2C_E1_C2','Embryo2C_E2_C1','Embryo2C_E2_C2','Embryo2C_E3_C1','Embryo2C_E3_C2',],
    ['Embryo_4C_rp1', 'Embryo_4C_rp2', 'Embryo_4C_rp3', 'Embryo_4C_rp4'],
    ['Embryo_8C_rp1', 'Embryo_8C_rp2', 'Embryo_8C_rp3', 'Embryo_8C_rp4', 'Embryo_8C_rp5', 'Embryo_8C_rp6', 'Embryo_8C_rp7', 'Embryo_8C_rp8', 'Embryo_8C_rp9', 'Embryo_8C_rp11'],
    ['Embryo4C_E1_C1', 'Embryo4C_E1_C2', 'Embryo4C_E1_C3', 'Embryo4C_E1_C4', 'Embryo4C_E2_C1', 'Embryo4C_E2_C2', 'Embryo4C_E2_C3', 'Embryo4C_E2_C4', 'Embryo4C_E3_C1', 'Embryo4C_E3_C2', 'Embryo4C_E3_C3', 'Embryo4C_E3_C4'],
    ['Embryo8C_E1_C1', 'Embryo8C_E1_C2', 'Embryo8C_E1_C3', 'Embryo8C_E1_C4', 'Embryo8C_E2_C1', 'Embryo8C_E2_C2', 'Embryo8C_E2_C3', 'Embryo8C_E2_C4', 'Embryo8C_E2_C5', 'Embryo8C_E2_C6', 'Embryo8C_E2_C7', 'Embryo8C_E2_C8', 'Embryo8C_E3_C1', 'Embryo8C_E3_C2', 'Embryo8C_E3_C3', 'Embryo8C_E3_C4', 'Embryo8C_E3_C5', 'Embryo8C_E3_C6', 'Embryo8C_E3_C7', 'Embryo8C_E3_C8'],
    ['embryo_E3_1_443', 'embryo_E3_1_444', 'embryo_E3_1_445', 'embryo_E3_1_447', 'embryo_E3_1_448', 'embryo_E3_2_449', 'embryo_E3_2_450', 'embryo_E3_2_452', 'embryo_E3_2_453', 'embryo_E3_2_454', 'embryo_E3_2_455', 'embryo_E3_2_467', 'embryo_E3_3_456', 'embryo_E3_3_457', 'embryo_E3_3_458', 'embryo_E3_3_459', 'embryo_E3_3_460', 'embryo_E3_45_3374', 'embryo_E3_45_3375', 'embryo_E3_45_3376', 'embryo_E3_45_3377', 'embryo_E3_45_3378', 'embryo_E3_45_3379', 'embryo_E3_45_3380', 'embryo_E3_45_3381', 'embryo_E3_46_3382', 'embryo_E3_46_3383', 'embryo_E3_46_3384', 'embryo_E3_46_3385', 'embryo_E3_46_3386', 'embryo_E3_46_3387', 'embryo_E3_46_3388', 'embryo_E3_47_3389', 'embryo_E3_47_3390', 'embryo_E3_47_3391', 'embryo_E3_47_3392', 'embryo_E3_47_3393', 'embryo_E3_47_3394', 'embryo_E3_47_3395', 'embryo_E3_48_3396', 'embryo_E3_48_3397', 'embryo_E3_48_3398', 'embryo_E3_48_3399', 'embryo_E3_48_3400', 'embryo_E3_48_3401', 'embryo_E3_48_3402', 'embryo_E3_49_3403', 'embryo_E3_49_3405', 'embryo_E3_49_3406', 'embryo_E3_49_3407', 'embryo_E3_49_3408', 'embryo_E3_49_3409', 'embryo_E3_49_3410', 'embryo_E3_49_3411', 'embryo_E3_4_462', 'embryo_E3_4_463', 'embryo_E3_4_465', 'embryo_E3_50_3412', 'embryo_E3_50_3413', 'embryo_E3_50_3414', 'embryo_E3_50_3415', 'embryo_E3_50_3416', 'embryo_E3_50_3417', 'embryo_E3_51_3420', 'embryo_E3_51_3421', 'embryo_E3_51_3422', 'embryo_E3_51_3423', 'embryo_E3_51_3425', 'embryo_E3_51_3426', 'embryo_E3_52_3428', 'embryo_E3_52_3429', 'embryo_E3_52_3430', 'embryo_E3_52_3431', 'embryo_E3_52_3432', 'embryo_E3_52_3433', 'embryo_E3_52_3434', 'embryo_E3_53_3435', 'embryo_E3_53_3436', 'embryo_E3_53_3437', 'embryo_E3_53_3438', ],
    ['embryo_E4_10_1219', 'embryo_E4_10_1221', 'embryo_E4_10_1223', 'embryo_E4_10_1225', 'embryo_E4_10_1227', 'embryo_E4_10_1228', 'embryo_E4_10_1229', 'embryo_E4_10_1230', 'embryo_E4_10_1231', 'embryo_E4_10_1232', 'embryo_E4_10_1233', 'embryo_E4_11_1258', 'embryo_E4_1_1', 'embryo_E4_1_2', 'embryo_E4_1_3', 'embryo_E4_1_4', 'embryo_E4_1_7', 'embryo_E4_24_5_0_4_1', 'embryo_E4_24_5_0_4_10', 'embryo_E4_24_5_0_4_12', 'embryo_E4_24_5_0_4_2', 'embryo_E4_24_5_0_4_3', 'embryo_E4_24_5_0_4_4', 'embryo_E4_24_5_0_4_5', 'embryo_E4_24_5_0_4_7', 'embryo_E4_24_5_0_4_9', 'embryo_E4_2_10', 'embryo_E4_2_13', 'embryo_E4_31_5_1_10', 'embryo_E4_31_5_1_11', 'embryo_E4_31_5_1_12', 'embryo_E4_31_5_1_2', 'embryo_E4_31_5_1_3', 'embryo_E4_31_5_1_4', 'embryo_E4_31_5_1_6', 'embryo_E4_31_5_1_8', 'embryo_E4_31_5_1_9', 'embryo_E4_3_472', 'embryo_E4_3_473', 'embryo_E4_3_476', 'embryo_E4_3_478', 'embryo_E4_3_479', 'embryo_E4_3_480', 'embryo_E4_3_481', 'embryo_E4_3_482', 'embryo_E4_3_484', 'embryo_E4_3_485', 'embryo_E4_3_486', 'embryo_E4_3_487', 'embryo_E4_3_488', 'embryo_E4_3_489', 'embryo_E4_3_490', 'embryo_E4_3_491', 'embryo_E4_4_492', 'embryo_E4_4_493', 'embryo_E4_4_494', 'embryo_E4_4_495', 'embryo_E4_4_496', 'embryo_E4_4_497', 'embryo_E4_4_498', 'embryo_E4_4_499', 'embryo_E4_4_500', 'embryo_E4_4_501', 'embryo_E4_4_502', 'embryo_E4_4_503', 'embryo_E4_4_504', 'embryo_E4_4_505', 'embryo_E4_4_506', 'embryo_E4_4_507', 'embryo_E4_4_508', 'embryo_E4_4_509', 'embryo_E4_5_510', 'embryo_E4_5_511', 'embryo_E4_5_512', 'embryo_E4_5_513', 'embryo_E4_5_514', 'embryo_E4_5_515', 'embryo_E4_5_517', 'embryo_E4_5_518', 'embryo_E4_5_519', 'embryo_E4_5_520', 'embryo_E4_5_521', 'embryo_E4_5_522', 'embryo_E4_5_523', 'embryo_E4_5_524', 'embryo_E4_5_525', 'embryo_E4_5_526', 'embryo_E4_6_609', 'embryo_E4_6_610', 'embryo_E4_6_613', 'embryo_E4_6_614', 'embryo_E4_6_616', 'embryo_E4_6_625', 'embryo_E4_6_627', 'embryo_E4_7_641', 'embryo_E4_7_642', 'embryo_E4_7_643', 'embryo_E4_7_644', 'embryo_E4_7_645', 'embryo_E4_7_646', 'embryo_E4_7_647', 'embryo_E4_7_648', 'embryo_E4_8_1171', 'embryo_E4_8_1172', 'embryo_E4_8_1173', 'embryo_E4_8_1175', 'embryo_E4_8_1177', 'embryo_E4_8_1178', 'embryo_E4_8_1179', 'embryo_E4_8_1180', 'embryo_E4_8_1181', 'embryo_E4_8_1182', 'embryo_E4_8_1183', 'embryo_E4_8_1184', 'embryo_E4_8_1185', 'embryo_E4_8_1187', 'embryo_E4_8_1188', 'embryo_E4_8_1189', 'embryo_E4_8_1190', 'embryo_E4_8_1191', 'embryo_E4_8_1192', 'embryo_E4_8_1193', 'embryo_E4_8_1194', 'embryo_E4_9_1195', 'embryo_E4_9_1197', 'embryo_E4_9_1200', 'embryo_E4_9_1202', 'embryo_E4_9_1203', 'embryo_E4_9_1204', 'embryo_E4_9_1205', 'embryo_E4_9_1206', 'embryo_E4_9_1207', 'embryo_E4_9_1208', 'embryo_E4_9_1209', 'embryo_E4_9_1210', 'embryo_E4_9_1211', 'embryo_E4_9_1212', 'embryo_E4_9_1213', 'embryo_E4_9_1214', 'embryo_E4_9_1215', 'embryo_E4_9_1217', 'embryo_E4_9_1218', ],
    ['embryo_E4_late_33_3157', 'embryo_E4_late_33_3158', 'embryo_E4_late_33_3159', 'embryo_E4_late_33_3160', 'embryo_E4_late_33_3161', 'embryo_E4_late_33_3162', 'embryo_E4_late_33_3163', 'embryo_E4_late_33_3164', 'embryo_E4_late_33_3165', 'embryo_E4_late_33_3166', 'embryo_E4_late_33_3167', 'embryo_E4_late_34_3169', 'embryo_E4_late_34_3170', 'embryo_E4_late_34_3171', 'embryo_E4_late_34_3172', 'embryo_E4_late_34_3173', 'embryo_E4_late_34_3174', 'embryo_E4_late_34_3175', 'embryo_E4_late_34_3176', 'embryo_E4_late_34_3178', 'embryo_E4_late_34_3179', 'embryo_E4_late_34_3180', 'embryo_E4_late_34_3181', 'embryo_E4_late_34_3182', 'embryo_E4_late_34_3183', 'embryo_E4_late_34_3184', 'embryo_E4_late_34_3185', 'embryo_E4_late_34_3186', 'embryo_E4_late_34_3188', 'embryo_E4_late_34_3189', 'embryo_E4_late_34_3190', 'embryo_E4_late_34_3191', 'embryo_E4_late_34_3192', 'embryo_E4_late_35_3193', 'embryo_E4_late_35_3195', 'embryo_E4_late_35_3196', 'embryo_E4_late_35_3197', 'embryo_E4_late_35_3199', 'embryo_E4_late_35_3200', 'embryo_E4_late_35_3201', 'embryo_E4_late_35_3202', 'embryo_E4_late_35_3203', 'embryo_E4_late_35_3204', 'embryo_E4_late_35_3205', 'embryo_E4_late_35_3207', 'embryo_E4_late_35_3208', 'embryo_E4_late_35_3209', 'embryo_E4_late_35_3212', ],
    ['embryo_E5_10_932', 'embryo_E5_10_933', 'embryo_E5_10_934', 'embryo_E5_10_935', 'embryo_E5_10_936', 'embryo_E5_10_937', 'embryo_E5_10_938', 'embryo_E5_10_939', 'embryo_E5_10_940', 'embryo_E5_10_941', 'embryo_E5_10_942', 'embryo_E5_10_943', 'embryo_E5_10_944', 'embryo_E5_10_945', 'embryo_E5_10_947', 'embryo_E5_10_948', 'embryo_E5_10_949', 'embryo_E5_10_950', 'embryo_E5_11_951', 'embryo_E5_11_952', 'embryo_E5_11_953', 'embryo_E5_11_955', 'embryo_E5_11_956', 'embryo_E5_11_957', 'embryo_E5_11_959', 'embryo_E5_11_960', 'embryo_E5_11_961', 'embryo_E5_11_962', 'embryo_E5_11_963', 'embryo_E5_11_964', 'embryo_E5_11_965', 'embryo_E5_11_966', 'embryo_E5_12_1027', 'embryo_E5_12_1028', 'embryo_E5_12_1029', 'embryo_E5_12_1031', 'embryo_E5_12_1033', 'embryo_E5_12_1034', 'embryo_E5_12_1035', 'embryo_E5_12_1036', 'embryo_E5_12_1037', 'embryo_E5_12_1038', 'embryo_E5_12_1039', 'embryo_E5_12_1041', 'embryo_E5_12_1042', 'embryo_E5_13_1750', 'embryo_E5_13_1751', 'embryo_E5_13_1752', 'embryo_E5_13_1753', 'embryo_E5_13_1754', 'embryo_E5_13_1755', 'embryo_E5_13_1756', 'embryo_E5_13_1757', 'embryo_E5_13_1758', 'embryo_E5_13_1759', 'embryo_E5_13_1760', 'embryo_E5_13_1761', 'embryo_E5_13_1762', 'embryo_E5_13_1763', 'embryo_E5_13_1764', 'embryo_E5_13_1765', 'embryo_E5_13_1766', 'embryo_E5_13_1767', 'embryo_E5_13_1768', 'embryo_E5_13_1769', 'embryo_E5_13_1770', 'embryo_E5_13_1771', 'embryo_E5_13_1773', 'embryo_E5_13_1774', 'embryo_E5_13_1775', 'embryo_E5_13_1776', 'embryo_E5_13_1777', 'embryo_E5_13_1778', 'embryo_E5_13_1779', 'embryo_E5_13_1780', 'embryo_E5_13_1781', 'embryo_E5_14_1782', 'embryo_E5_14_1783', 'embryo_E5_14_1784', 'embryo_E5_14_1785', 'embryo_E5_14_1786', 'embryo_E5_14_1787', 'embryo_E5_14_1788', 'embryo_E5_14_1789', 'embryo_E5_14_1790', 'embryo_E5_14_1791', 'embryo_E5_14_1792', 'embryo_E5_14_1793', 'embryo_E5_14_1794', 'embryo_E5_14_1795', 'embryo_E5_14_1797', 'embryo_E5_14_1798', 'embryo_E5_14_1802', 'embryo_E5_14_1806', 'embryo_E5_14_1807', 'embryo_E5_14_1808', 'embryo_E5_14_1811', 'embryo_E5_14_1812', 'embryo_E5_14_1813', 'embryo_E5_14_1916', 'embryo_E5_14_1917', 'embryo_E5_14_1918', 'embryo_E5_14_1919', 'embryo_E5_14_1923', 'embryo_E5_14_1924', 'embryo_E5_14_1925', 'embryo_E5_15_1820', 'embryo_E5_15_1821', 'embryo_E5_15_1822', 'embryo_E5_15_1823', 'embryo_E5_15_1824', 'embryo_E5_15_1825', 'embryo_E5_15_1826', 'embryo_E5_15_1827', 'embryo_E5_15_1828', 'embryo_E5_15_1829', 'embryo_E5_15_1830', 'embryo_E5_15_1831', 'embryo_E5_15_1834', 'embryo_E5_15_1835', 'embryo_E5_15_1836', 'embryo_E5_15_1837', 'embryo_E5_15_1838', 'embryo_E5_15_1839', 'embryo_E5_15_1840', 'embryo_E5_15_1841', 'embryo_E5_15_1842', 'embryo_E5_15_1843', 'embryo_E5_15_1844', 'embryo_E5_15_1845', 'embryo_E5_16_1885', 'embryo_E5_16_1886', 'embryo_E5_16_1887', 'embryo_E5_16_1888', 'embryo_E5_16_1889', 'embryo_E5_16_1890', 'embryo_E5_16_1891', 'embryo_E5_16_1893', 'embryo_E5_16_1894', 'embryo_E5_16_1895', 'embryo_E5_16_1896', 'embryo_E5_16_1897', 'embryo_E5_16_1898', 'embryo_E5_16_1899', 'embryo_E5_16_1900', 'embryo_E5_16_1901', 'embryo_E5_16_1903', 'embryo_E5_16_1904', 'embryo_E5_16_1905', 'embryo_E5_16_1906', 'embryo_E5_16_1907', 'embryo_E5_16_1908', 'embryo_E5_16_1909', 'embryo_E5_16_1910', 'embryo_E5_16_1911', 'embryo_E5_16_1912', 'embryo_E5_16_1913', 'embryo_E5_16_1914', 'embryo_E5_16_1915', 'embryo_E5_1_26', 'embryo_E5_1_28', 'embryo_E5_1_30', 'embryo_E5_1_31', 'embryo_E5_1_32', 'embryo_E5_2_38', 'embryo_E5_2_40', 'embryo_E5_2_41', 'embryo_E5_2_42', 'embryo_E5_2_43', 'embryo_E5_2_45', 'embryo_E5_2_46', 'embryo_E5_2_47', 'embryo_E5_2_48', 'embryo_E5_37_3231', 'embryo_E5_37_3232', 'embryo_E5_37_3234', 'embryo_E5_37_3235', 'embryo_E5_37_3237', 'embryo_E5_37_3239', 'embryo_E5_37_3240', 'embryo_E5_37_3242', 'embryo_E5_37_3243', 'embryo_E5_37_3245', 'embryo_E5_37_3246', 'embryo_E5_37_3247', 'embryo_E5_37_3253', 'embryo_E5_38_3255', 'embryo_E5_38_3256', 'embryo_E5_39_3262', 'embryo_E5_39_3263', 'embryo_E5_39_3264', 'embryo_E5_39_3266', 'embryo_E5_39_3267', 'embryo_E5_39_3269', 'embryo_E5_39_3274', 'embryo_E5_3_49', 'embryo_E5_3_50', 'embryo_E5_3_51', 'embryo_E5_3_52', 'embryo_E5_3_54', 'embryo_E5_3_55', 'embryo_E5_3_56', 'embryo_E5_3_57', 'embryo_E5_3_58', 'embryo_E5_3_59', 'embryo_E5_3_60', 'embryo_E5_3_61', 'embryo_E5_40_3278', 'embryo_E5_40_3279', 'embryo_E5_40_3280', 'embryo_E5_40_3281', 'embryo_E5_40_3282', 'embryo_E5_40_3283', 'embryo_E5_40_3284', 'embryo_E5_40_3285', 'embryo_E5_40_3286', 'embryo_E5_40_3287', 'embryo_E5_40_3288', 'embryo_E5_40_3289', 'embryo_E5_40_3290', 'embryo_E5_40_3291', 'embryo_E5_40_3292', 'embryo_E5_40_3293', 'embryo_E5_40_3294', 'embryo_E5_40_3296', 'embryo_E5_40_3297', 'embryo_E5_40_3298', 'embryo_E5_40_3299', 'embryo_E5_40_3300', 'embryo_E5_40_3301', 'embryo_E5_40_3302', 'embryo_E5_40_3303', 'embryo_E5_40_3304', 'embryo_E5_41_3305', 'embryo_E5_41_3306', 'embryo_E5_41_3307', 'embryo_E5_41_3308', 'embryo_E5_41_3309', 'embryo_E5_41_3310', 'embryo_E5_41_3313', 'embryo_E5_41_3315', 'embryo_E5_41_3316', 'embryo_E5_41_3317', 'embryo_E5_41_3318', 'embryo_E5_41_3321', 'embryo_E5_41_3322', 'embryo_E5_41_3323', 'embryo_E5_41_3324', 'embryo_E5_41_3325', 'embryo_E5_41_3326', 'embryo_E5_41_3327', 'embryo_E5_41_3328', 'embryo_E5_42_3329', 'embryo_E5_42_3330', 'embryo_E5_42_3331', 'embryo_E5_42_3332', 'embryo_E5_42_3333', 'embryo_E5_42_3334', 'embryo_E5_42_3335', 'embryo_E5_42_3336', 'embryo_E5_42_3337', 'embryo_E5_42_3340', 'embryo_E5_43_3343', 'embryo_E5_43_3347', 'embryo_E5_43_3348', 'embryo_E5_43_3349', 'embryo_E5_43_3350', 'embryo_E5_43_3352', 'embryo_E5_43_3353', 'embryo_E5_43_3354', 'embryo_E5_43_3355', 'embryo_E5_43_3356', 'embryo_E5_43_3357', 'embryo_E5_43_3358', 'embryo_E5_43_3359', 'embryo_E5_43_3360', 'embryo_E5_43_3361', 'embryo_E5_43_3362', 'embryo_E5_43_3363', 'embryo_E5_43_3364', 'embryo_E5_43_3365', 'embryo_E5_5_100', 'embryo_E5_5_101', 'embryo_E5_5_91', 'embryo_E5_5_92', 'embryo_E5_5_93', 'embryo_E5_5_94', 'embryo_E5_5_95', 'embryo_E5_5_96', 'embryo_E5_5_97', 'embryo_E5_5_98', 'embryo_E5_5_99', 'embryo_E5_6_360', 'embryo_E5_6_361', 'embryo_E5_6_362', 'embryo_E5_6_363', 'embryo_E5_6_364', 'embryo_E5_6_365', 'embryo_E5_6_368', 'embryo_E5_6_369', 'embryo_E5_6_371', 'embryo_E5_6_372', 'embryo_E5_6_373', 'embryo_E5_6_375', 'embryo_E5_6_379', 'embryo_E5_6_382', 'embryo_E5_7_674', 'embryo_E5_7_675', 'embryo_E5_7_676', 'embryo_E5_7_677', 'embryo_E5_7_678', 'embryo_E5_7_679', 'embryo_E5_7_680', 'embryo_E5_7_681', 'embryo_E5_7_682', 'embryo_E5_7_683', 'embryo_E5_7_684', 'embryo_E5_7_685', 'embryo_E5_7_686', 'embryo_E5_7_687', 'embryo_E5_7_688', 'embryo_E5_7_689', 'embryo_E5_7_690', 'embryo_E5_7_691', 'embryo_E5_7_692', 'embryo_E5_7_693', 'embryo_E5_7_694', 'embryo_E5_7_695', 'embryo_E5_7_696', 'embryo_E5_7_697', 'embryo_E5_7_698', 'embryo_E5_7_700', 'embryo_E5_7_701', 'embryo_E5_7_702', 'embryo_E5_7_703', 'embryo_E5_7_704', 'embryo_E5_7_705', 'embryo_E5_7_706', 'embryo_E5_8_915', 'embryo_E5_8_916', 'embryo_E5_8_918', 'embryo_E5_8_919', 'embryo_E5_8_920', 'embryo_E5_8_921', 'embryo_E5_8_922', 'embryo_E5_9_923', 'embryo_E5_9_924', 'embryo_E5_9_925', 'embryo_E5_9_927', 'embryo_E5_9_928', 'embryo_E5_9_929', 'embryo_E5_9_930', 'embryo_E5_9_931', ],
    ['embryo_E5_early_31_3058', 'embryo_E5_early_31_3059', 'embryo_E5_early_31_3060', 'embryo_E5_early_31_3062', 'embryo_E5_early_31_3064', 'embryo_E5_early_31_3068', 'embryo_E5_early_31_3069', 'embryo_E5_early_31_3070', 'embryo_E5_early_31_3071', 'embryo_E5_early_31_3072', 'embryo_E5_early_36_3215', 'embryo_E5_early_36_3216', 'embryo_E5_early_36_3217', 'embryo_E5_early_36_3218', 'embryo_E5_early_36_3219', 'embryo_E5_early_36_3220', 'embryo_E5_early_36_3221', 'embryo_E5_early_36_3222', 'embryo_E5_early_36_3223', 'embryo_E5_early_36_3224', 'embryo_E5_early_36_3225', 'embryo_E5_early_36_3226', 'embryo_E5_early_36_3227', 'embryo_E5_early_36_3228', ],
    ['embryo_E6_10_1043', 'embryo_E6_10_1044', 'embryo_E6_10_1045', 'embryo_E6_10_1046', 'embryo_E6_10_1047', 'embryo_E6_10_1048', 'embryo_E6_10_1049', 'embryo_E6_10_1050', 'embryo_E6_10_1051', 'embryo_E6_10_1052', 'embryo_E6_10_1055', 'embryo_E6_10_1056', 'embryo_E6_10_1057', 'embryo_E6_10_1058', 'embryo_E6_10_1060', 'embryo_E6_10_1061', 'embryo_E6_11_1064', 'embryo_E6_11_1065', 'embryo_E6_11_1068', 'embryo_E6_11_1070', 'embryo_E6_11_1071', 'embryo_E6_11_1074', 'embryo_E6_11_1076', 'embryo_E6_12_1266', 'embryo_E6_12_1267', 'embryo_E6_12_1268', 'embryo_E6_12_1269', 'embryo_E6_12_1270', 'embryo_E6_12_1271', 'embryo_E6_12_1272', 'embryo_E6_12_1273', 'embryo_E6_12_1274', 'embryo_E6_12_1275', 'embryo_E6_12_1276', 'embryo_E6_12_1277', 'embryo_E6_12_1278', 'embryo_E6_12_1279', 'embryo_E6_12_1280', 'embryo_E6_12_1281', 'embryo_E6_12_1286', 'embryo_E6_12_1287', 'embryo_E6_12_1288', 'embryo_E6_12_1289', 'embryo_E6_12_1290', 'embryo_E6_12_1291', 'embryo_E6_12_1292', 'embryo_E6_12_1293', 'embryo_E6_12_1294', 'embryo_E6_12_1295', 'embryo_E6_12_1482', 'embryo_E6_12_1483', 'embryo_E6_12_1484', 'embryo_E6_12_1485', 'embryo_E6_12_1486', 'embryo_E6_12_1487', 'embryo_E6_12_1488', 'embryo_E6_13_1362', 'embryo_E6_13_1363', 'embryo_E6_13_1364', 'embryo_E6_13_1365', 'embryo_E6_13_1366', 'embryo_E6_13_1367', 'embryo_E6_13_1368', 'embryo_E6_13_1369', 'embryo_E6_13_1370', 'embryo_E6_13_1371', 'embryo_E6_13_1372', 'embryo_E6_13_1373', 'embryo_E6_13_1374', 'embryo_E6_13_1375', 'embryo_E6_13_1376', 'embryo_E6_13_1377', 'embryo_E6_13_1378', 'embryo_E6_13_1379', 'embryo_E6_13_1380', 'embryo_E6_13_1381', 'embryo_E6_13_1382', 'embryo_E6_13_1383', 'embryo_E6_13_1384', 'embryo_E6_13_1386', 'embryo_E6_13_1387', 'embryo_E6_13_1388', 'embryo_E6_13_1389', 'embryo_E6_13_1390', 'embryo_E6_13_1391', 'embryo_E6_13_1392', 'embryo_E6_13_1393', 'embryo_E6_13_1394', 'embryo_E6_13_1395', 'embryo_E6_13_1396', 'embryo_E6_13_1397', 'embryo_E6_13_1398', 'embryo_E6_13_1399', 'embryo_E6_13_1400', 'embryo_E6_14_1402', 'embryo_E6_14_1403', 'embryo_E6_14_1404', 'embryo_E6_14_1406', 'embryo_E6_14_1407', 'embryo_E6_14_1409', 'embryo_E6_14_1410', 'embryo_E6_14_1411', 'embryo_E6_14_1412', 'embryo_E6_14_1413', 'embryo_E6_14_1414', 'embryo_E6_14_1416', 'embryo_E6_14_1417', 'embryo_E6_14_1418', 'embryo_E6_14_1419', 'embryo_E6_14_1420', 'embryo_E6_14_1421', 'embryo_E6_14_1422', 'embryo_E6_14_1423', 'embryo_E6_14_1424', 'embryo_E6_14_1425', 'embryo_E6_14_1426', 'embryo_E6_14_1427', 'embryo_E6_14_1428', 'embryo_E6_14_1429', 'embryo_E6_14_1430', 'embryo_E6_14_1431', 'embryo_E6_14_1432', 'embryo_E6_14_1433', 'embryo_E6_15_1434', 'embryo_E6_15_1435', 'embryo_E6_15_1436', 'embryo_E6_15_1437', 'embryo_E6_15_1438', 'embryo_E6_15_1439', 'embryo_E6_15_1441', 'embryo_E6_15_1442', 'embryo_E6_15_1443', 'embryo_E6_15_1445', 'embryo_E6_15_1446', 'embryo_E6_15_1447', 'embryo_E6_15_1450', 'embryo_E6_15_1451', 'embryo_E6_15_1453', 'embryo_E6_15_1454', 'embryo_E6_15_1455', 'embryo_E6_15_1457', 'embryo_E6_15_1458', 'embryo_E6_15_1460', 'embryo_E6_15_1461', 'embryo_E6_15_1462', 'embryo_E6_15_1463', 'embryo_E6_15_1465', 'embryo_E6_15_1466', 'embryo_E6_15_1467', 'embryo_E6_15_1468', 'embryo_E6_15_1469', 'embryo_E6_15_1470', 'embryo_E6_15_1471', 'embryo_E6_15_1473', 'embryo_E6_15_1474', 'embryo_E6_15_1475', 'embryo_E6_15_1476', 'embryo_E6_15_1477', 'embryo_E6_15_1478', 'embryo_E6_15_1479', 'embryo_E6_15_1481', 'embryo_E6_16_1493', 'embryo_E6_16_1494', 'embryo_E6_16_1495', 'embryo_E6_16_1496', 'embryo_E6_16_1497', 'embryo_E6_16_1498', 'embryo_E6_16_1499', 'embryo_E6_16_1500', 'embryo_E6_16_1501', 'embryo_E6_16_1503', 'embryo_E6_16_1504', 'embryo_E6_16_1505', 'embryo_E6_17_1570', 'embryo_E6_17_1572', 'embryo_E6_17_1573', 'embryo_E6_17_1574', 'embryo_E6_17_1575', 'embryo_E6_17_1576', 'embryo_E6_17_1578', 'embryo_E6_17_1579', 'embryo_E6_17_1581', 'embryo_E6_17_1582', 'embryo_E6_17_1583', 'embryo_E6_17_1584', 'embryo_E6_17_1585', 'embryo_E6_17_1586', 'embryo_E6_17_1587', 'embryo_E6_17_1588', 'embryo_E6_17_1589', 'embryo_E6_17_1590', 'embryo_E6_17_1591', 'embryo_E6_17_1592', 'embryo_E6_17_1593', 'embryo_E6_17_1594', 'embryo_E6_17_1596', 'embryo_E6_17_1598', 'embryo_E6_17_1599', 'embryo_E6_17_1600', 'embryo_E6_17_1601', 'embryo_E6_17_1602', 'embryo_E6_17_1603', 'embryo_E6_17_1605', 'embryo_E6_17_1606', 'embryo_E6_17_1607', 'embryo_E6_17_1608', 'embryo_E6_17_1609', 'embryo_E6_17_1610', 'embryo_E6_17_1611', 'embryo_E6_17_1612', 'embryo_E6_17_1613', 'embryo_E6_17_1614', 'embryo_E6_17_1616', 'embryo_E6_17_1617', 'embryo_E6_17_1618', 'embryo_E6_17_1619', 'embryo_E6_17_1620', 'embryo_E6_18_1622', 'embryo_E6_18_1623', 'embryo_E6_18_1624', 'embryo_E6_18_1625', 'embryo_E6_18_1626', 'embryo_E6_18_1628', 'embryo_E6_18_1629', 'embryo_E6_18_1630', 'embryo_E6_18_1632', 'embryo_E6_18_1633', 'embryo_E6_18_1635', 'embryo_E6_18_1636', 'embryo_E6_18_1637', 'embryo_E6_18_1638', 'embryo_E6_18_1639', 'embryo_E6_18_1640', 'embryo_E6_18_1641', 'embryo_E6_18_1643', 'embryo_E6_18_1644', 'embryo_E6_18_1645', 'embryo_E6_1_72', 'embryo_E6_1_73', 'embryo_E6_1_74', 'embryo_E6_1_77', 'embryo_E6_1_78', 'embryo_E6_1_79', 'embryo_E6_1_80', 'embryo_E6_1_81', 'embryo_E6_1_82', 'embryo_E6_1_83', 'embryo_E6_1_84', 'embryo_E6_1_85', 'embryo_E6_1_86', 'embryo_E6_1_88', 'embryo_E6_1_89', 'embryo_E6_1_90', 'embryo_E6_22_1846', 'embryo_E6_22_1847', 'embryo_E6_22_1848', 'embryo_E6_22_1849', 'embryo_E6_22_1850', 'embryo_E6_22_1851', 'embryo_E6_22_1852', 'embryo_E6_22_1853', 'embryo_E6_22_1854', 'embryo_E6_22_1855', 'embryo_E6_22_1856', 'embryo_E6_22_1857', 'embryo_E6_22_1858', 'embryo_E6_22_1859', 'embryo_E6_22_1860', 'embryo_E6_22_1861', 'embryo_E6_22_1862', 'embryo_E6_22_1863', 'embryo_E6_22_1864', 'embryo_E6_22_1865', 'embryo_E6_22_1866', 'embryo_E6_22_1867', 'embryo_E6_2_105', 'embryo_E6_2_108', 'embryo_E6_2_109', 'embryo_E6_2_114', 'embryo_E6_2_115', 'embryo_E6_2_116', 'embryo_E6_2_117', 'embryo_E6_2_118', 'embryo_E6_2_119', 'embryo_E6_3_383', 'embryo_E6_3_384', 'embryo_E6_3_389', 'embryo_E6_3_391', 'embryo_E6_3_395', 'embryo_E6_3_396', 'embryo_E6_4_424', 'embryo_E6_4_425', 'embryo_E6_4_426', 'embryo_E6_4_427', 'embryo_E6_4_429', 'embryo_E6_4_432', 'embryo_E6_6_707', 'embryo_E6_6_708', 'embryo_E6_6_709', 'embryo_E6_6_710', 'embryo_E6_6_712', 'embryo_E6_6_713', 'embryo_E6_6_714', 'embryo_E6_6_715', 'embryo_E6_6_716', 'embryo_E6_6_717', 'embryo_E6_6_718', 'embryo_E6_6_719', 'embryo_E6_6_720', 'embryo_E6_6_722', 'embryo_E6_6_723', 'embryo_E6_6_724', 'embryo_E6_6_725', 'embryo_E6_6_726', 'embryo_E6_6_727', 'embryo_E6_6_728', 'embryo_E6_7_729', 'embryo_E6_7_737', 'embryo_E6_7_738', 'embryo_E6_7_739', 'embryo_E6_7_741', 'embryo_E6_7_742', 'embryo_E6_7_743', 'embryo_E6_7_744', 'embryo_E6_8_769', 'embryo_E6_8_771', 'embryo_E6_8_772', 'embryo_E6_8_773', 'embryo_E6_8_774', 'embryo_E6_8_775', 'embryo_E6_8_776', 'embryo_E6_8_777', 'embryo_E6_8_778', 'embryo_E6_8_779', 'embryo_E6_8_780', 'embryo_E6_8_781', 'embryo_E6_8_782', 'embryo_E6_8_783', 'embryo_E6_8_784', 'embryo_E6_8_785', 'embryo_E6_8_786', 'embryo_E6_8_787', 'embryo_E6_8_789', 'embryo_E6_8_790', 'embryo_E6_8_791', 'embryo_E6_8_792', 'embryo_E6_8_793', 'embryo_E6_8_794', 'embryo_E6_8_795', 'embryo_E6_8_796', 'embryo_E6_8_797', 'embryo_E6_8_798', 'embryo_E6_8_799', 'embryo_E6_8_800', 'embryo_E6_8_801', 'embryo_E6_8_802', 'embryo_E6_8_803', 'embryo_E6_8_804', 'embryo_E6_8_806', 'embryo_E6_8_807', 'embryo_E6_8_808', 'embryo_E6_8_809', 'embryo_E6_8_810', 'embryo_E6_8_811', 'embryo_E6_8_812', 'embryo_E6_8_813', 'embryo_E6_8_814', 'embryo_E6_8_815', 'embryo_E6_8_816', 'embryo_E6_8_817', 'embryo_E6_8_818', 'embryo_E6_8_819', 'embryo_E6_8_820', 'embryo_E6_8_821', 'embryo_E6_8_822', 'embryo_E6_8_823', 'embryo_E6_8_824', 'embryo_E6_8_825', 'embryo_E6_8_826', 'embryo_E6_8_827', 'embryo_E6_8_828', 'embryo_E6_8_829', 'embryo_E6_8_831', 'embryo_E6_8_832', 'embryo_E6_9_1007', 'embryo_E6_9_1008', 'embryo_E6_9_1010', 'embryo_E6_9_1011', 'embryo_E6_9_1012', 'embryo_E6_9_1013', 'embryo_E6_9_1014', 'embryo_E6_9_1015', 'embryo_E6_9_1016', 'embryo_E6_9_1017', 'embryo_E6_9_1018', 'embryo_E6_9_1020', 'embryo_E6_9_1021', 'embryo_E6_9_1022', 'embryo_E6_9_1023', 'embryo_E6_9_1024', 'embryo_E6_9_1025', 'embryo_E6_9_1026', ],
    ['embryo_E7_10_745', 'embryo_E7_10_746', 'embryo_E7_10_747', 'embryo_E7_10_748', 'embryo_E7_10_749', 'embryo_E7_10_750', 'embryo_E7_10_753', 'embryo_E7_10_756', 'embryo_E7_10_760', 'embryo_E7_10_761', 'embryo_E7_10_762', 'embryo_E7_10_763', 'embryo_E7_10_764', 'embryo_E7_10_766', 'embryo_E7_10_767', 'embryo_E7_10_768', 'embryo_E7_11_833', 'embryo_E7_11_835', 'embryo_E7_11_836', 'embryo_E7_11_837', 'embryo_E7_11_838', 'embryo_E7_11_839', 'embryo_E7_11_840', 'embryo_E7_11_841', 'embryo_E7_11_842', 'embryo_E7_11_843', 'embryo_E7_11_844', 'embryo_E7_11_845', 'embryo_E7_11_847', 'embryo_E7_11_848', 'embryo_E7_11_849', 'embryo_E7_11_850', 'embryo_E7_11_851', 'embryo_E7_11_852', 'embryo_E7_11_853', 'embryo_E7_11_854', 'embryo_E7_11_855', 'embryo_E7_11_856', 'embryo_E7_12_857', 'embryo_E7_12_858', 'embryo_E7_12_859', 'embryo_E7_12_860', 'embryo_E7_12_861', 'embryo_E7_12_862', 'embryo_E7_12_863', 'embryo_E7_12_864', 'embryo_E7_12_865', 'embryo_E7_12_869', 'embryo_E7_12_870', 'embryo_E7_12_871', 'embryo_E7_12_872', 'embryo_E7_12_874', 'embryo_E7_12_875', 'embryo_E7_12_876', 'embryo_E7_12_877', 'embryo_E7_12_878', 'embryo_E7_12_879', 'embryo_E7_12_880', 'embryo_E7_13_881', 'embryo_E7_13_882', 'embryo_E7_13_883', 'embryo_E7_13_884', 'embryo_E7_13_885', 'embryo_E7_13_886', 'embryo_E7_13_887', 'embryo_E7_13_888', 'embryo_E7_13_889', 'embryo_E7_13_890', 'embryo_E7_13_891', 'embryo_E7_13_892', 'embryo_E7_14_893', 'embryo_E7_14_894', 'embryo_E7_14_895', 'embryo_E7_14_896', 'embryo_E7_14_897', 'embryo_E7_14_898', 'embryo_E7_14_899', 'embryo_E7_14_900', 'embryo_E7_14_901', 'embryo_E7_14_902', 'embryo_E7_14_903', 'embryo_E7_14_904', 'embryo_E7_14_905', 'embryo_E7_14_907', 'embryo_E7_14_908', 'embryo_E7_14_909', 'embryo_E7_14_910', 'embryo_E7_14_911', 'embryo_E7_14_912', 'embryo_E7_14_913', 'embryo_E7_14_914', 'embryo_E7_15_1078', 'embryo_E7_15_1079', 'embryo_E7_15_1080', 'embryo_E7_15_1081', 'embryo_E7_15_1082', 'embryo_E7_15_1083', 'embryo_E7_15_1084', 'embryo_E7_15_1085', 'embryo_E7_15_1086', 'embryo_E7_15_1087', 'embryo_E7_15_1088', 'embryo_E7_15_1089', 'embryo_E7_15_1090', 'embryo_E7_15_1091', 'embryo_E7_15_1092', 'embryo_E7_15_1096', 'embryo_E7_15_1098', 'embryo_E7_15_1099', 'embryo_E7_15_1100', 'embryo_E7_15_1101', 'embryo_E7_16_1102', 'embryo_E7_16_1103', 'embryo_E7_16_1104', 'embryo_E7_16_1105', 'embryo_E7_16_1106', 'embryo_E7_16_1107', 'embryo_E7_16_1108', 'embryo_E7_16_1110', 'embryo_E7_16_1111', 'embryo_E7_16_1112', 'embryo_E7_16_1113', 'embryo_E7_16_1114', 'embryo_E7_16_1115', 'embryo_E7_16_1116', 'embryo_E7_16_1118', 'embryo_E7_16_1119', 'embryo_E7_16_1120', 'embryo_E7_16_1121', 'embryo_E7_16_1122', 'embryo_E7_16_1123', 'embryo_E7_16_1124', 'embryo_E7_16_1125', 'embryo_E7_16_1126', 'embryo_E7_16_1127', 'embryo_E7_16_1128', 'embryo_E7_16_1129', 'embryo_E7_16_1130', 'embryo_E7_16_1131', 'embryo_E7_16_1132', 'embryo_E7_16_1133', 'embryo_E7_16_1134', 'embryo_E7_16_1135', 'embryo_E7_16_1136', 'embryo_E7_16_1138', 'embryo_E7_16_1139', 'embryo_E7_16_1141', 'embryo_E7_16_1142', 'embryo_E7_16_1143', 'embryo_E7_16_1144', 'embryo_E7_16_1146', 'embryo_E7_16_1147', 'embryo_E7_16_1148', 'embryo_E7_16_1149', 'embryo_E7_16_1150', 'embryo_E7_16_1152', 'embryo_E7_16_1153', 'embryo_E7_16_1154', 'embryo_E7_16_1155', 'embryo_E7_16_1156', 'embryo_E7_16_1157', 'embryo_E7_16_1158', 'embryo_E7_16_1159', 'embryo_E7_16_1160', 'embryo_E7_16_1161', 'embryo_E7_16_1162', 'embryo_E7_16_1163', 'embryo_E7_16_1164', 'embryo_E7_16_1165', 'embryo_E7_16_1166', 'embryo_E7_16_1167', 'embryo_E7_16_1168', 'embryo_E7_16_1169', 'embryo_E7_16_1170', 'embryo_E7_17_1301', 'embryo_E7_17_1302', 'embryo_E7_17_1303', 'embryo_E7_17_1304', 'embryo_E7_17_1305', 'embryo_E7_17_1306', 'embryo_E7_17_1307', 'embryo_E7_17_1308', 'embryo_E7_17_1309', 'embryo_E7_17_1310', 'embryo_E7_17_1311', 'embryo_E7_17_1312', 'embryo_E7_17_1313', 'embryo_E7_17_1314', 'embryo_E7_17_1315', 'embryo_E7_17_1316', 'embryo_E7_17_1317', 'embryo_E7_17_1318', 'embryo_E7_17_1320', 'embryo_E7_17_1321', 'embryo_E7_17_1323', 'embryo_E7_17_1324', 'embryo_E7_17_1326', 'embryo_E7_17_1327', 'embryo_E7_17_1328', 'embryo_E7_17_1329', 'embryo_E7_17_1330', 'embryo_E7_17_1332', 'embryo_E7_17_1333', 'embryo_E7_17_1334', 'embryo_E7_17_1335', 'embryo_E7_17_1336', 'embryo_E7_17_1337', 'embryo_E7_17_1338', 'embryo_E7_17_1339', 'embryo_E7_17_1340', 'embryo_E7_17_1341', 'embryo_E7_17_1342', 'embryo_E7_17_1343', 'embryo_E7_17_1344', 'embryo_E7_17_1345', 'embryo_E7_17_1346', 'embryo_E7_17_1347', 'embryo_E7_17_1348', 'embryo_E7_17_1349', 'embryo_E7_17_1350', 'embryo_E7_17_1351', 'embryo_E7_17_1352', 'embryo_E7_17_1353', 'embryo_E7_19_1538', 'embryo_E7_19_1539', 'embryo_E7_19_1542', 'embryo_E7_19_1543', 'embryo_E7_19_1544', 'embryo_E7_19_1545', 'embryo_E7_19_1546', 'embryo_E7_19_1547', 'embryo_E7_19_1548', 'embryo_E7_19_1549', 'embryo_E7_19_1550', 'embryo_E7_19_1551', 'embryo_E7_19_1552', 'embryo_E7_19_1553', 'embryo_E7_19_1554', 'embryo_E7_19_1556', 'embryo_E7_19_1564', 'embryo_E7_19_1565', 'embryo_E7_19_1566', 'embryo_E7_19_1568', 'embryo_E7_19_1569', 'embryo_E7_2_138', 'embryo_E7_2_139', 'embryo_E7_2_141', 'embryo_E7_2_142', 'embryo_E7_2_144', 'embryo_E7_2_145', 'embryo_E7_2_146', 'embryo_E7_2_147', 'embryo_E7_2_148', 'embryo_E7_2_149', 'embryo_E7_2_150', 'embryo_E7_2_151', 'embryo_E7_2_152', 'embryo_E7_2_153', 'embryo_E7_2_154', 'embryo_E7_2_155', 'embryo_E7_2_156', 'embryo_E7_2_157', 'embryo_E7_2_158', 'embryo_E7_2_159', 'embryo_E7_2_160', 'embryo_E7_2_161', 'embryo_E7_2_162', 'embryo_E7_2_163', 'embryo_E7_2_164', 'embryo_E7_2_165', 'embryo_E7_2_166', 'embryo_E7_3_167', 'embryo_E7_3_168', 'embryo_E7_3_170', 'embryo_E7_3_171', 'embryo_E7_3_172', 'embryo_E7_3_173', 'embryo_E7_3_174', 'embryo_E7_3_175', 'embryo_E7_3_176', 'embryo_E7_3_177', 'embryo_E7_3_178', 'embryo_E7_3_179', 'embryo_E7_3_181', 'embryo_E7_3_182', 'embryo_E7_3_183', 'embryo_E7_3_184', 'embryo_E7_3_185', 'embryo_E7_3_186', 'embryo_E7_3_187', 'embryo_E7_3_188', 'embryo_E7_3_189', 'embryo_E7_3_190', 'embryo_E7_4_191', 'embryo_E7_4_192', 'embryo_E7_4_193_1', 'embryo_E7_4_193_2', 'embryo_E7_4_194', 'embryo_E7_4_195', 'embryo_E7_4_196', 'embryo_E7_4_197', 'embryo_E7_4_198', 'embryo_E7_4_200', 'embryo_E7_4_202', 'embryo_E7_4_203', 'embryo_E7_4_204', 'embryo_E7_4_205', 'embryo_E7_4_206', 'embryo_E7_4_207', 'embryo_E7_4_208', 'embryo_E7_4_209', 'embryo_E7_4_210', 'embryo_E7_4_211', 'embryo_E7_4_212', 'embryo_E7_4_213', 'embryo_E7_4_214', 'embryo_E7_4_216', 'embryo_E7_4_217', 'embryo_E7_4_218', 'embryo_E7_4_219', 'embryo_E7_4_220', 'embryo_E7_4_221', 'embryo_E7_4_222', 'embryo_E7_4_223', 'embryo_E7_4_224', 'embryo_E7_4_225', 'embryo_E7_4_226', 'embryo_E7_4_227', 'embryo_E7_4_228', 'embryo_E7_4_229', 'embryo_E7_4_230', 'embryo_E7_5_231', 'embryo_E7_5_232', 'embryo_E7_5_233', 'embryo_E7_5_235', 'embryo_E7_5_237', 'embryo_E7_5_240', 'embryo_E7_5_241', 'embryo_E7_5_243', 'embryo_E7_5_245', 'embryo_E7_5_246', 'embryo_E7_6_247', 'embryo_E7_6_248', 'embryo_E7_6_249', 'embryo_E7_6_250', 'embryo_E7_6_251', 'embryo_E7_6_252', 'embryo_E7_6_253', 'embryo_E7_6_254', 'embryo_E7_6_255', 'embryo_E7_6_256', 'embryo_E7_6_257', 'embryo_E7_6_258', 'embryo_E7_6_259', 'embryo_E7_6_260', 'embryo_E7_6_261', 'embryo_E7_6_262', 'embryo_E7_6_263', 'embryo_E7_6_264', 'embryo_E7_6_265', 'embryo_E7_6_266', 'embryo_E7_6_267', 'embryo_E7_6_273', 'embryo_E7_6_274', 'embryo_E7_6_275', 'embryo_E7_6_276', 'embryo_E7_6_278', 'embryo_E7_6_279', 'embryo_E7_7_280', 'embryo_E7_7_281', 'embryo_E7_7_282', 'embryo_E7_7_283', 'embryo_E7_7_284', 'embryo_E7_7_285', 'embryo_E7_7_286', 'embryo_E7_7_291', 'embryo_E7_7_292', 'embryo_E7_7_293', 'embryo_E7_7_294', 'embryo_E7_7_298', 'embryo_E7_7_299', 'embryo_E7_7_300', 'embryo_E7_7_301', 'embryo_E7_7_302', 'embryo_E7_7_303', 'embryo_E7_7_307', 'embryo_E7_7_308', 'embryo_E7_7_309', 'embryo_E7_7_310', 'embryo_E7_8_311', 'embryo_E7_8_312', 'embryo_E7_8_313', 'embryo_E7_8_314', 'embryo_E7_8_315', 'embryo_E7_8_316', 'embryo_E7_8_317', 'embryo_E7_8_318', 'embryo_E7_8_319', 'embryo_E7_8_320', 'embryo_E7_8_321', 'embryo_E7_8_322', 'embryo_E7_8_323', 'embryo_E7_8_324', 'embryo_E7_8_325', 'embryo_E7_8_327', 'embryo_E7_8_328', 'embryo_E7_8_329', 'embryo_E7_8_330', 'embryo_E7_8_331', 'embryo_E7_8_333', 'embryo_E7_8_335', 'embryo_E7_8_339', 'embryo_E7_8_340', 'embryo_E7_8_341', 'embryo_E7_8_342', 'embryo_E7_8_343', 'embryo_E7_8_344', 'embryo_E7_8_347', 'embryo_E7_8_348', 'embryo_E7_8_350', 'embryo_E7_9_531', 'embryo_E7_9_532', 'embryo_E7_9_534', 'embryo_E7_9_535', 'embryo_E7_9_536', 'embryo_E7_9_537', 'embryo_E7_9_538', 'embryo_E7_9_539', 'embryo_E7_9_540', 'embryo_E7_9_541', 'embryo_E7_9_542', 'embryo_E7_9_543', 'embryo_E7_9_544', 'embryo_E7_9_545', 'embryo_E7_9_546', 'embryo_E7_9_547', 'embryo_E7_9_548', 'embryo_E7_9_549', 'embryo_E7_9_550', 'embryo_E7_9_551', 'embryo_E7_9_554', 'embryo_E7_9_555', 'embryo_E7_9_556', 'embryo_E7_9_557', 'embryo_E7_9_558', 'embryo_E7_9_559', 'embryo_E7_9_560', 'embryo_E7_9_561', 'embryo_E7_9_562', 'embryo_E7_9_563', 'embryo_E7_9_564', 'embryo_E7_9_565', 'embryo_E7_9_567', 'embryo_E7_9_568', 'embryo_E7_9_569', 'embryo_E7_9_570', 'embryo_E7_9_571', 'embryo_E7_9_573', 'embryo_E7_9_574', ],
    ['Endometrial_stromal_cells_rp1', 'Endometrial_stromal_cells_rp2', 'Endometrial_stroma_rp1', 'Endometrial_stroma_rp2'],
    ['Endometrial_stroma_rp1', 'Endometrial_stroma_rp2'],
    ['endometrial_stromal_fibroblasts_rp1', 'endometrial_stromal_fibroblasts_rp2'],
    ['Eosophageal_tissue_rp1', 'Eosophageal_tissue_rp2', 'Eosophageal_tissue_rp3', 'Eosophageal_tissue_rp4', 'Eosophageal_tissue_rp5', 'Eosophageal_tissue_rp6'],
    ['epithelium_breast_rp1', 'epithelium_breast_rp2', 'epithelium_breast_rp3', 'epithelium_breast_rp4'],
    ['Esophagus_rp1', 'Esophagus_rp2'],
    ['esophagogastric_junction_rp1', 'esophagogastric_junction_rp2', 'esophagogastric_junction_rp3', 'esophagogastric_junction_rp4'],
    ['esophagus_muscularis_mucosa_rp1', 'esophagus_muscularis_mucosa_rp2', 'esophagus_muscularis_mucosa_rp3', 'esophagus_muscularis_mucosa_rp4'],
    ['esophagus_squamous_epithelium_rp1', 'esophagus_squamous_epithelium_rp2', 'esophagus_squamous_epithelium_rp3', 'esophagus_squamous_epithelium_rp4'],
    ['Epidermal_keratinocytes_rp1', 'Epidermal_keratinocytes_rp2', 'Epidermal_keratinocytes_rp3', 'Epidermal_keratinocytes_rp4', 'Epidermal_keratinocytes_rp5'],# sample 6 has a problem, I take the majority vote 'Epidermal_keratinocytes_rp6'],
    ['Epidermal_melanocytes_rp1', 'Epidermal_melanocytes_rp2', 'epidermal_melanocytes_rp3', 'epidermal_melanocytes_rp4', 'epidermal_melanocytes_rp5'],
    ['Epidermal_melanocytes_juvenile_rp1', 'Epidermal_melanocytes_juvenile_rp2'],
    ['Erythroid_progenitor_rp1', 'Erythroid_progenitor_rp2', 'Erythroid_progenitor_rp3'],
    ['fatpad_omental_rp1', 'fatpad_omental_rp2', 'fatpad_omental_rp3', 'fatpad_omental_rp4'],
    ['Fetal_retinal_pigment_epithelium_rp1', 'Fetal_retinal_pigment_epithelium_rp2', 'Fetal_retinal_pigment_epithelium_rp3'],
    ['follicular_dendritic_cells_cultured_rp1', 'follicular_dendritic_cells_cultured_rp2', 'follicular_dendritic_cells_cultured_rp3'],
    ['Gastric_tissue_rp1', 'Gastric_tissue_rp2'],
    ['gastric_epthelial_cells_rp1', 'gastric_epthelial_cells_rp2'],
    ['gastrocnemius_medialis_rp1', 'gastrocnemius_medialis_rp2', 'gastrocnemius_medialis_rp3', 'gastrocnemius_medialis_rp4'],
    ['germinal_B_cells_rp1', 'germinal_B_cells_rp2', 'germinal_B_cells_rp3', 'germinal_B_cells_rp4'],
    ['Granulocytes_rp1', 'Granulocytes_rp2'],
    ['Gut_rp1', 'Gut_rp2'],
    ['Heart_rp1', 'Heart_rp2', 'Heart_rp3', 'Heart_rp4', 'Heart_rp5'],
    ['Hepatocyts_rp1', 'Hepatocyte_rp2'],
    ['hESC_cortical_neuron_d12_cortical_specification_rp1', 'hESC_cortical_neuron_d12_cortical_specification_rp2'],
    ['hESC_cortical_neuron_d19_cortical_specification_rp1', 'hESC_cortical_neuron_d19_cortical_specification_rp2', 'hESC_cortical_neuron_d19_cortical_specification_rp3', 'hESC_cortical_neuron_d19_cortical_specification_rp4'],
    ['hESC_cortical_neuron_d26_deep_layer_rp1', 'hESC_cortical_neuron_d26_deep_layer_rp2'],
    ['hESC_cortical_neuron_d33_deep_layer_rp1', 'hESC_cortical_neuron_d33_deep_layer_rp2'],
    ['hESC_cortical_neuron_d49_deep_layer_rp1', 'hESC_cortical_neuron_d49_deep_layer_rp2'],
    ['hESC_cortical_neuron_d63_upper_layer_rp1', 'hESC_cortical_neuron_d63_upper_layer_rp2'],
    ['hESC_cortical_neuron_d7_rp1', 'hESC_cortical_neuron_d7_rp2', 'hESC_cortical_neuron_d7_rp3', 'hESC_cortical_neuron_d7_rp4'],
    ['hESC_cortical_neuron_d77_upper_layer_rp1', 'hESC_cortical_neuron_d77_upper_layer_rp2'],
    ['hESC_H1_rp1', 'hESC_H1_rp2', 'hESC_H1_rp3', 'hESC_H1_rp4', 'hESC_H1_rp5', 'hESC_H1_rp6', 'hESC_H1_rp7', 'hESC_H1_rp8', 'hESC_H1_rp9', 'hESC_H1_rp10', 'hESC_H1_rp11', 'hESC_H1_rp12', 'hESC_H1_rp13', 'hESC_H1_rp14', 'hESC_H1_rp16', 'hESC_H1_rp17', 'hESC_h1_rp18', 'hESC_h1_rp19','hESC_cortical_neuron_d0_hESC_rp1', 'hESC_cortical_neuron_d0_hESC_rp3', 'hESC_cortical_neuron_d0_hESC_rp4','hESC_liver_diff_d0_hESC_rp1'],
    ['hESCs_3iL_rp1', 'hESCs_3iL_rp2', 'hESCs_3iL_rp3'],
    ['hESCs_H1_rp18', 'hESCs_H1_rp19', 'hESCs_H1_rp20'], # Singapore: H1 WA-01
    ['Human_skeletal_muscle_myoblasts_rp1', 'Human_skeletal_muscle_myoblasts_rp2', 'Human_skeletal_muscle_myoblasts_rp3'],
    ['Ileum_rp1', 'Ileum_rp2', 'Ileum_rp4', 'Ileum_rp5', 'Ileum_rp6', 'Ileum_rp7', 'Ileum_rp8', 'Ileum_rp10', 'Ileum_rp11', 'Ileum_rp12', 'Ileum_rp14', 'Ileum_rp15', 'Ileum_rp16', 'Ileum_rp17', 'Ileum_rp18', 'Ileum_rp19', 'Ileum_rp20', 'Ileum_rp21', 'Ileum_rp22', 'Ileum_rp23', 'Ileum_rp24', 'Ileum_rp25', 'Ileum_rp26', 'Ileum_rp27', 'Ileum_rp28', 'Ileum_rp29', 'Ileum_rp30', 'Ileum_rp31', 'Ileum_rp32', 'Ileum_rp33', 'Ileum_rp34', 'Ileum_rp35', 'Ileum_rp36', 'Ileum_rp37', 'Ileum_rp38', 'Ileum_rp39', 'Ileum_rp40', 'Ileum_rp41', 'Ileum_rp42', 'Ileum_rp43'],
    ['iMSC_rp1', 'iMSC_rp2'],
    ['induced_cortical_neuron_rp1', 'induced_cortical_neuron_rp2', 'induced_cortical_neuron_rp3'],
    ['invitro_DA_neurons_rp1', 'invitro_DA_neurons_rp2', 'invitro_DA_neurons_rp3', 'invitro_DA_neurons_rp4'],
    ['invitro_DA_neurons_PD_pat1_rp1','invitro_DA_neurons_PD_pat1_rp2','invitro_DA_neurons_PD_pat2_rp1','invitro_DA_neurons_PD_pat2_rp2','invitro_DA_neurons_PD_pat3_rp1','invitro_DA_neurons_PD_pat3_rp2','invitro_DA_neurons_PD_pat4_rp1','invitro_DA_neurons_PD_pat4_rp2','invitro_DA_neurons_PD_pat5_rp1','invitro_DA_neurons_PD_pat5_rp2','invitro_DA_neurons_sporadicPD_rp1','invitro_DA_neurons_sporadicPD_rp2','invitro_DA_neurons_twin_PD_rp1','invitro_DA_neurons_twin_PD_rp2','invitro_DA_neurons_twin_PD_rp3','invitro_DA_neurons_twin_PD_rp4'],
    ['invitro_DA_neurons_WT_pat1_rp1','invitro_DA_neurons_WT_pat1_rp2','invitro_DA_neurons_WT_pat2_rp1','invitro_DA_neurons_WT_pat2_rp2','invitro_DA_neurons_WT_pat3_rp1','invitro_DA_neurons_WT_pat3_rp2','invitro_DA_neurons_WT_pat4_rp1','invitro_DA_neurons_WT_pat4_rp2','invitro_DA_neurons_WT_pat5_rp1','invitro_DA_neurons_WT_pat5_rp2'],
    ['invitro_DA_neurons_twin_nonPD_rp1','invitro_DA_neurons_twin_nonPD_rp2','invitro_DA_neurons_twin_nonPD_rp3','invitro_DA_neurons_twin_nonPD_rp4'],
    ['invitro_da_neuron_lzwC11_rp1','invitro_da_neuron_lzwC14_rp1','invitro_da_neuron_lzwC21_rp1','invitro_da_neuron_lzwC2921_rp1','invitro_da_neuron_lzwC2924_rp1','invitro_da_neuron_lzwC3859_rp1','invitro_da_neuron_lzwC3880_rp1','invitro_da_neuron_lzwC46_rp1','invitro_da_neuron_lzwC5_rp1'],
    ['IVD_enteric_neural_crest_rp1', 'IVD_enteric_neural_crest_rp2', 'IVD_enteric_neural_crest_rp3'],
    ['IVD_melanocyte_rp1', 'IVD_melanocyte_rp2', 'IVD_melanocyte_rp3'],
    ['IVD_neural_crest_rp1', 'IVD_neural_crest_rp2', 'IVD_neural_crest_rp3'],
    ['iPSC_reprogramming_CD34pCB_iPSC_rp1', 'iPSC_reprogramming_CD34pCB_iPSC_rp2', 'iPSC_reprogramming_CD34pCB_iPSC_rp3'],
    ['iPSC_reprogramming_hIFT_D10_rp1', 'iPSC_reprogramming_hIFT_D10_rp2', 'iPSC_reprogramming_hIFT_D10_rp3'],
    ['iPSC_reprogramming_hIFT_D10_SSEA3n_rp1', 'iPSC_reprogramming_hIFT_D10_SSEA3n_rp2', 'iPSC_reprogramming_hIFT_D10_SSEA3n_rp3'],
    ['iPSC_reprogramming_hIFT_D10_SSEA3p_rp1', 'iPSC_reprogramming_hIFT_D10_SSEA3p_rp2', 'iPSC_reprogramming_hIFT_D10_SSEA3p_rp3', 'iPSC_reprogramming_hIFT_D10_SSEA3p_rp4', 'iPSC_reprogramming_hIFT_D10_SSEA3p_rp5'],
    ['iPSC_reprogramming_hIFT_D14_rp1', 'iPSC_reprogramming_hIFT_D14_rp2', 'iPSC_reprogramming_hIFT_D14_rp3'],
    ['iPSC_reprogramming_hIFT_D14_SSEA3n_rp1', 'iPSC_reprogramming_hIFT_D14_SSEA3n_rp2', 'iPSC_reprogramming_hIFT_D14_SSEA3n_rp3'],
    ['iPSC_reprogramming_hIFT_D14_SSEA3p_rp1', 'iPSC_reprogramming_hIFT_D14_SSEA3p_rp2', 'iPSC_reprogramming_hIFT_D14_SSEA3p_rp3', 'iPSC_reprogramming_hIFT_D14_SSEA3p_rp4', 'iPSC_reprogramming_hIFT_D14_SSEA3p_rp5'],
    ['iPSC_reprogramming_hIFT_D2_rp1', 'iPSC_reprogramming_hIFT_D2_rp2', 'iPSC_reprogramming_hIFT_D2_rp3', 'iPSC_reprogramming_hIFT_D2_rp4', 'iPSC_reprogramming_hIFT_D2_rp5'],
    ['iPSC_reprogramming_hIFT_D20_TRA160n_rp1', 'iPSC_reprogramming_hIFT_D20_TRA160n_rp2', 'iPSC_reprogramming_hIFT_D20_TRA160n_rp3', 'iPSC_reprogramming_hIFT_D20_TRA160n_rp4'],
    ['iPSC_reprogramming_hIFT_D20_TRA160p_rp1', 'iPSC_reprogramming_hIFT_D20_TRA160p_rp2', 'iPSC_reprogramming_hIFT_D20_TRA160p_rp3', 'iPSC_reprogramming_hIFT_D20_TRA160p_rp4', 'iPSC_reprogramming_hIFT_D20_TRA160p_rp5'],
    ['iPSC_reprogramming_hIFT_D24_TRA160n_rp1', 'iPSC_reprogramming_hIFT_D24_TRA160n_rp2', 'iPSC_reprogramming_hIFT_D24_TRA160n_rp3', 'iPSC_reprogramming_hIFT_D24_TRA160n_rp4', 'iPSC_reprogramming_hIFT_D24_TRA160n_rp5', 'iPSC_reprogramming_hIFT_D24_TRA160n_rp6'],
    ['iPSC_reprogramming_hIFT_D24_TRA160p_rp1', 'iPSC_reprogramming_hIFT_D24_TRA160p_rp2', 'iPSC_reprogramming_hIFT_D24_TRA160p_rp3', 'iPSC_reprogramming_hIFT_D24_TRA160p_rp4'],
    ['iPSC_reprogramming_hIFT_D5_rp1', 'iPSC_reprogramming_hIFT_D5_rp2', 'iPSC_reprogramming_hIFT_D5_rp3', 'iPSC_reprogramming_hIFT_D5_rp4', 'iPSC_reprogramming_hIFT_D5_rp5', 'iPSC_reprogramming_hIFT_D5_rp6', 'iPSC_reprogramming_hIFT_D5_rp7', 'iPSC_reprogramming_hIFT_D5_rp8', 'iPSC_reprogramming_hIFT_D5_rp9'],
    ['iPSC_reprogramming_hIFT_D8_rp1', 'iPSC_reprogramming_hIFT_D8_rp2', 'iPSC_reprogramming_hIFT_D8_rp3', 'iPSC_reprogramming_hIFT_D8_rp4'],
    ['Keratinocytes_rp1', 'Keratinocytes_rp2', 'Keratinocytes_rp3'],
    ['keratinocyte_differentiated_rp1', 'keratinocyte_differentiated_rp2', 'keratinocyte_differentiated_rp3', 'keratinocyte_precursor_rp1', 'keratinocyte_precursor_rp2', 'keratinocyte_precursor_rp3'],
    ['Kidney_rp1', 'Kidney_rp3'],
    ['Late_basophilic_erythroblast_rp1', 'Late_basophilic_erythroblast_rp2', 'Late_basophilic_erythroblast_rp3', 'Late_basophilic_erythroblast_rp4', 'Late_basophilic_erythroblast_rp5', 'Late_basophilic_erythroblast_rp6'],
    ['Late_basophilic_erythroblast_rp1', 'Late_basophilic_erythroblast_rp2', 'Late_basophilic_erythroblast_rp3'],
    ['Late_blastocyst_E1_C10_pTE', 'Late_blastocyst_E1_C11_pTE', 'Late_blastocyst_E1_C2_pTE', 'Late_blastocyst_E1_C3_pTE', 'Late_blastocyst_E1_C5_pTE', 'Late_blastocyst_E1_C8_pTE', 'Late_blastocyst_E2_C10_pTE',],
    ['Late_blastocyst_E1_C4_mTE', 'Late_blastocyst_E1_C12_mTE', 'Late_blastocyst_E1_C6_mTE', 'Late_blastocyst_E1_C7_mTE', 'Late_blastocyst_E1_C9_mTE', 'Late_blastocyst_E2_C4_mTE', 'Late_blastocyst_E2_C5_mTE', 'Late_blastocyst_E2_C6_mTE', 'Late_blastocyst_E2_C7_mTE', ],
    ['Late_blastocyst_E2_C1_EPI', 'Late_blastocyst_E2_C2_EPI', 'Late_blastocyst_E2_C3_EPI', 'Late_blastocyst_E2_C8_EPI', 'Late_blastocyst_E3_C1_EPI'],
    ['Late_blastocyst_E3_C2_PE', 'Late_blastocyst_E3_C3_PE', 'Late_blastocyst_E3_C4_PE', 'Late_blastocyst_E3_C5_PE', 'Late_blastocyst_E3_C6_PE', 'Late_blastocyst_E3_C7_PE', 'Late_blastocyst_E3_C8_PE'],
    ['Liver_rp1', 'Liver_rp2', 'Liver_rp3', 'Liver_rp4', 'Liver_rp5', 'Liver_rp6'],
    ['Lung_rp1', 'Lung_rp2', 'Lung_rp3'],
    ['Lung_IPF_rp1', 'Lung_IPF_rp2', 'Lung_IPF_rp3', 'Lung_IPF_rp4', 'Lung_IPF_rp5', 'Lung_IPF_rp6', 'Lung_IPF_rp7', 'Lung_IPF_rp8'],
    ['Lung_fibroblast_rp1', 'Lung_fibroblast_rp2'],
    ['Lung_normal_rp1', 'Lung_normal_rp2', 'Lung_normal_rp3', 'Lung_normal_rp4', 'Lung_normal_rp5', 'Lung_normal_rp6', 'Lung_normal_rp7'],
    ['Lymph_node_rp1', 'Lymph_node_rp2'],
    ['lymphatic_endothelial_cell_rp1', 'lymphatic_endothelial_cell_rp2'],
    ['Macrophage_M1_rp1', 'Macrophage_M1_rp2', 'Macrophage_M1_rp3'],
    ['Macrophage_M2_rp1', 'Macrophage_M2_rp2', 'Macrophage_M2_rp3'],
    ['Mammary_epithelial_cells_rp1', 'Mammary_epithelial_cells_rp2'],
    ['mesoderm_invitro_rp1', 'mesoderm_invitro_rp2', 'mesoderm_invitro_rp3', 'mesoderm_invitro_rp4', 'mesoderm_invitro_rp5', 'mesoderm_invitro_rp6'],
    ['Microvascular_endothelial_cells_rp1', 'Microvascular_endothelial_cells_rp2'],
    ['microglia_adult_rp1', 'microglia_adult_rp2', 'microglia_adult_rp3'],
    ['microglia_fetal_rp1', 'microglia_fetal_rp2', 'microglia_fetal_conditioned_medium_rp1',],
    ['microglia_induced_rp1', 'microglia_induced_rp2', 'microglia_induced_rp3', 'microglia_induced_rp4', 'microglia_induced_rp5', 'microglia_induced_rp6', 'microglia_induced_conditioned_medium_rp1', 'microglia_induced_conditioned_medium_rp2', 'microglia_induced_conditioned_medium_rp3'],
    ['Monocytes_rp1', 'Monocytes_rp2', 'Monocytes_rp3', 'Monocytes_rp4', 'Monocytes_rp5', 'Monocytes_rp6', 'Monocytes_rp7', 'Monocytes_rp8'],
    ['Monocytes_CD14p_rp1', 'Monocytes_CD14p_rp2', 'Monocytes_CD14p_rp3', 'Monocytes_CD14p_rp4', 'Monocytes_CD14p_rp5', 'Monocytes_CD14p_rp6'],
    ['Mononuclear_cells_peripheral_blood_rp1', 'Mononuclear_cells_peripheral_blood_rp2'],
    ['Morula_rp1', 'Morula_rp2', 'Morula_rp3'],
    ['Morula_E1_C1', 'Morula_E1_C2', 'Morula_E1_C4', 'Morula_E1_C5', 'Morula_E1_C6', 'Morula_E1_C7', 'Morula_E2_C1', 'Morula_E2_C2', 'Morula_E2_C3', 'Morula_E2_C4', 'Morula_E2_C5', 'Morula_E2_C6', 'Morula_E2_C7', 'Morula_E2_C8'],
    ['Motor_neuron_sod_av4p_rp1', 'Motor_neuron_sod_av4p_rp2'],
    ['Motor_neuron_sod_pp_rp1', 'Motor_neuron_sod_pp_rp2', 'Motor_neuron_sod_pp_rp3'],
    ['MSC_adipose_rp1', 'MSC_adipose_rp2'],
    ['MSC_bone_marrow_rp1', 'MSC_bone_marrow_rp2'],
    ['MSC_umbilical_cord_rp1', 'MSC_umbilical_cord_rp2'],
    ['Mural_granulosa_rp1', 'Mural_granulosa_rp2', 'Mural_granulosa_rp3'],
    ['Myometrium_labour_rp1', 'Myometrium_labour_rp2', 'Myometrium_labour_rp3', 'Myometrium_labour_rp4', 'Myometrium_labour_rp5'],
    ['Myometrium_no_labour_rp1', 'Myometrium_no_labour_rp2', 'Myometrium_no_labour_rp3', 'Myometrium_no_labour_rp4', 'Myometrium_no_labour_rp5'],
    ['naive_B_cells_rp1', 'naive_B_cells_rp2', 'naive_B_cells_rp3', 'naive_B_cells_rp4', 'naive_B_cells_rp5'],
    ['neocortex_cortical_plate_rp1', 'neocortex_cortical_plate_rp2', 'neocortex_cortical_plate_rp3', 'neocortex_cortical_plate_rp4', 'neocortex_cortical_plate_rp5', 'neocortex_cortical_plate_rp6'],
    ['neocortex_inner_subventricular_zone_rp1', 'neocortex_inner_subventricular_zone_rp2', 'neocortex_inner_subventricular_zone_rp3', 'neocortex_inner_subventricular_zone_rp4', 'neocortex_inner_subventricular_zone_rp5', 'neocortex_inner_subventricular_zone_rp6'],
    ['neocortex_outer_subventricular_zone_rp1', 'neocortex_outer_subventricular_zone_rp2', 'neocortex_outer_subventricular_zone_rp3', 'neocortex_outer_subventricular_zone_rp4', 'neocortex_outer_subventricular_zone_rp5', 'neocortex_outer_subventricular_zone_rp6'],
    ['neocortex_ventricular_zone_rp1', 'neocortex_ventricular_zone_rp2', 'neocortex_ventricular_zone_rp3', 'neocortex_ventricular_zone_rp4', 'neocortex_ventricular_zone_rp5', 'neocortex_ventricular_zone_rp6'],
    ['Neutrophil_rp1', 'Neutrophil_rp2'],
    ['NPC_rp1', 'NPC_rp2', 'NPC_rp3'],
    ['Oocyte_rp1', 'Oocyte_rp2', 'Oocyte_rp3'],
    ['oligodendrocyte_rp1', 'oligodendrocyte_rp2', 'oligodendrocyte_rp3', 'oligodendrocyte_rp4'],
    ['Placenta_rp61', 'Placenta_rp62'],
    ['Hair_follicle_dermal_papilla_rp1', 'Hair_follicle_dermal_papilla_rp2'],
    ['Oocyte_E1_C1', 'Oocyte_E2_C1', 'Oocyte_E3_C1'],
    ['Orthochromatic_erythroblast_rp1', 'Orthochromatic_erythroblast_rp2', 'Orthochromatic_erythroblast_rp3', 'Orthochromatic_erythroblast_rp4', 'Orthochromatic_erythroblast_rp5', 'Orthochromatic_erythroblast_rp6'],
    ['Osteoblasts_rp1', 'Osteoblasts_rp2', 'Osteoblasts_rp3', 'Osteoblasts_rp4', 'Osteoblasts_rp5', 'Osteoblasts_rp6', 'Osteoblasts_rp7', 'Osteoblasts_rp8', 'Osteoblasts_rp9', 'Osteoblasts_rp10'],
    ['Ovary_rp1', 'Ovary_rp2'],
    ['Pancreatic_bud_rp1', 'Pancreatic_bud_rp2'],
    ['Pancreatic_bud_invitro_rp1', 'Pancreatic_bud_invitro_rp2'],
    ['Pancreatic_islets_rp1', 'Pancreatic_islets_rp2', 'Pancreatic_islets_rp3', 'Pancreatic_islets_rp4', 'Pancreatic_islets_rp5', 'Pancreatic_islets_rp6', 'Pancreatic_islets_rp7', 'Pancreatic_islets_rp8', 'Pancreatic_islets_rp9', 'Pancreatic_islets_rp10'],
    ['Placental_epithelial_rp1', 'Placental_epithelial_rp2'],
    ['Placental_pericytes_rp1', 'Placental_pericytes_rp2'],
    ['Platelets_rp1', 'Platelets_rp2', 'Platelets_rp3', 'Platelets_rp4'],
    ['Polychromatic_erythroblast_rp1', 'Polychromatic_erythroblast_rp2', 'Polychromatic_erythroblast_rp3', 'Polychromatic_erythroblast_rp4', 'Polychromatic_erythroblast_rp5', 'Polychromatic_erythroblast_rp6'],
    ['Proerythroblast_rp1', 'Proerythroblast_rp2', 'Proerythroblast_rp3', 'Proerythroblast_rp4', 'Proerythroblast_rp5', 'Proerythroblast_rp6'],
    ['Pronuclei_rp1', 'Pronuclei_rp2', 'Pronuclei_rp3'],
    ['Prostate_rp1', 'Prostate_rp2', 'Prostate_rp3', 'Prostate_rp4', 'Prostate_rp5', 'Prostate_rp6', 'Prostate_rp7', 'Prostate_rp8', 'Prostate_rp9', 'Prostate_rp11', 'Prostate_rp12'],
    ['Radial_glial_early_rp1', 'Radial_glial_early_rp2'],
    ['Radial_glial_late_rp1', 'Radial_glial_late_rp2', 'Radial_glial_late_rp3'],
    ['Radial_glial_mid_rp1', 'Radial_glial_mid_rp2'],
    ['Retina_rp1', 'Retina_rp2'], # Same study, same lab, but # 3 is an outlier from the other two...
    ['Saphenous_vein_endothelial_cells_rp1', 'Saphenous_vein_endothelial_cells_rp2'],
    ['Skeletal_muscle_rp1', 'Skeletal_muscle_rp2', 'Skeletal_muscle_rp3', 'Skeletal_muscle_cells_rp3', 'Skeletal_muscle_cells_rp4', 'Skeletal_muscle_cells_rp5', 'Skeletal_muscle_cells_rp6', 'Skeletal_muscle_cells_rp7', 'Skeletal_muscle_cells_rp8', 'Skeletal_muscle_cells_rp9', 'Skeletal_muscle_cells_rp10', 'Skeletal_muscle_cells_rp11', 'Skeletal_muscle_cells_rp12', 'Skeletal_muscle_cells_rp13', 'Skeletal_muscle_cells_rp14', 'Skeletal_muscle_cells_rp15', 'Skeletal_muscle_cells_rp16', 'Skeletal_muscle_cells_rp17', 'Skeletal_muscle_cells_rp18', 'Skeletal_muscle_cells_rp19', 'Skeletal_muscle_cells_rp20', 'Skeletal_muscle_cells_rp21', 'Skeletal_muscle_cells_rp22', 'Skeletal_muscle_cells_rp23', 'Skeletal_muscle_cells_rp24', 'Skeletal_muscle_cells_rp25', 'Skeletal_muscle_cells_rp26', 'Skeletal_muscle_cells_rp27'],
    ['Skeletal_muscle_myotube_rp1', 'Skeletal_muscle_myotube_rp2'],
    ['Sperm_rp1', 'Sperm_rp2', 'Sperm_rp4', 'Sperm_rp5'],
    ['stomach_rp1', 'stomach_rp2' ,'stomach_rp3', 'stomach_rp4'],
    ['Testes_rp1', 'Testes_rp2'],
    ['Thyroid_rp1', 'Thyroid_rp2'],
    ['trophoblast_invitro_rp1', 'trophoblast_invitro_rp2'],
    ['Umbilical_vein_endothelial_cells_rp1', 'Umbilical_vein_endothelial_cells_rp2'],
    ['Villious_mesenchymal_fibroblasts_rp1', 'Villious_mesenchymal_fibroblasts_rp2'],
    ['White_preadipocytes_rp1', 'White_preadipocytes_rp2'],
    ['Zygote_rp1', 'Zygote_rp2', 'Zygote_E1_C1', 'Zygote_E2_C1', 'Zygote_E3_C1'],

    ['primed_hESC_ELF1_rp1', 'primed_hESC_ELF1_rp2', 'primed_hESC_ELF1_rp3'],

    ['myofibroblasts_rp1', 'myofibroblasts_rp2', 'myofibroblasts_rp3'],
    ['myometrial_cells_cultured_rp1', 'myometrial_cells_cultured_rp2', 'myometrial_cells_cultured_rp3', 'myometrial_cells_cultured_rp4'],


    ['SS_Blastocyst_Epiblast_rp13',    'SS_Blastocyst_Epiblast_rp14',
    'SS_Blastocyst_Epiblast_rp15',    'SS_Blastocyst_Epiblast_rp16',
    'SS_Blastocyst_Epiblast_rp17',    'SS_Blastocyst_Epiblast_rp18',
    'SS_Blastocyst_Epiblast_rp19',    'SS_Blastocyst_Epiblast_rp20',
    'SS_Blastocyst_Epiblast_rp21',    'SS_Blastocyst_Epiblast_rp22',
    'SS_Blastocyst_Epiblast_rp23',    'SS_Blastocyst_Epiblast_rp24',
    'SS_Blastocyst_Epiblast_rp25',    'SS_Blastocyst_Epiblast_rp26',
    'SS_Blastocyst_Epiblast_rp27',    'SS_Blastocyst_Epiblast_rp28',
    'SS_Blastocyst_Epiblast_rp29',    'SS_Blastocyst_Epiblast_rp30',
    'SS_Blastocyst_Epiblast_rp31',    'SS_Blastocyst_Epiblast_rp32',
    'SS_Blastocyst_Epiblast_rp33',    'SS_Blastocyst_Epiblast_rp34',
    'SS_Blastocyst_Epiblast_rp35',    'SS_Blastocyst_Epiblast_rp36'],
    ['SS_Blastocyst_Primitive_Endoderm_rp1',    'SS_Blastocyst_Primitive_Endoderm_rp10',
    'SS_Blastocyst_Primitive_Endoderm_rp11',    'SS_Blastocyst_Primitive_Endoderm_rp12',
    'SS_Blastocyst_Primitive_Endoderm_rp18',    'SS_Blastocyst_Primitive_Endoderm_rp19',    'SS_Blastocyst_Primitive_Endoderm_rp2',
    'SS_Blastocyst_Primitive_Endoderm_rp20',    'SS_Blastocyst_Primitive_Endoderm_rp21',    'SS_Blastocyst_Primitive_Endoderm_rp22',
    'SS_Blastocyst_Primitive_Endoderm_rp3',    'SS_Blastocyst_Primitive_Endoderm_rp4',    'SS_Blastocyst_Primitive_Endoderm_rp5',
    'SS_Blastocyst_Primitive_Endoderm_rp6',    'SS_Blastocyst_Primitive_Endoderm_rp7',    'SS_Blastocyst_Primitive_Endoderm_rp8',
    'SS_Blastocyst_Primitive_Endoderm_rp9'],
    ['SS_Blastocyst_Trophectoderm_rp1',    'SS_Blastocyst_Trophectoderm_rp10',
    'SS_Blastocyst_Trophectoderm_rp11',    'SS_Blastocyst_Trophectoderm_rp12',
    'SS_Blastocyst_Trophectoderm_rp13',    'SS_Blastocyst_Trophectoderm_rp15',
    'SS_Blastocyst_Trophectoderm_rp16',    'SS_Blastocyst_Trophectoderm_rp17',
    'SS_Blastocyst_Trophectoderm_rp18',    'SS_Blastocyst_Trophectoderm_rp2',
    'SS_Blastocyst_Trophectoderm_rp20',    'SS_Blastocyst_Trophectoderm_rp21',
    'SS_Blastocyst_Trophectoderm_rp22',    'SS_Blastocyst_Trophectoderm_rp23',
    'SS_Blastocyst_Trophectoderm_rp3',    'SS_Blastocyst_Trophectoderm_rp4',
    'SS_Blastocyst_Trophectoderm_rp5',    'SS_Blastocyst_Trophectoderm_rp6',
    'SS_Blastocyst_Trophectoderm_rp7',    'SS_Blastocyst_Trophectoderm_rp8',    'SS_Blastocyst_Trophectoderm_rp9'],


    output_pears="Pearson_correlations.tsv",
    pearson_hist="Pearson_histogram.png",
    threshold=0.6,
    _ignore_missing_samples=True)

# pretify the condition names here:
pretty = []
for i in arr.getConditionNames():
    newi = i.replace("_rp1", "").replace("_", " ")
    if newi.endswith(" 1"):
        newi = newi.replace(" 1", "")
    pretty.append(newi)
arr.setConditionNames(pretty)

# It is possible to make it here with a mean_replicates genes that actually have zero in all columns.
# I thought that sort of case would be really rare. But unfortunately it's surprisingly common.
arr = arr.filter_low_expressed(10**1.6, 1)

mapped = ensg.map(key="ensg", genelist=arr)
mapped.strip_errs() # I probably want a error key containing version too...
print(list(mapped.keys()))
mapped.saveTSV("genes_ntc_expression.tsv", key_order=['ensg', 'name', 'transcript_type'], gzip=True)

# Clean out hanger on data
# ['loc', 'name', 'ensg', 'tss_loc', 'conditions', 'strand']
f = {"force_tsv": True, 'ensg': 0, 'name': 1, 'transcript_type': 2}
mapped = expression(filename='genes_ntc_expression.tsv', format=f, expn='column[3:]')
mapped.save("genes_ntc_expression.glb") # These are the final tables.

mapped = ensg.map(key="ensg", genelist=raw_expn)
mapped.save("genes_ntc_expression_nonmerged.glb")
mapped.saveTSV("genes_ntc_expression_nonmerged.tsv")
mapped.saveTSV("genes_ntc_expression_nonmerged.tsv", gzip=True)

arr.tree(filename="tree.png", color_threshold=0.0, label_size=5, size=(5,14))
print()
print("Num conditions =", len(arr.getConditionNames()))
print()
