"""

post EDASeq clean-up and annotation.


"""

import sys, os, glob
from glbase3 import *

user_path = os.path.expanduser("~")
ensg = glload(os.path.join("../hg38/hg38_gencode_ensg_tes_v32.glb"))

raw_expn = expression(filename="rawtags_gc_normed.tsv", format={"force_tsv": True, "skiplines": 0, "ensg": 0}, expn="column[1:]")
raw_expn.sort_conditions()

arr = raw_expn.mean_replicates(
    ['Adipose_1', 'Adipose_2'],
    ['Adrenal_gland_1', 'Adrenal_gland_2'],
    ['Airway_basal_cells_1', 'Airway_basal_cells_2', 'Airway_basal_cells_3', 'Airway_basal_cells_4', 'Airway_basal_cells_5', 'Airway_basal_cells_6', 'Airway_basal_cells_7', 'Airway_basal_cells_8', 'Airway_basal_cells_9', 'Airway_basal_cells_10', 'Airway_basal_cells_11', 'Airway_basal_cells_12', 'Airway_basal_cells_13', 'Airway_basal_cells_14', 'Airway_basal_cells_15', 'Airway_basal_cells_16', 'Airway_basal_cells_17', 'Airway_basal_cells_18', 'Airway_basal_cells_19', 'Airway_basal_cells_20', 'Airway_basal_cells_21', 'Airway_basal_cells_22', 'Airway_basal_cells_23', 'Airway_basal_cells_24', 'Airway_basal_cells_28', 'Airway_basal_cells_29', 'Airway_basal_cells_30'],
    ['Airway_smooth_muscle_1', 'Airway_smooth_muscle_2', 'Airway_smooth_muscle_3', 'Airway_smooth_muscle_4'],
    ['Aortic_adventitial_fibroblasts_1', 'Aortic_adventitial_fibroblasts_2'],
    ['Aortic_endothelial_cells_1', 'Aortic_endothelial_cells_2'],
    ['Astrocytes_1', 'Astrocytes_2'],
    ['B_cells_CD20p_1', 'B_cells_CD20p_2', 'B_cells_CD20p_3', 'B_cells_CD20p_4', 'B_cells_CD20p_5', 'B_cells_CD20p_6'],
    ['Bone_marrow_1', 'Bone_marrow_2', 'Bone_marrow_3', 'Bone_marrow_4'],
    ['Bone_marrow_IL3Rahi_precursors_1', 'Bone_marrow_IL3Rahi_precursors_2', 'Bone_marrow_IL3Rahi_precursors_3'],
    ['Bone_marrow_IL3Ralo_precursors_1', 'Bone_marrow_IL3Ralo_precursors_2', 'Bone_marrow_IL3Ralo_precursors_3'],
    ['Bone_marrow_MSC_W8B2p_1', 'Bone_marrow_MSC_W8B2p_2'],
    ['Brain_1', 'Brain_2', 'Brain_4'],
    ['Breast_2', 'Breast_3'],
    ['Bronchial_epithelial_cells_1', 'Bronchial_epithelial_cells_2'],
    ['Cardiac_resident_MSC_cKitp_1', 'Cardiac_resident_MSC_cKitp_2', 'Cardiac_resident_MSC_cKitp_3'],
    ['Cardiac_resident_MSC_W8B2p_1', 'Cardiac_resident_MSC_W8B2p_2', 'Cardiac_resident_MSC_W8B2p_3'],
    ['CD34p_bone_marrow_cells_1', 'CD34p_bone_marrow_cells_2', 'CD34p_bone_marrow_cells_3', 'CD34p_bone_marrow_cells_4', 'CD34p_bone_marrow_cells_5'],
    ['CD4p_T_cells_1', 'CD4p_T_cells_2', 'CD4p_T_cells_3', 'CD4p_T_cells_4', 'CD4p_T_cells_5', 'CD4p_T_cells_6', 'CD4p_T_cells_7', 'CD4p_T_cells_8'],
    ['CD4T_memory_1', 'CD4T_memory_2', 'CD4T_memory_3'],
    ['CD4T_naive_1', 'CD4T_naive_2', 'CD4T_naive_3', 'CD4T_naive_4', 'CD4T_naive_5', 'CD4T_naive_6', 'CD4T_naive_7'],
    ['CD4T_Teffector_1', 'CD4T_Teffector_2', 'CD4T_Teffector_3'],
    ['CD4T_Tfh_1', 'CD4T_Tfh_2', 'CD4T_Tfh_3'],
    ['CD4T_Th1_1', 'CD4T_Th1_2'],
    ['CD4T_Th1_effector_1', 'CD4T_Th1_effector_2'],
    ['CD4T_Th17_1', 'CD4T_Th17_2'],
    ['CD4T_Th17_effector_1', 'CD4T_Th17_effector_2'],
    ['CD4T_Th2_1', 'CD4T_Th2_2'],
    ['CD4T_Th2_effector_1', 'CD4T_Th2_effector_2'],
    ['Chondrocytes_1', 'Chondrocytes_2'],
    ['chondrogenic_ectomesenchyme_1', 'chondrogenic_ectomesenchyme_2', 'chondrogenic_ectomesenchyme_3'],
    ['Colon_1', 'Colon_2', 'Colon_3'],
    ['Corneal_endothelial_cells_adult_1', 'Corneal_endothelial_cells_adult_2', 'Corneal_endothelial_cells_adult_3'],#, 'Corneal_endothelial_cells_1', 'Corneal_endothelial_cells_2'],
    ['Corneal_endothelial_cells_fetal_1', 'Corneal_endothelial_cells_fetal_2'],
    ['Cortex_2', 'Cortex_3', 'Cortex_4', 'Cortex_5'],
    ['Cumulus_granulosa_1', 'Cumulus_granulosa_2', 'Cumulus_granulosa_3'],
    ['Cumulus_granulosa_germinal_vesicle_1', 'Cumulus_granulosa_germinal_vesicle_2'],
    ['Cumulus_granulosa_M2_1', 'Cumulus_granulosa_M2_2', 'Cumulus_granulosa_M2_3'],
    ['definitive_endoderm_invitro_1', 'definitive_endoderm_invitro_2', 'definitive_endoderm_invitro_3', 'definitive_endoderm_invitro_4', 'definitive_endoderm_invitro_5', 'definitive_endoderm_invitro_6'],
    ['Dermal_fibroblasts_1', 'Dermal_fibroblasts_2', 'Dermal_fibroblasts_3', 'Dermal_fibroblasts_4'], # Dermal 3 and 4 appear quite different from 1 and 2.
    ['Dermal_lymphatic_endothelium_1', 'Dermal_lymphatic_endothelium_2'],
    ['Dorsolateral_prefrontal_cortex_1', 'Dorsolateral_prefrontal_cortex_2', 'Dorsolateral_prefrontal_cortex_3', 'Dorsolateral_prefrontal_cortex_4', 'Dorsolateral_prefrontal_cortex_5'],
    ['Early_basophilic_erythroblast_1', 'Early_basophilic_erythroblast_2', 'Early_basophilic_erythroblast_3', 'Early_basophilic_erythroblast_4', 'Early_basophilic_erythroblast_5', 'Early_basophilic_erythroblast_6'],
    ['ectoderm_invitro_1' ,'ectoderm_invitro_2', 'ectoderm_invitro_3', 'ectoderm_invitro_4', 'ectoderm_invitro_5', 'ectoderm_invitro_6', 'ectoderm_invitro_7', 'ectoderm_invitro_8', 'ectoderm_invitro_9', 'ectoderm_invitro_10', 'ectoderm_invitro_11', 'ectoderm_invitro_12', 'ectoderm_invitro_13', 'ectoderm_invitro_14'],
    ['Embryo_2C_1', 'Embryo_2C_2', 'Embryo_2C_3'],
    ['Embryo_4C_1', 'Embryo_4C_2', 'Embryo_4C_3', 'Embryo_4C_4'],
    ['Embryo_8C_1', 'Embryo_8C_2', 'Embryo_8C_3', 'Embryo_8C_4', 'Embryo_8C_5', 'Embryo_8C_6', 'Embryo_8C_7', 'Embryo_8C_8', 'Embryo_8C_9', 'Embryo_8C_11'],
    ['Embryo4C_E1_C1', 'Embryo4C_E1_C2', 'Embryo4C_E1_C3', 'Embryo4C_E1_C4', 'Embryo4C_E2_C1', 'Embryo4C_E2_C2', 'Embryo4C_E2_C3', 'Embryo4C_E2_C4', 'Embryo4C_E3_C1', 'Embryo4C_E3_C2', 'Embryo4C_E3_C3', 'Embryo4C_E3_C4'],
    ['Embryo8C_E1_C1', 'Embryo8C_E1_C2', 'Embryo8C_E1_C3', 'Embryo8C_E1_C4', 'Embryo8C_E2_C1', 'Embryo8C_E2_C2', 'Embryo8C_E2_C3', 'Embryo8C_E2_C4', 'Embryo8C_E2_C5', 'Embryo8C_E2_C6', 'Embryo8C_E2_C7', 'Embryo8C_E2_C8', 'Embryo8C_E3_C1', 'Embryo8C_E3_C2', 'Embryo8C_E3_C3', 'Embryo8C_E3_C4', 'Embryo8C_E3_C5', 'Embryo8C_E3_C6', 'Embryo8C_E3_C7', 'Embryo8C_E3_C8'],
    ['Endometrial_stromal_cells_1', 'Endometrial_stromal_cells_2', 'Endometrial_stroma_1', 'Endometrial_stroma_2'],
    ['Eosophageal_tissue_1', 'Eosophageal_tissue_2', 'Eosophageal_tissue_3', 'Eosophageal_tissue_4', 'Eosophageal_tissue_5', 'Eosophageal_tissue_6'],
    ['Epidermal_keratinocytes_1', 'Epidermal_keratinocytes_2', 'Epidermal_keratinocytes_3', 'Epidermal_keratinocytes_4', 'Epidermal_keratinocytes_5'],# sample 6 has a problem, I take the majority vote 'Epidermal_keratinocytes_6'],
    ['Epidermal_melanocytes_1', 'Epidermal_melanocytes_2'],
    ['Epidermal_melanocytes_juvenile_1', 'Epidermal_melanocytes_juvenile_2'],
    ['Erythroid_progenitor_1', 'Erythroid_progenitor_2', 'Erythroid_progenitor_3'],
    ['Fetal_retinal_pigment_epithelium_1', 'Fetal_retinal_pigment_epithelium_2', 'Fetal_retinal_pigment_epithelium_3'],
    ['Gastric_tissue_1', 'Gastric_tissue_2'],
    ['germinal_B_cells_1', 'germinal_B_cells_2', 'germinal_B_cells_3', 'germinal_B_cells_4'],
    ['Granulocytes_1', 'Granulocytes_2'],
    ['Heart_1', 'Heart_2', 'Heart_3'], # Delete from above in MAIN
    ['Hepatocyts_1', 'Hepatocyte_2'],
    ['hESC_cortical_neuron_d12_cortical_specification_1', 'hESC_cortical_neuron_d12_cortical_specification_2'],
    ['hESC_cortical_neuron_d19_cortical_specification_1', 'hESC_cortical_neuron_d19_cortical_specification_2', 'hESC_cortical_neuron_d19_cortical_specification_3', 'hESC_cortical_neuron_d19_cortical_specification_4'],
    ['hESC_cortical_neuron_d26_deep_layer_1', 'hESC_cortical_neuron_d26_deep_layer_2'],
    ['hESC_cortical_neuron_d33_deep_layer_1', 'hESC_cortical_neuron_d33_deep_layer_2'],
    ['hESC_cortical_neuron_d49_deep_layer_1', 'hESC_cortical_neuron_d49_deep_layer_2'],
    ['hESC_cortical_neuron_d63_upper_layer_1', 'hESC_cortical_neuron_d63_upper_layer_2'],
    ['hESC_cortical_neuron_d7_1', 'hESC_cortical_neuron_d7_2', 'hESC_cortical_neuron_d7_3', 'hESC_cortical_neuron_d7_4'],
    ['hESC_cortical_neuron_d77_upper_layer_1', 'hESC_cortical_neuron_d77_upper_layer_2'],
    ['hESC_H1_1', 'hESC_H1_2', 'hESC_H1_3', 'hESC_H1_4', 'hESC_H1_5', 'hESC_H1_6', 'hESC_H1_7', 'hESC_H1_8', 'hESC_H1_9', 'hESC_H1_10', 'hESC_H1_11', 'hESC_H1_12', 'hESC_H1_13', 'hESC_H1_14', 'hESC_H1_16', 'hESC_H1_17', 'hESC_h1_18', 'hESC_h1_19','hESC_cortical_neuron_d0_hESC_1', 'hESC_cortical_neuron_d0_hESC_3', 'hESC_cortical_neuron_d0_hESC_4','hESC_liver_diff_d0_hESC_1'],
    ['hESCs_3iL_1', 'hESCs_3iL_2', 'hESCs_3iL_3'],
    ['hESCs_H1_18', 'hESCs_H1_19', 'hESCs_H1_20'], # Singapore: H1 WA-01
    ['Human_skeletal_muscle_myoblasts_1', 'Human_skeletal_muscle_myoblasts_2', 'Human_skeletal_muscle_myoblasts_3'],
    ['Ileum_1', 'Ileum_2', 'Ileum_4', 'Ileum_5', 'Ileum_6', 'Ileum_7', 'Ileum_8', 'Ileum_10', 'Ileum_11', 'Ileum_12', 'Ileum_14', 'Ileum_15', 'Ileum_16', 'Ileum_17', 'Ileum_18', 'Ileum_19', 'Ileum_20', 'Ileum_21', 'Ileum_22', 'Ileum_23', 'Ileum_24', 'Ileum_25', 'Ileum_26', 'Ileum_27', 'Ileum_28', 'Ileum_29', 'Ileum_30', 'Ileum_31', 'Ileum_32', 'Ileum_33', 'Ileum_34', 'Ileum_35', 'Ileum_36', 'Ileum_37', 'Ileum_38', 'Ileum_39', 'Ileum_40', 'Ileum_41', 'Ileum_42', 'Ileum_43'],
    ['iMSC_1', 'iMSC_2'],
    ['induced_cortical_neuron_1', 'induced_cortical_neuron_2', 'induced_cortical_neuron_3'],
    ['invitro_DA_neurons_1', 'invitro_DA_neurons_2', 'invitro_DA_neurons_3', 'invitro_DA_neurons_4'],
    ['iPSC_reprogramming_CD34pCB_iPSC_1', 'iPSC_reprogramming_CD34pCB_iPSC_2', 'iPSC_reprogramming_CD34pCB_iPSC_3'],
    ['iPSC_reprogramming_hIFT_D10_1', 'iPSC_reprogramming_hIFT_D10_2', 'iPSC_reprogramming_hIFT_D10_3'],
    ['iPSC_reprogramming_hIFT_D10_SSEA3n_1', 'iPSC_reprogramming_hIFT_D10_SSEA3n_2', 'iPSC_reprogramming_hIFT_D10_SSEA3n_3'],
    ['iPSC_reprogramming_hIFT_D10_SSEA3p_1', 'iPSC_reprogramming_hIFT_D10_SSEA3p_2', 'iPSC_reprogramming_hIFT_D10_SSEA3p_3', 'iPSC_reprogramming_hIFT_D10_SSEA3p_4', 'iPSC_reprogramming_hIFT_D10_SSEA3p_5'],
    ['iPSC_reprogramming_hIFT_D14_1', 'iPSC_reprogramming_hIFT_D14_2', 'iPSC_reprogramming_hIFT_D14_3'],
    ['iPSC_reprogramming_hIFT_D14_SSEA3n_1', 'iPSC_reprogramming_hIFT_D14_SSEA3n_2', 'iPSC_reprogramming_hIFT_D14_SSEA3n_3'],
    ['iPSC_reprogramming_hIFT_D14_SSEA3p_1', 'iPSC_reprogramming_hIFT_D14_SSEA3p_2', 'iPSC_reprogramming_hIFT_D14_SSEA3p_3', 'iPSC_reprogramming_hIFT_D14_SSEA3p_4', 'iPSC_reprogramming_hIFT_D14_SSEA3p_5'],
    ['iPSC_reprogramming_hIFT_D2_1', 'iPSC_reprogramming_hIFT_D2_2', 'iPSC_reprogramming_hIFT_D2_3', 'iPSC_reprogramming_hIFT_D2_4', 'iPSC_reprogramming_hIFT_D2_5'],
    ['iPSC_reprogramming_hIFT_D20_TRA160n_1', 'iPSC_reprogramming_hIFT_D20_TRA160n_2', 'iPSC_reprogramming_hIFT_D20_TRA160n_3', 'iPSC_reprogramming_hIFT_D20_TRA160n_4'],
    ['iPSC_reprogramming_hIFT_D20_TRA160p_1', 'iPSC_reprogramming_hIFT_D20_TRA160p_2', 'iPSC_reprogramming_hIFT_D20_TRA160p_3', 'iPSC_reprogramming_hIFT_D20_TRA160p_4', 'iPSC_reprogramming_hIFT_D20_TRA160p_5'],
    ['iPSC_reprogramming_hIFT_D24_TRA160n_1', 'iPSC_reprogramming_hIFT_D24_TRA160n_2', 'iPSC_reprogramming_hIFT_D24_TRA160n_3', 'iPSC_reprogramming_hIFT_D24_TRA160n_4', 'iPSC_reprogramming_hIFT_D24_TRA160n_5', 'iPSC_reprogramming_hIFT_D24_TRA160n_6'],
    ['iPSC_reprogramming_hIFT_D24_TRA160p_1', 'iPSC_reprogramming_hIFT_D24_TRA160p_2', 'iPSC_reprogramming_hIFT_D24_TRA160p_3', 'iPSC_reprogramming_hIFT_D24_TRA160p_4'],
    ['iPSC_reprogramming_hIFT_D5_1', 'iPSC_reprogramming_hIFT_D5_2', 'iPSC_reprogramming_hIFT_D5_3', 'iPSC_reprogramming_hIFT_D5_4', 'iPSC_reprogramming_hIFT_D5_5', 'iPSC_reprogramming_hIFT_D5_6', 'iPSC_reprogramming_hIFT_D5_7', 'iPSC_reprogramming_hIFT_D5_8', 'iPSC_reprogramming_hIFT_D5_9'],
    ['iPSC_reprogramming_hIFT_D8_1', 'iPSC_reprogramming_hIFT_D8_2', 'iPSC_reprogramming_hIFT_D8_3', 'iPSC_reprogramming_hIFT_D8_4'],
    ['Keratinocytes_1', 'Keratinocytes_2', 'Keratinocytes_3'],
    ['Kidney_1', 'Kidney_3'],
    ['Late_basophilic_erythroblast_1', 'Late_basophilic_erythroblast_2', 'Late_basophilic_erythroblast_3', 'Late_basophilic_erythroblast_4', 'Late_basophilic_erythroblast_5', 'Late_basophilic_erythroblast_6'],
    ['Late_basophilic_erythroblast_1', 'Late_basophilic_erythroblast_2', 'Late_basophilic_erythroblast_3'],
    ['Late_blastocyst_E1_C1_pTE', 'Late_blastocyst_E1_C10_pTE', 'Late_blastocyst_E1_C11_pTE', 'Late_blastocyst_E1_C2_pTE', 'Late_blastocyst_E1_C3_pTE', 'Late_blastocyst_E1_C5_pTE', 'Late_blastocyst_E1_C8_pTE', 'Late_blastocyst_E2_C10_pTE', 'Late_blastocyst_E2_C9_pTE', ],
    ['Late_blastocyst_E1_C4_mTE', 'Late_blastocyst_E1_C12_mTE', 'Late_blastocyst_E1_C6_mTE', 'Late_blastocyst_E1_C7_mTE', 'Late_blastocyst_E1_C9_mTE', 'Late_blastocyst_E2_C4_mTE', 'Late_blastocyst_E2_C5_mTE', 'Late_blastocyst_E2_C6_mTE', 'Late_blastocyst_E2_C7_mTE', ],
    ['Late_blastocyst_E2_C1_EPI', 'Late_blastocyst_E2_C2_EPI', 'Late_blastocyst_E2_C3_EPI', 'Late_blastocyst_E2_C8_EPI', 'Late_blastocyst_E3_C1_EPI'],
    ['Late_blastocyst_E3_C2_PE', 'Late_blastocyst_E3_C3_PE', 'Late_blastocyst_E3_C4_PE', 'Late_blastocyst_E3_C5_PE', 'Late_blastocyst_E3_C6_PE', 'Late_blastocyst_E3_C7_PE', 'Late_blastocyst_E3_C8_PE'],
    ['Liver_1', 'Liver_2', 'Liver_3'],
    ['Lung_2', 'Lung_3'],
    ['Lung_fibroblast_1', 'Lung_fibroblast_2'],
    ['Lung_normal_1', 'Lung_normal_2', 'Lung_normal_3', 'Lung_normal_4', 'Lung_normal_5', 'Lung_normal_6', 'Lung_normal_7'],
    ['Lymph_node_1', 'Lymph_node_2'],
    ['Macrophage_M1_1', 'Macrophage_M1_2', 'Macrophage_M1_3'],
    ['Macrophage_M2_1', 'Macrophage_M2_2', 'Macrophage_M2_3'],
    ['Mammary_epithelial_cells_1', 'Mammary_epithelial_cells_2'],
    ['mesoderm_invitro_1', 'mesoderm_invitro_2', 'mesoderm_invitro_3', 'mesoderm_invitro_4', 'mesoderm_invitro_5', 'mesoderm_invitro_6'],
    ['Microvascular_endothelial_cells_1', 'Microvascular_endothelial_cells_2'],
    ['Monocytes_1', 'Monocytes_2', 'Monocytes_3', 'Monocytes_4', 'Monocytes_5', 'Monocytes_6', 'Monocytes_7', 'Monocytes_8'],
    ['Monocytes_CD14p_1', 'Monocytes_CD14p_2', 'Monocytes_CD14p_3', 'Monocytes_CD14p_4', 'Monocytes_CD14p_5', 'Monocytes_CD14p_6'],
    ['Mononuclear_cells_peripheral_blood_1', 'Mononuclear_cells_peripheral_blood_2'],
    ['Morula_1', 'Morula_2', 'Morula_3'],
    ['Morula_E1_C1', 'Morula_E1_C2', 'Morula_E1_C3', 'Morula_E1_C4', 'Morula_E1_C5', 'Morula_E1_C6', 'Morula_E1_C7', 'Morula_E1_C8', 'Morula_E2_C1', 'Morula_E2_C2', 'Morula_E2_C3', 'Morula_E2_C4', 'Morula_E2_C5', 'Morula_E2_C6', 'Morula_E2_C7', 'Morula_E2_C8'],
    ['Motor_neuron_sod_av4p_1', 'Motor_neuron_sod_av4p_2'],
    ['Motor_neuron_sod_pp_1', 'Motor_neuron_sod_pp_2', 'Motor_neuron_sod_pp_3'],
    ['MSC_adipose_1', 'MSC_adipose_2'],
    ['MSC_bone_marrow_1', 'MSC_bone_marrow_2'],
    ['MSC_umbilical_cord_1', 'MSC_umbilical_cord_2'],
    ['Mural_granulosa_1', 'Mural_granulosa_2', 'Mural_granulosa_3'],
    ['Myometrium_labour_1', 'Myometrium_labour_2', 'Myometrium_labour_3', 'Myometrium_labour_4', 'Myometrium_labour_5'],
    ['Myometrium_no_labour_1', 'Myometrium_no_labour_2', 'Myometrium_no_labour_3', 'Myometrium_no_labour_4', 'Myometrium_no_labour_5'],
    ['naive_B_cells_1', 'naive_B_cells_2', 'naive_B_cells_3', 'naive_B_cells_4', 'naive_B_cells_5'],
    ['neocortex_cortical_plate_1', 'neocortex_cortical_plate_2', 'neocortex_cortical_plate_3', 'neocortex_cortical_plate_4', 'neocortex_cortical_plate_5', 'neocortex_cortical_plate_6'],
    ['neocortex_inner_subventricular_zone_1', 'neocortex_inner_subventricular_zone_2', 'neocortex_inner_subventricular_zone_3', 'neocortex_inner_subventricular_zone_4', 'neocortex_inner_subventricular_zone_5', 'neocortex_inner_subventricular_zone_6'],
    ['neocortex_outer_subventricular_zone_1', 'neocortex_outer_subventricular_zone_2', 'neocortex_outer_subventricular_zone_3', 'neocortex_outer_subventricular_zone_4', 'neocortex_outer_subventricular_zone_5', 'neocortex_outer_subventricular_zone_6'],
    ['neocortex_ventricular_zone_1', 'neocortex_ventricular_zone_2', 'neocortex_ventricular_zone_3', 'neocortex_ventricular_zone_4', 'neocortex_ventricular_zone_5', 'neocortex_ventricular_zone_6'],
    ['Neutrophil_1', 'Neutrophil_2'],
    ['NPC_1', 'NPC_2', 'NPC_3'],
    ['Oocyte_1', 'Oocyte_2', 'Oocyte_3', 'Oocyte_4', 'Oocyte_5'],
    #['Oocyte E1 C1', 'Oocyte E2 C1', 'Oocyte E3 C1'],
    ['Orthochromatic_erythroblast_1', 'Orthochromatic_erythroblast_2', 'Orthochromatic_erythroblast_3', 'Orthochromatic_erythroblast_4', 'Orthochromatic_erythroblast_5', 'Orthochromatic_erythroblast_6'],
    ['Osteoblasts_1', 'Osteoblasts_2', 'Osteoblasts_3', 'Osteoblasts_4', 'Osteoblasts_5', 'Osteoblasts_6', 'Osteoblasts_7', 'Osteoblasts_8', 'Osteoblasts_9', 'Osteoblasts_10'],
    ['Ovary_1', 'Ovary_2'],
    ['Pancreatic_bud_1', 'Pancreatic_bud_2'],
    ['Pancreatic_bud_invitro_1', 'Pancreatic_bud_invitro_2'],
    ['Pancreatic_islets_1',], #'Pancreatic_islets_2', 'Pancreatic_islets_3', 'Pancreatic_islets_4', 'Pancreatic_islets_5', 'Pancreatic_islets_6', 'Pancreatic_islets_7', 'Pancreatic_islets_8', 'Pancreatic_islets_9', 'Pancreatic_islets_10'],
    ['Placental_epithelial_1', 'Placental_epithelial_2'],
    ['Placental_pericytes_1', 'Placental_pericytes_2'],
    ['Platelets_1', 'Platelets_2', 'Platelets_3', 'Platelets_4'],
    ['Polychromatic_erythroblast_1', 'Polychromatic_erythroblast_2', 'Polychromatic_erythroblast_3', 'Polychromatic_erythroblast_4', 'Polychromatic_erythroblast_5', 'Polychromatic_erythroblast_6'],
    ['Proerythroblast_1', 'Proerythroblast_2', 'Proerythroblast_3', 'Proerythroblast_4', 'Proerythroblast_5', 'Proerythroblast_6'],
    #['Pronuclei_1', 'Pronuclei_2', 'Pronuclei_3'],
    #['Prostate_1', 'Prostate_2', 'Prostate_3', 'Prostate_4', 'Prostate_5', 'Prostate_6', 'Prostate_7', 'Prostate_8', 'Prostate_9', 'Prostate_11', 'Prostate_12'],
    ['Radial_glial_early_1', 'Radial_glial_early_2'],
    ['Radial_glial_late_1', 'Radial_glial_late_2', 'Radial_glial_late_3'],
    ['Radial_glial_mid_1', 'Radial_glial_mid_2'],
    #['Retina_1', 'Retina_2', 'Retina_3'], # Same study, same lab, but # 3 is an outlier from the other two...
    ['Saphenous_vein_endothelial_cells_1', 'Saphenous_vein_endothelial_cells_2'],
    #['Skeletal_muscle_1', 'Skeletal_muscle_2', 'Skeletal_muscle_cells_3', 'Skeletal_muscle_cells_4', 'Skeletal_muscle_cells_5', 'Skeletal_muscle_cells_6', 'Skeletal_muscle_cells_7', 'Skeletal_muscle_cells_8', 'Skeletal_muscle_cells_9', 'Skeletal_muscle_cells_10', 'Skeletal_muscle_cells_11', 'Skeletal_muscle_cells_12', 'Skeletal_muscle_cells_13', 'Skeletal_muscle_cells_14', 'Skeletal_muscle_cells_15', 'Skeletal_muscle_cells_16', 'Skeletal_muscle_cells_17', 'Skeletal_muscle_cells_18', 'Skeletal_muscle_cells_19', 'Skeletal_muscle_cells_20', 'Skeletal_muscle_cells_21', 'Skeletal_muscle_cells_22', 'Skeletal_muscle_cells_23', 'Skeletal_muscle_cells_24', 'Skeletal_muscle_cells_25', 'Skeletal_muscle_cells_26', 'Skeletal_muscle_cells_27'],
    ['Skeletal_muscle_myotube_1', 'Skeletal_muscle_myotube_2'],
    #['Sperm_1', 'Sperm_2'],#, 'Sperm_3', 'Sperm_4', 'Sperm_5'],
    ['Testes_1', 'Testes_2'],
    ['Thyroid_1', 'Thyroid_2'],
    ['trophoblast_invitro_1', 'trophoblast_invitro_2'],
    ['Umbilical_vein_endothelial_cells_1', 'Umbilical_vein_endothelial_cells_2'],
    ['Villious_mesenchymal_fibroblasts_1', 'Villious_mesenchymal_fibroblasts_2'],
    ['White_preadipocytes_1', 'White_preadipocytes_2'],
    #['Zygote_1', 'Zygote_2',
    ['Zygote_E1_C1', 'Zygote_E2_C1', 'Zygote_E3_C1'],
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
mapped.saveTSV("genes_ntc_expression.tsv", key_order=['ensg', 'name', 'transcript_type'])

# Clean out hanger on data
# ['loc', 'name', 'ensg', 'tss_loc', 'conditions', 'strand']
f = {"force_tsv": True, 'ensg': 0, 'name': 1, 'transcript_type': 2}
mapped = expression(filename='genes_ntc_expression.tsv', format=f, expn='column[3:]')
mapped.save("genes_ntc_expression.glb") # These are the final tables.

mapped = ensg.map(key="ensg", genelist=raw_expn)
mapped.save("genes_ntc_expression_nonmerged.glb")
mapped.saveTSV("genes_ntc_expression_nonmerged.tsv")

arr.tree(filename="tree.png", color_threshold=0.0, label_size=5, size=(5,14))
print()
print("Num conditions =", len(arr.getConditionNames()))
print()
