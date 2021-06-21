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

arr = raw_expn.mean_replicates(
    ['Achilles_tendon_rp1','Achilles_tendon_rp2','Achilles_tendon_rp3','Achilles_tendon_rp4'],
    ['Adipose_rp1', 'Adipose_rp2'],
    ['adult_pancreas_exocrine_rp1', 'adult_pancreas_exocrine_rp2','adult_pancreas_exocrine_rp3','adult_pancreas_exocrine_rp4', 'adult_pancreas_exocrine_rp5','adult_pancreas_exocrine_rp6'],
    ['Adrenal_gland_rp1', 'Adrenal_gland_rp2'],
    ['Airway_basal_cells_rp1', 'Airway_basal_cells_rp2', 'Airway_basal_cells_rp3', 'Airway_basal_cells_rp4', 'Airway_basal_cells_rp5', 'Airway_basal_cells_rp6', 'Airway_basal_cells_rp7', 'Airway_basal_cells_rp8', 'Airway_basal_cells_rp9', 'Airway_basal_cells_rp10', 'Airway_basal_cells_rp11', 'Airway_basal_cells_rp12', 'Airway_basal_cells_rp13', 'Airway_basal_cells_rp14', 'Airway_basal_cells_rp15', 'Airway_basal_cells_rp16', 'Airway_basal_cells_rp17', 'Airway_basal_cells_rp18', 'Airway_basal_cells_rp19', 'Airway_basal_cells_rp20', 'Airway_basal_cells_rp21', 'Airway_basal_cells_rp22', 'Airway_basal_cells_rp23', 'Airway_basal_cells_rp24', 'Airway_basal_cells_rp28', 'Airway_basal_cells_rp29', 'Airway_basal_cells_rp30'],
    ['Airway_smooth_muscle_rp1', 'Airway_smooth_muscle_rp2', 'Airway_smooth_muscle_rp3', 'Airway_smooth_muscle_rp4'],
    ['Aortic_adventitial_fibroblasts_rp1', 'Aortic_adventitial_fibroblasts_rp2'],
    ['Aortic_endothelial_cells_rp1', 'Aortic_endothelial_cells_rp2'],
    ['Astrocytes_rp1', 'Astrocytes_rp2'],
    ['aortic_valve_tricuspid_valve_rp1', 'aortic_valve_tricuspid_valve_rp2', 'aortic_valve_tricuspid_valve_rp3', 'aortic_valve_tricuspid_valve_rp4', 'aortic_valve_tricuspid_valve_rp5', 'aortic_valve_tricuspid_valve_rp6', 'aortic_valve_tricuspid_valve_rp7', 'aortic_valve_tricuspid_valve_rp8', 'aortic_valve_tricuspid_valve_rp9', 'aortic_valve_tricuspid_valve_rp10'],
    ['astrocyte_adult_rp1', 'astrocyte_adult_rp10', 'astrocyte_adult_rp11', 'astrocyte_adult_rp12', 'astrocyte_adult_rp2', 'astrocyte_adult_rp3', 'astrocyte_adult_rp4', 'astrocyte_adult_rp5', 'astrocyte_adult_rp6', 'astrocyte_adult_rp7', 'astrocyte_adult_rp8', 'astrocyte_adult_rp9', 'astrocyte_fetal_rp4', 'astrocyte_fetal_rp5'],
    ['astrocyte_hippocampus_adult_rp1', 'astrocyte_hippocampus_adult_rp2', 'astrocyte_hippocampus_adult_rp3', 'astrocyte_hippocampus_adult_rp4'],
    ['B_cells_CD20p_rp1', 'B_cells_CD20p_rp2', 'B_cells_CD20p_rp3', 'B_cells_CD20p_rp4', 'B_cells_CD20p_rp5', 'B_cells_CD20p_rp6'],
    ['Bone_marrow_rp1', 'Bone_marrow_rp2', 'Bone_marrow_rp3', 'Bone_marrow_rp4'],
    ['Bone_marrow_IL3Rahi_precursors_rp1', 'Bone_marrow_IL3Rahi_precursors_rp2', 'Bone_marrow_IL3Rahi_precursors_rp3'],
    ['Bone_marrow_IL3Ralo_precursors_rp1', 'Bone_marrow_IL3Ralo_precursors_rp2', 'Bone_marrow_IL3Ralo_precursors_rp3'],
    ['Bone_marrow_MSC_W8B2p_rp1', 'Bone_marrow_MSC_W8B2p_rp2'],
    ['Brain_rp1', 'Brain_rp2', 'Brain_rp4'],
    ['Breast_rp2', 'Breast_rp3'],
    ['Bronchial_epithelial_cells_rp1', 'Bronchial_epithelial_cells_rp2'],
    ['Cardiac_resident_MSC_cKitp_rp1', 'Cardiac_resident_MSC_cKitp_rp2', 'Cardiac_resident_MSC_cKitp_rp3'],
    ['Cardiac_resident_MSC_W8B2p_rp1', 'Cardiac_resident_MSC_W8B2p_rp2', 'Cardiac_resident_MSC_W8B2p_rp3'],
    ['CD34p_bone_marrow_cells_rp1', 'CD34p_bone_marrow_cells_rp2', 'CD34p_bone_marrow_cells_rp3', 'CD34p_bone_marrow_cells_rp4', 'CD34p_bone_marrow_cells_rp5'],
    ['CD4p_T_cells_rp1', 'CD4p_T_cells_rp2', 'CD4p_T_cells_rp3', 'CD4p_T_cells_rp4', 'CD4p_T_cells_rp5', 'CD4p_T_cells_rp6', 'CD4p_T_cells_rp7', 'CD4p_T_cells_rp8'],
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
    ['Chondrocytes_rp1', 'Chondrocytes_rp2'],
    ['chondrogenic_ectomesenchyme_rp1', 'chondrogenic_ectomesenchyme_rp2', 'chondrogenic_ectomesenchyme_rp3'],
    ['Colon_rp1', 'Colon_rp2', 'Colon_rp3', 'Colon_rp4', 'Colon_rp5'],
    ['colon_sigmoid_rp1', 'colon_sigmoid_rp2', 'colon_sigmoid_rp3', 'colon_sigmoid_rp4'],
    ['colon_transverse_rp1', 'colon_transverse_rp2', 'colon_transverse_rp3', 'colon_transverse_rp4'],
    ['colon_left_rp1', 'colonic_left_rp2'],
    ['Corneal_endothelial_cells_adult_rp1', 'Corneal_endothelial_cells_adult_rp2', 'Corneal_endothelial_cells_adult_rp3'],#, 'Corneal_endothelial_cells_rp1', 'Corneal_endothelial_cells_rp2'],
    ['Corneal_endothelial_cells_fetal_rp1', 'Corneal_endothelial_cells_fetal_rp2'],
    ['Cortex_rp2', 'Cortex_rp3', 'Cortex_rp4', 'Cortex_rp5'],
    ['cortical_neuron_wta_ctrl_0h', 'cortical_neuron_wtb_ctrl_0h', 'cortical_neuron_wtc_ctrl_0h'],
    ['Cumulus_granulosa_rp1', 'Cumulus_granulosa_rp2', 'Cumulus_granulosa_rp3'],
    ['Cumulus_granulosa_germinal_vesicle_rp1', 'Cumulus_granulosa_germinal_vesicle_rp2'],
    ['Cumulus_granulosa_M2_rp1', 'Cumulus_granulosa_M2_rp2', 'Cumulus_granulosa_M2_rp3'],
    ['definitive_endoderm_invitro_rp1', 'definitive_endoderm_invitro_rp2', 'definitive_endoderm_invitro_rp3', 'definitive_endoderm_invitro_rp4', 'definitive_endoderm_invitro_rp5', 'definitive_endoderm_invitro_rp6'],
    ['Dermal_fibroblasts_rp1', 'Dermal_fibroblasts_rp2', 'Dermal_fibroblasts_rp3', 'Dermal_fibroblasts_rp4'], # Dermal 3 and 4 appear quite different from 1 and 2.
    ['Dermal_lymphatic_endothelium_rp1', 'Dermal_lymphatic_endothelium_rp2'],
    ['Dorsolateral_prefrontal_cortex_rp1', 'Dorsolateral_prefrontal_cortex_rp2', 'Dorsolateral_prefrontal_cortex_rp3', 'Dorsolateral_prefrontal_cortex_rp4', 'Dorsolateral_prefrontal_cortex_rp5'],
    ['Early_basophilic_erythroblast_rp1', 'Early_basophilic_erythroblast_rp2', 'Early_basophilic_erythroblast_rp3', 'Early_basophilic_erythroblast_rp4', 'Early_basophilic_erythroblast_rp5', 'Early_basophilic_erythroblast_rp6'],
    ['ectoderm_invitro_1' ,'ectoderm_invitro_rp2', 'ectoderm_invitro_rp3', 'ectoderm_invitro_rp4', 'ectoderm_invitro_rp5', 'ectoderm_invitro_rp6', 'ectoderm_invitro_rp7', 'ectoderm_invitro_rp8', 'ectoderm_invitro_rp9', 'ectoderm_invitro_rp10', 'ectoderm_invitro_rp11', 'ectoderm_invitro_rp12', 'ectoderm_invitro_rp13', 'ectoderm_invitro_rp14'],
    ['Embryo_2C_rp1', 'Embryo_2C_rp2', 'Embryo_2C_rp3'],
    ['Embryo_4C_rp1', 'Embryo_4C_rp2', 'Embryo_4C_rp3', 'Embryo_4C_rp4'],
    ['Embryo_8C_rp1', 'Embryo_8C_rp2', 'Embryo_8C_rp3', 'Embryo_8C_rp4', 'Embryo_8C_rp5', 'Embryo_8C_rp6', 'Embryo_8C_rp7', 'Embryo_8C_rp8', 'Embryo_8C_rp9', 'Embryo_8C_rp11'],
    ['Embryo4C_E1_C1', 'Embryo4C_E1_C2', 'Embryo4C_E1_C3', 'Embryo4C_E1_C4', 'Embryo4C_E2_C1', 'Embryo4C_E2_C2', 'Embryo4C_E2_C3', 'Embryo4C_E2_C4', 'Embryo4C_E3_C1', 'Embryo4C_E3_C2', 'Embryo4C_E3_C3', 'Embryo4C_E3_C4'],
    ['Embryo8C_E1_C1', 'Embryo8C_E1_C2', 'Embryo8C_E1_C3', 'Embryo8C_E1_C4', 'Embryo8C_E2_C1', 'Embryo8C_E2_C2', 'Embryo8C_E2_C3', 'Embryo8C_E2_C4', 'Embryo8C_E2_C5', 'Embryo8C_E2_C6', 'Embryo8C_E2_C7', 'Embryo8C_E2_C8', 'Embryo8C_E3_C1', 'Embryo8C_E3_C2', 'Embryo8C_E3_C3', 'Embryo8C_E3_C4', 'Embryo8C_E3_C5', 'Embryo8C_E3_C6', 'Embryo8C_E3_C7', 'Embryo8C_E3_C8'],
    ['Endometrial_stromal_cells_rp1', 'Endometrial_stromal_cells_rp2', 'Endometrial_stroma_rp1', 'Endometrial_stroma_rp2'],
    ['Endometrial_stroma_rp1', 'Endometrial_stroma_rp2'],
    ['endometrial_stromal_fibroblasts_rp1', 'endometrial_stromal_fibroblasts_rp2'],
    ['Eosophageal_tissue_rp1', 'Eosophageal_tissue_rp2', 'Eosophageal_tissue_rp3', 'Eosophageal_tissue_rp4', 'Eosophageal_tissue_rp5', 'Eosophageal_tissue_rp6'],
    ['epithelium_breast_rp1', 'epithelium_breast_rp2', 'epithelium_breast_rp3', 'epithelium_breast_rp4'],
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
    ['hESC_H1_rp1', 'hESC_H1_rp2', 'hESC_H1_rp3', 'hESC_H1_rp4', 'hESC_H1_rp5', 'hESC_H1_rp6', 'hESC_H1_rp7', 'hESC_H1_rp8', 'hESC_H1_rp9', 'hESC_H1_rp10', 'hESC_H1_rp11', 'hESC_H1_rp12', 'hESC_H1_rp13', 'hESC_H1_rp14', 'hESC_H1_rp16', 'hESC_H1_rp17', 'hESC_h1_rp18', 'hESC_h1_rp19','hESC_cortical_neuron_d0_hESC_rp1', 'hESC_cortical_neuron_d0_hESC_rp3', 'hESC_cortical_neuron_d0_hESC_rp4','hESC_liver_diff_d0_hESC_1'],
    ['hESCs_3iL_rp1', 'hESCs_3iL_rp2', 'hESCs_3iL_rp3'],
    ['hESCs_H1_rp18', 'hESCs_H1_rp19', 'hESCs_H1_20'], # Singapore: H1 WA-01
    ['Human_skeletal_muscle_myoblasts_rp1', 'Human_skeletal_muscle_myoblasts_rp2', 'Human_skeletal_muscle_myoblasts_rp3'],
    ['Ileum_rp1', 'Ileum_rp2', 'Ileum_rp4', 'Ileum_rp5', 'Ileum_rp6', 'Ileum_rp7', 'Ileum_rp8', 'Ileum_rp10', 'Ileum_rp11', 'Ileum_rp12', 'Ileum_rp14', 'Ileum_rp15', 'Ileum_rp16', 'Ileum_rp17', 'Ileum_rp18', 'Ileum_rp19', 'Ileum_rp20', 'Ileum_rp21', 'Ileum_rp22', 'Ileum_rp23', 'Ileum_rp24', 'Ileum_rp25', 'Ileum_rp26', 'Ileum_rp27', 'Ileum_rp28', 'Ileum_rp29', 'Ileum_rp30', 'Ileum_rp31', 'Ileum_rp32', 'Ileum_rp33', 'Ileum_rp34', 'Ileum_rp35', 'Ileum_rp36', 'Ileum_rp37', 'Ileum_rp38', 'Ileum_rp39', 'Ileum_rp40', 'Ileum_rp41', 'Ileum_rp42', 'Ileum_rp43'],
    ['iMSC_rp1', 'iMSC_rp2'],
    ['induced_cortical_neuron_rp1', 'induced_cortical_neuron_rp2', 'induced_cortical_neuron_rp3'],
    ['invitro_DA_neurons_rp1', 'invitro_DA_neurons_rp2', 'invitro_DA_neurons_rp3', 'invitro_DA_neurons_rp4'],
    ['invitro_DA_neurons_PD_pat1_rp1',
    'invitro_DA_neurons_PD_pat1_rp2',
    'invitro_DA_neurons_PD_pat2_rp1',
    'invitro_DA_neurons_PD_pat2_rp2',
    'invitro_DA_neurons_PD_pat3_rp1',
    'invitro_DA_neurons_PD_pat3_rp2',
    'invitro_DA_neurons_PD_pat4_rp1',
    'invitro_DA_neurons_PD_pat4_rp2',
    'invitro_DA_neurons_PD_pat5_rp1',
    'invitro_DA_neurons_PD_pat5_rp2',
    'invitro_DA_neurons_sporadicPD_rp1',
    'invitro_DA_neurons_sporadicPD_rp2',
    'invitro_DA_neurons_twin_PD_rp1',
    'invitro_DA_neurons_twin_PD_rp2',
    'invitro_DA_neurons_twin_PD_rp3',
    'invitro_DA_neurons_twin_PD_rp4'],
    ['invitro_DA_neurons_WT_pat1_rp1',
    'invitro_DA_neurons_WT_pat1_rp2',
    'invitro_DA_neurons_WT_pat2_rp1',
    'invitro_DA_neurons_WT_pat2_rp2',
    'invitro_DA_neurons_WT_pat3_rp1',
    'invitro_DA_neurons_WT_pat3_rp2',
    'invitro_DA_neurons_WT_pat4_rp1',
    'invitro_DA_neurons_WT_pat4_rp2',
    'invitro_DA_neurons_WT_pat5_rp1',
    'invitro_DA_neurons_WT_pat5_rp2'],
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
    ['Late_blastocyst_E1_C1_pTE', 'Late_blastocyst_E1_C10_pTE', 'Late_blastocyst_E1_C11_pTE', 'Late_blastocyst_E1_C2_pTE', 'Late_blastocyst_E1_C3_pTE', 'Late_blastocyst_E1_C5_pTE', 'Late_blastocyst_E1_C8_pTE', 'Late_blastocyst_E2_C10_pTE', 'Late_blastocyst_E2_C9_pTE', ],
    ['Late_blastocyst_E1_C4_mTE', 'Late_blastocyst_E1_C12_mTE', 'Late_blastocyst_E1_C6_mTE', 'Late_blastocyst_E1_C7_mTE', 'Late_blastocyst_E1_C9_mTE', 'Late_blastocyst_E2_C4_mTE', 'Late_blastocyst_E2_C5_mTE', 'Late_blastocyst_E2_C6_mTE', 'Late_blastocyst_E2_C7_mTE', ],
    ['Late_blastocyst_E2_C1_EPI', 'Late_blastocyst_E2_C2_EPI', 'Late_blastocyst_E2_C3_EPI', 'Late_blastocyst_E2_C8_EPI', 'Late_blastocyst_E3_C1_EPI'],
    ['Late_blastocyst_E3_C2_PE', 'Late_blastocyst_E3_C3_PE', 'Late_blastocyst_E3_C4_PE', 'Late_blastocyst_E3_C5_PE', 'Late_blastocyst_E3_C6_PE', 'Late_blastocyst_E3_C7_PE', 'Late_blastocyst_E3_C8_PE'],
    ['Liver_rp1', 'Liver_rp2', 'Liver_rp3', 'Liver_rp4'],
    ['Lung_rp2', 'Lung_rp3'],
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
    ['Morula_E1_C1', 'Morula_E1_C2', 'Morula_E1_C3', 'Morula_E1_C4', 'Morula_E1_C5', 'Morula_E1_C6', 'Morula_E1_C7', 'Morula_E1_C8', 'Morula_E2_C1', 'Morula_E2_C2', 'Morula_E2_C3', 'Morula_E2_C4', 'Morula_E2_C5', 'Morula_E2_C6', 'Morula_E2_C7', 'Morula_E2_C8'],
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
    ['Oocyte_rp1', 'Oocyte_rp2', 'Oocyte_rp3', 'Oocyte_rp4', 'Oocyte_rp5'],
    #['Oocyte E1 C1', 'Oocyte E2 C1', 'Oocyte E3 C1'],
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
    ['Retina_rp1', 'Retina_rp2', 'Retina_rp3'], # Same study, same lab, but # 3 is an outlier from the other two...
    ['Saphenous_vein_endothelial_cells_rp1', 'Saphenous_vein_endothelial_cells_rp2'],
    ['Skeletal_muscle_rp1', 'Skeletal_muscle_rp2', 'Skeletal_muscle_rp3', 'Skeletal_muscle_cells_rp3', 'Skeletal_muscle_cells_rp4', 'Skeletal_muscle_cells_rp5', 'Skeletal_muscle_cells_rp6', 'Skeletal_muscle_cells_rp7', 'Skeletal_muscle_cells_rp8', 'Skeletal_muscle_cells_rp9', 'Skeletal_muscle_cells_rp10', 'Skeletal_muscle_cells_rp11', 'Skeletal_muscle_cells_rp12', 'Skeletal_muscle_cells_rp13', 'Skeletal_muscle_cells_rp14', 'Skeletal_muscle_cells_rp15', 'Skeletal_muscle_cells_rp16', 'Skeletal_muscle_cells_rp17', 'Skeletal_muscle_cells_rp18', 'Skeletal_muscle_cells_rp19', 'Skeletal_muscle_cells_rp20', 'Skeletal_muscle_cells_rp21', 'Skeletal_muscle_cells_rp22', 'Skeletal_muscle_cells_rp23', 'Skeletal_muscle_cells_rp24', 'Skeletal_muscle_cells_rp25', 'Skeletal_muscle_cells_rp26', 'Skeletal_muscle_cells_rp27'],
    ['Skeletal_muscle_myotube_rp1', 'Skeletal_muscle_myotube_rp2'],
    ['Sperm_rp1', 'Sperm_rp2', 'Sperm_rp3', 'Sperm_rp4', 'Sperm_rp5'],
    ['Testes_rp1', 'Testes_rp2'],
    ['Thyroid_rp1', 'Thyroid_rp2'],
    ['trophoblast_invitro_rp1', 'trophoblast_invitro_rp2'],
    ['Umbilical_vein_endothelial_cells_rp1', 'Umbilical_vein_endothelial_cells_rp2'],
    ['Villious_mesenchymal_fibroblasts_rp1', 'Villious_mesenchymal_fibroblasts_rp2'],
    ['White_preadipocytes_rp1', 'White_preadipocytes_rp2'],
    ['Zygote_rp1', 'Zygote_rp2', 'Zygote_E1_C1', 'Zygote_E2_C1', 'Zygote_E3_C1'],
    output_pears="Pearson_correlations.tsv",
    pearson_hist="Pearson_histogram.png",
    threshold=0.7,
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
