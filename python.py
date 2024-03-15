# In[]:
# In[]:
from IPython.display import Image
import openmc
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import openmc.lib
# import openmc_source_plotter as osp
import os
from openmc_plasma_source import TokamakSource
import openmc.deplete 
# import openmc_dagmc_wrapper as odw
# import dagmc_h5m_file_inspector as di
# import regular_mesh_plotter as rmp
# from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_geometry

# In[]:
# Materials
water = openmc.Material(name='water')
water.add_element('H',11.111,'wo')
water.add_element('O',88.889,'wo')
water.set_density('g/cc', 1.0 )

helium = openmc.Material(name='helium')
helium.add_element('He',100.0,'wo')
helium.set_density('g/cc', 0.149)

mf82h = openmc.Material(name='mf82f')
mf82h.add_element('C',0.1,'wo')
mf82h.add_element('Al',14e-4,'wo')
mf82h.add_element('V',0.2,'wo')
mf82h.add_element('Cr',7.5,'wo')
mf82h.add_element('Fe',90.11586,'wo')
mf82h.add_element('Co',28e-4,'wo')
mf82h.add_element('Ni',474e-4,'wo')
mf82h.add_element('Cu',100e-4,'wo')
mf82h.add_element('Nb',3.3e-4,'wo')
mf82h.add_element('Mo',21e-4,'wo')
mf82h.add_element('Pd',0.05e-4,'wo')
mf82h.add_element('Ag',0.1e-4,'wo')
mf82h.add_element('Cd',0.4e-4,'wo')
mf82h.add_element('Eu',0.05e-4,'wo')
mf82h.add_element('Tb',0.02e-4,'wo')
mf82h.add_element('Dy',0.05e-4,'wo')
mf82h.add_element('Ho',0.05e-4,'wo')
mf82h.add_element('Er',0.05e-4,'wo')
mf82h.add_element('Ta',0.02,'wo')
mf82h.add_element('W',2,'wo')
mf82h.add_element('Os',0.05e-2,'wo')
# mf82h.add_element('Ir',0.05e-2,'wo')
mf82h.add_element('Bi',0.2e-2,'wo')
mf82h.add_element('U',0.05e-2,'wo')
mf82h.set_density('g/cc', 7.89)

W11TiCNoMo = openmc.Material(name='w11ti')
W11TiCNoMo.add_element('C',0.2206,'wo')
W11TiCNoMo.add_element('O',202e-4,'wo')
W11TiCNoMo.add_element('N',41e-4,'wo')
W11TiCNoMo.add_element('Al',1e-4,'wo')
W11TiCNoMo.add_element('Si',1e-4,'wo')
W11TiCNoMo.add_element('K',1e-4,'wo')
W11TiCNoMo.add_element('Ti',0.8802,'wo')
W11TiCNoMo.add_element('Cr',3e-4,'wo')
W11TiCNoMo.add_element('Fe',8e-4,'wo')
W11TiCNoMo.add_element('Ni',2e-4,'wo')
W11TiCNoMo.add_element('Cu',1e-4,'wo')
W11TiCNoMo.add_element('Mo',12e-4,'wo')
W11TiCNoMo.add_element('Cd',1e-4,'wo')
W11TiCNoMo.add_element('W',98.8718,'wo')
W11TiCNoMo.add_element('Pb',1e-4,'wo')
W11TiCNoMo.set_density('g/cc', 18.1)

pbli = openmc.Material(name='pbli')
pbli.add_element('Pb',99.447,'wo')
pbli.add_nuclide('Li6', 0.4905, 'wo')
pbli.add_nuclide('Li7', 0.0545, 'wo')
pbli.add_element('Zn',10e-4,'wo')
pbli.add_element('Fe',10e-4,'wo')
pbli.add_element('Bi',43e-4,'wo')
pbli.add_element('Cd',5.0e-4,'wo')
pbli.add_element('Ag',5.0e-4,'wo')
pbli.add_element('Sn',5.0e-4,'wo')
pbli.add_element('Ni',2e-4,'wo')
pbli.set_density('g/cc', 9.32)

SS316LN = openmc.Material(name='SS316LN')
SS316LN.add_element('B',0.001,'wo')
SS316LN.add_element('C',0.03,'wo')
SS316LN.add_element('N',0.14,'wo')
SS316LN.add_element('O',0.002,'wo')
SS316LN.add_element('Al',0.05,'wo')
SS316LN.add_element('Si',0.75,'wo')
SS316LN.add_element('P',0.045,'wo')
SS316LN.add_element('K',5e-4,'wo')
SS316LN.add_element('Ti',0.15,'wo')
SS316LN.add_element('V',0.004,'wo')
SS316LN.add_element('Cr',17,'wo')
SS316LN.add_element('Mn',2,'wo')
SS316LN.add_element('Fe',64.9209,'wo')
SS316LN.add_element('Co',12,'wo')
SS316LN.add_element('Ni',0.05,'wo')
SS316LN.add_element('Cu',0.3,'wo')
SS316LN.add_element('Zr',0.002,'wo')
SS316LN.add_element('Nb',0.01,'wo')
SS316LN.add_element('Mo',2.5,'wo')
SS316LN.add_element('Sn',0.002,'wo')
SS316LN.add_element('Ta',0.01,'wo')
SS316LN.add_element('W',0.001,'wo')
SS316LN.add_element('Pb',8e-4,'wo')
SS316LN.add_element('Bi',8e-4,'wo')
SS316LN.set_density('g/cc', 7.93)

eins = openmc.Material(name='eins')
eins.add_element('H',1.96,'wo')
eins.add_element('C',24.12,'wo')
eins.add_element('N',1.46,'wo')
eins.add_element('O',40.19,'wo')
eins.add_element('Mg',3.92,'wo')
eins.add_element('Al',8.6,'wo')
eins.add_element('Si',19.75,'wo')
eins.set_density('g/cc', 1.80)

sic = openmc.Material(name='sic')
sic.add_element('C',29.95,'wo')
sic.add_element('Na',0.05e-4,'wo')
sic.add_element('Si',70.05,'wo')
sic.add_element('K',0.18e-4,'wo')
sic.add_element('Sc',0.013e-4,'wo')
sic.add_element('Cr',0.017e-4,'wo')
sic.add_element('Fe',0.44e-4,'wo')
sic.add_element('Co',0.013e-4,'wo')
sic.add_element('Ni',0.074e-4,'wo')
sic.add_element('Cu',0.048e-4,'wo')
sic.add_element('Zn',0.043e-4,'wo')
sic.add_element('Ga',0.005e-4,'wo')
sic.add_element('As',0.003e-4,'wo')
sic.add_element('Br',0.001e-4,'wo')
sic.add_element('Rb',0.001e-4,'wo')
sic.add_element('Sr',0.012e-4,'wo')
sic.add_element('Zr',0.236e-4,'wo')
sic.add_element('Mo',0.041e-4,'wo')
sic.add_element('Ag',0.002e-4,'wo')
sic.add_element('Cd',0.004e-4,'wo')
sic.add_element('In',0.001e-4,'wo')
sic.add_element('Sb',0.001e-4,'wo')
sic.add_element('Cs',0.001e-4,'wo')
sic.add_element('Ba',0.047e-4,'wo')
sic.add_element('La',0.018e-4,'wo')
sic.add_element('Eu',0.001e-4,'wo')
sic.add_element('Tb',0.001e-4,'wo')
sic.add_element('Yb',0.001e-4,'wo')
sic.add_element('Hf',0.001e-4,'wo')
sic.add_element('Ta',0.001e-4,'wo')
sic.add_element('W',0.032e-4,'wo')
# sic.add_element('Ir',0.001e-4,'wo')
sic.add_element('Pt',0.542e-4,'wo')
sic.add_element('Hg',0.001e-4,'wo')
sic.add_element('Th',0.001e-4,'wo')
sic.add_element('U',0.001e-4,'wo')
sic.set_density('g/cc', 3.217)

wc = openmc.Material(name='wc')
wc.add_element('C',6.0074,'wo')
wc.add_element('O',46.06e-4,'wo')
wc.add_element('N',18.62e-4,'wo')
wc.add_element('Si',92.12e-4,'wo')
wc.add_element('Fe',68.6e-4,'wo')
wc.add_element('Ni',9.8e-4,'wo')
wc.add_element('Al',22.54e-4,'wo')
wc.add_element('Mo',19.6e-4,'wo')
wc.add_element('Mn',9.21e-4,'wo')
wc.add_element('Mg',9.21e-4,'wo')
wc.add_element('Cu',9.212e-4,'wo')
wc.add_element('Ag',9.212e-4,'wo')
wc.add_element('Ca',9.212e-4,'wo')
wc.add_element('W',91.924,'wo')
wc.set_density('g/cc', 15.3174)

JK2LBSteel = openmc.Material(name='JK2LBSteel')
JK2LBSteel.add_element('B',0.002,'wo')
JK2LBSteel.add_element('C',0.02,'wo')
JK2LBSteel.add_element('N',0.2,'wo')
JK2LBSteel.add_element('Si',0.3,'wo')
JK2LBSteel.add_element('P',0.004,'wo')
JK2LBSteel.add_element('S',0.004,'wo')
JK2LBSteel.add_element('Cr',13,'wo')
JK2LBSteel.add_element('Mn',21,'wo')
JK2LBSteel.add_element('Fe',55.47,'wo')
JK2LBSteel.add_element('Ni',9,'wo')
JK2LBSteel.add_element('Mo',1,'wo')
JK2LBSteel.set_density('g/cc', 8.0)

Cr3FS = openmc.Material(name='Cr3FS')
Cr3FS.add_element('C',0.1,'wo')
Cr3FS.add_element('Si',0.14,'wo')
Cr3FS.add_element('V',0.25,'wo')
Cr3FS.add_element('Mn',0.5,'wo')
Cr3FS.add_element('Fe',93.003301,'wo')
Cr3FS.add_element('W',3.0,'wo')
Cr3FS.add_element('Al',30e-4,'wo')
Cr3FS.add_element('Co',8e-4,'wo')
Cr3FS.add_element('Ni',13e-4,'wo')
Cr3FS.add_element('Cu',10e-4,'wo')
Cr3FS.add_element('Nb',0.5e-4,'wo')
Cr3FS.add_element('Mo',5e-4,'wo')
Cr3FS.add_element('Pd',0.05e-4,'wo')
Cr3FS.add_element('Ag',0.05e-4,'wo')
Cr3FS.add_element('Cd',0.05e-4,'wo')
Cr3FS.add_element('Eu',0.02e-4,'wo')
Cr3FS.add_element('Tb',0.02e-4,'wo')
Cr3FS.add_element('Dy',0.05e-4,'wo')
Cr3FS.add_element('Ho',0.05e-4,'wo')
Cr3FS.add_element('Er',0.05e-4,'wo')
Cr3FS.add_element('Os',0.05e-4,'wo')
# Cr3FS.add_element('Ir',0.05e-4,'wo')
Cr3FS.add_element('Bi',0.05e-4,'wo')
Cr3FS.set_density('g/cc', 7.89)

Cu = openmc.Material(name='Cu')
Cu.add_element('C',100.0,'wo')
Cu.set_density('g/cc', 8.44)

TernaryNb3Sn= openmc.Material(name='TernaryNb3Sn')
TernaryNb3Sn.add_element('Nb',68.95,'wo')
TernaryNb3Sn.add_element('Sn',30,'wo')
TernaryNb3Sn.add_element('Ti',1.05,'wo')
TernaryNb3Sn.set_density('g/cc', 8.90)

Lhe = openmc.Material(name='Lhe')
Lhe.add_element('He',100.0,'wo')
Lhe.set_density('g/cc', 0.149)

bmf82h = openmc.Material(name='mf82f')
bmf82h.add_element('B',3.0,'wo')
bmf82h.add_element('C',0.1,'wo')
bmf82h.add_element('Al',14e-4,'wo')
bmf82h.add_element('V',0.2,'wo')
bmf82h.add_element('Cr',7.5,'wo')
bmf82h.add_element('Fe',87.11586,'wo')
bmf82h.add_element('Co',28e-4,'wo')
bmf82h.add_element('Ni',474e-4,'wo')
bmf82h.add_element('Cu',100e-4,'wo')
bmf82h.add_element('Nb',3.3e-4,'wo')
bmf82h.add_element('Mo',21e-4,'wo')
bmf82h.add_element('Pd',0.05e-4,'wo')
bmf82h.add_element('Ag',0.1e-4,'wo')
bmf82h.add_element('Cd',0.4e-4,'wo')
bmf82h.add_element('Eu',0.05e-4,'wo')
bmf82h.add_element('Tb',0.02e-4,'wo')
bmf82h.add_element('Dy',0.05e-4,'wo')
bmf82h.add_element('Ho',0.05e-4,'wo')
bmf82h.add_element('Er',0.05e-4,'wo')
bmf82h.add_element('Ta',0.02,'wo')
bmf82h.add_element('W',2,'wo')
bmf82h.add_element('Os',0.05e-2,'wo')
# bmf82h.add_element('Ir',0.05e-2,'wo')
bmf82h.add_element('Bi',0.2e-2,'wo')
bmf82h.add_element('U',0.05e-2,'wo')
bmf82h.set_density('g/cc', 7.89)

tung = openmc.Material(name='tung')
tung.add_element('W',100,'wo')
tung.set_density('g/cc', 19.35)



# LiAlO2
LiAlO2_mat = openmc.Material(name='lithium_aluminate')
LiAlO2_mat.add_element('Li', 1.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
LiAlO2_mat.add_element('Al', 1.0, percent_type='ao')
LiAlO2_mat.add_element('O', 2.0, percent_type='ao')
LiAlO2_mat.set_density('g/cm3', 2.29675)

# Li2TiO3
Li2TiO3_mat = openmc.Material(name='lithium_titanate')
Li2TiO3_mat.add_element('Li', 2.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
Li2TiO3_mat.add_element('Ti', 1.0, percent_type='ao')
Li2TiO3_mat.add_element('O', 3.0, percent_type='ao')
Li2TiO3_mat.set_density('g/cm3', 3.43)

# LiO2
LiO2_mat = openmc.Material(name='Lithium_oxide')
LiO2_mat.add_element('Li', 2.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
LiO2_mat.add_element('O', 2.0, percent_type='ao')
LiO2_mat.set_density('g/cm3', 2.01)

#Li2ZrO3
Li2ZrO3_mat = openmc.Material(name='lithium_zirconate')
Li2ZrO3_mat.add_element('Li', 2.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
Li2ZrO3_mat.add_element('Zr', 1.0, percent_type='ao')
Li2ZrO3_mat.add_element('O', 3.0, percent_type='ao')
Li2ZrO3_mat.set_density('g/cm3', 4.15)

# Li4SiO4
Li4SiO4_mat = openmc.Material(name='tetralithium_orthosilicate')
Li4SiO4_mat.add_element('Li', 4.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
Li4SiO4_mat.add_element('Si', 1.0, percent_type='ao')
Li4SiO4_mat.add_element('O', 4.0, percent_type='ao')
Li4SiO4_mat.set_density('g/cm3', 2.35)

#Li4TiO4
Li4TiO4_mat = openmc.Material(name='tetralithium_titanium')
Li4TiO4_mat.add_element('Li', 4.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
Li4TiO4_mat.add_element('Ti', 1.0, percent_type='ao')
Li4TiO4_mat.add_element('O', 4.0, percent_type='ao')
Li4TiO4_mat.set_density('g/cm3', 2.5)

#Li4GeO4
Li4GeO4_mat = openmc.Material(name='sb7')
Li4GeO4_mat.add_element('Li', 4.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
Li4GeO4_mat.add_element('Ge', 1.0, percent_type='ao')
Li4GeO4_mat.add_element('O', 4.0, percent_type='ao')
Li4GeO4_mat.set_density('g/cm3', 3.04)

#Li8ZrO6
Li8ZrO6_mat = openmc.Material(name='sb8')
Li8ZrO6_mat.add_element('Li', 8.0, percent_type='ao',
                        enrichment=90,
                        enrichment_target='Li6',
                        enrichment_type='ao'
                        )
Li8ZrO6_mat.add_element('Zr', 1.0, percent_type='ao')
Li8ZrO6_mat.add_element('O', 6.0, percent_type='ao')
Li8ZrO6_mat.set_density('g/cm3', 2.91)


Be12Ti_mat = openmc.Material(name='beryllium_titane')
Be12Ti_mat.add_element('Be', 12.0, percent_type='ao')
Be12Ti_mat.add_element('Ti', 1.0, percent_type='ao')
Be12Ti_mat.set_density('g/cm3', 2.26)

Be_mat = openmc.Material(name='beryllium')
Be_mat.add_element('Be', 1.0, percent_type='ao')
Be_mat.set_density('g/cm3', 1.85)

Be12V_mat = openmc.Material(name='beryllium_v')
Be12V_mat.add_element('Be', 12.0, percent_type='ao')
Be12V_mat.add_element('V', 1.0, percent_type='ao')
Be12V_mat.set_density('g/cm3', 2.28)

# %%
#BW
m1_mat = openmc.Material.mix_materials(
    name='m1',
    materials=[
        mf82h,
        helium
        ],
    fracs=[0.8, 0.2],
    percent_type='vo')
m1_mat.volume=1.142e7/16
m1_mat.depletable=True    
#Divbox
m2_mat = openmc.Material.mix_materials(
    name='m2',
    materials=[
        mf82h,
        helium,
        ],
    fracs=[0.8, 0.2],
    percent_type='vo')
m2_mat.volume=7.763e9/16
m2_mat.depletable=True    
#Div
m3_mat = openmc.Material.mix_materials(
    name='m3',
    materials=[
        mf82h,
        W11TiCNoMo,
        helium
        ],
    fracs=[0.12, 0.41,0.47],
    percent_type='vo')
m3_mat.volume=6.979e6/16
m3_mat.depletable=True    
#Fw
m4_mat = openmc.Material.mix_materials(
    name='m4',
    materials=[
        mf82h,
        helium
        ],
    fracs=[0.34, 0.66],
    percent_type='vo')
m4_mat.volume=1.532e7/16
m4_mat.depletable=True    
#Hemanifold
m5_mat = openmc.Material.mix_materials(
    name='m5',
    materials=[
        mf82h,
        helium
        ],
    fracs=[0.3, 0.7],
    percent_type='vo')
m5_mat.volume=2.226e7/16
m5_mat.depletable=True    
#IBbz    
m6_mat = openmc.Material.mix_materials(
    name='m6', 
    materials=[
        pbli
        ],
    fracs=[1.0],
    percent_type='vo')
m6_mat.volume=4.183e7/16
m6_mat.depletable=True    
#IBcch
m7_mat = openmc.Material.mix_materials(
    name='m7',
    materials=[
        mf82h,
        helium,
        ],
    fracs=[0.58, 0.42],
    percent_type='vo')
m7_mat.volume=3.55E+05
m7_mat.depletable=True      
#IBcc
m8_mat = openmc.Material.mix_materials(
    name='m8',
    materials=[
        SS316LN
        ],
    fracs=[1.0],
    percent_type='vo')
m8_mat.volume=3.67e7
m8_mat.depletable=True    
#IBeins
m9_mat = openmc.Material.mix_materials(
    name='m9',
    materials=[
        eins
        ],
    fracs=[1.0],
    percent_type='vo')
m9_mat.volume=3.09e5
m9_mat.depletable=True    
#IBliner
m10_mat = openmc.Material.mix_materials(
    name='m10',
    materials=[
        sic
        ],
    fracs=[0.46],
    percent_type='vo')
m10_mat.volume=4.31e6
m10_mat.depletable=True    
#IBsr
m11_mat = openmc.Material.mix_materials(
    name='m11',
    materials=[
        mf82h,
        helium,
        wc
        ],
    fracs=[0.28, 0.2,0.52],
    percent_type='vo')
m11_mat.volume=2.31e7
m11_mat.depletable=True    
#IBthshield
m12_mat = openmc.Material.mix_materials(
    name='m12',
    materials=[
        JK2LBSteel,
        helium
        ],
    fracs=[0.5, 0.5],
    percent_type='vo')
m12_mat.volume=2.138e6
m12_mat.depletable=True    
#IBvv
m13_mat = openmc.Material.mix_materials(
    name='m13',
    materials=[
        Cr3FS,
        wc,
        helium
        ],
    fracs=[0.43,0.51,0.06],
    percent_type='vo')
m13_mat.volume=1.23e7
m13_mat.depletable=True    
#IBwp    
m14_mat = openmc.Material.mix_materials(
    name='m14',
    materials=[
        JK2LBSteel,
        Cu,
        TernaryNb3Sn,
        eins,        
        Lhe,
        ],
    fracs=[0.29,0.43,0.06,0.08,0.14],
    percent_type='vo')
m14_mat.volume=5.56e7
m14_mat.depletable=True    
#Kshell    
m15_mat = openmc.Material.mix_materials(
    name='m15',
    materials=[
        W11TiCNoMo
        ],
    fracs=[1.0],
    percent_type='vo')
m15_mat.volume=3.32e6
m15_mat.depletable=True    
#LTshield
m16_mat = openmc.Material.mix_materials(
    name='m16',
    materials=[
        Cr3FS,
        bmf82h,
        water],
    fracs=[0.39,0.29,0.32],
    percent_type='vo')
m16_mat.volume=1.92e8
m16_mat.depletable=True    
#OBbz
m17_mat = openmc.Material.mix_materials(
    name='m17',
    # materials=[
    #     pbli
    #     ],
    # fracs=[1.0],
    # percent_type='vo')  
    materials=[
        pbli
        ],
    fracs=[1.0],
    percent_type='vo')
m17_mat.volume=1.83e8
m17_mat.depletable=True    
#OBbch
m18_mat = openmc.Material.mix_materials(
    name='m18',
    materials=[
        mf82h,
        helium,
        ],
    fracs=[0.58, 0.42],
    percent_type='vo')
m18_mat.volume=1966000
m18_mat.depletable=True    
#OBdivvv
m19_mat = openmc.Material.mix_materials(
    name='m19',
    materials=[
        Cr3FS,
        helium,
        ],
    fracs=[0.6, 0.4],
    percent_type='vo')
m19_mat.volume=8.183e7
m19_mat.depletable=True    
#OBliner    
m20_mat = openmc.Material.mix_materials(
    name='m20',
    materials=[
        sic
        ],
    fracs=[0.46],
    percent_type='vo')
m20_mat.volume=1.681e7
m20_mat.depletable=True    
#Stshield        
m21_mat = openmc.Material.mix_materials(
    name='m21',
    materials=[
        tung
        ],
    fracs=[1.0],
    percent_type='vo')
m21_mat.volume=4.256e6
m21_mat.depletable=True    
#OBsr
m22_mat = openmc.Material.mix_materials(
    name='m22',
    materials=[
        mf82h,
        bmf82h,
        helium
        ],
    fracs=[0.28,0.52,0.20],
    percent_type='vo')
m22_mat.volume=8.673e7
m22_mat.depletable=True    
#Sw    
m23_mat = openmc.Material.mix_materials(
    name='m23',
    materials=[
        mf82h,
        helium,
        ],
    fracs=[0.34,0.66],
    percent_type='vo')
m23_mat.volume=1.319e7
m23_mat.depletable=True    
#Warmor
m24_mat = openmc.Material.mix_materials(
    name='m24',
    materials=[
        tung
        ],
    fracs=[0.913],
    percent_type='vo')
m24_mat.volume=33702.263
m24_mat.depletable=True        
#Divshield
m25_mat = openmc.Material.mix_materials(
    name='m25', 
    materials=[
        mf82h,
        helium
        ],
    fracs=[0.9, 0.1],
    percent_type='vo')
m25_mat.volume=5.932e6
m25_mat.depletable=True    
#IBLTshield
m26_mat = openmc.Material.mix_materials(
    name='m26', 
    materials=[
        Cr3FS,
        wc,
        water,
        ],
    fracs=[0.30,0.37,0.33],
    percent_type='vo')
m26_mat.volume=2.720e7
m26_mat.depletable=True

mats = openmc.Materials([m1_mat,m2_mat,m3_mat,m4_mat,m5_mat,m6_mat,m7_mat,m8_mat,m9_mat,
                         m10_mat,m11_mat,m12_mat,m13_mat,m14_mat,m15_mat,m16_mat,m17_mat,
                         m18_mat,m19_mat,m20_mat,m21_mat,m22_mat,m23_mat,m24_mat,m25_mat,m26_mat])
mats.cross_sections = "/home/fnovais/XS/cross_sections.xml"
# mats.export_to_xml()

# %%
# dagmc_univ = openmc.DAGMCUniverse(filename="new_test.h5m")

# py1 = openmc.Plane(a=0.3826834,b=0.9238795,c=-0.0000000,d=-0.0002050,surface_id=99999999,boundary_type="reflective")
# py2 = openmc.YPlane(y0=0.000050,surface_id=99999998,boundary_type="reflective")
# pz1 = openmc.ZPlane(z0=4130.0,surface_id=99999997,boundary_type="vacuum")
# pz2 = openmc.ZPlane(z0=-4130.0,surface_id=99999996,boundary_type="vacuum")
# px1 = openmc.XPlane(x0=10500.0,surface_id=99999995,boundary_type="vacuum")

# region = ( +py1 & -py2 & -pz1 & +pz2 & -px1)

# containing_cell = openmc.Cell(cell_id=9999, region=region, fill=dagmc_univ)

# model = openmc.Model()
# model.geometry = openmc.Geometry(root=[containing_cell])

# geometry = openmc.Geometry(root=[containing_cell])


dagmc_univ = openmc.DAGMCUniverse(filename="dagmc.h5m")

py1 = openmc.Plane(a=0.3826834,b=0.9238795,c=-0.0000000,d=-0.0002050,surface_id=99999999,boundary_type="reflective")
py2 = openmc.YPlane(y0=0.00000,surface_id=99999998,boundary_type="reflective")
pz1 = openmc.ZPlane(z0=413.0,surface_id=99999997,boundary_type="vacuum")
pz2 = openmc.ZPlane(z0=-413.0,surface_id=99999996,boundary_type="vacuum")
px1 = openmc.XPlane(x0=1050.0,surface_id=99999995,boundary_type="vacuum")

region = ( +py1 & -py2 & -pz1 & +pz2 & -px1)

# region = ( +py1 & -py2)
containing_cell = openmc.Cell(cell_id=9999, region=region, fill=dagmc_univ)

# model = openmc.Model()
# model.geometry = openmc.Geometry(root=[containing_cell])

geometry = openmc.Geometry(root=[containing_cell])
# plot = geometry.plot(basis='xy')
# geometry = openmc.Geometry(root=dagmc_univ)
# geometry.export_to_xml()
# %%
my_source = TokamakSource(
    elongation=2.2,
    ion_density_centre=1.6e20,
    ion_density_peaking_factor=1.52,
    ion_density_pedestal=1.0e20,
    ion_density_separatrix=0.5e20,
    ion_temperature_centre=22,
    ion_temperature_peaking_factor=2.25,
    ion_temperature_pedestal=4.0,
    ion_temperature_separatrix=0.1,
    major_radius=450,
    minor_radius=120.0,
    pedestal_radius=114.0,
    mode="H",
    shafranov_factor=14.4,
    triangularity=0.625,
    ion_temperature_beta=7.5,
    # angles=(5.890486225480862,2*3.141592653589793),
    # sample_size=1000
  ).make_openmc_sources()

# %%
# my_source = openmc.Source()
# radius = openmc.stats.Discrete([4200], [1])

# # the distribution of source z values is just a single value
# z_values = openmc.stats.Discrete([0], [1])

# # the distribution of source azimuthal angles values is a uniform distribution between 0 and 2 Pi
# angle = openmc.stats.Uniform(a=15/16*2*3.14159265359, b=2* 3.14159265359)

# # this makes the ring source using the three distributions and a radius
# my_source.space = openmc.stats.CylindricalIndependent(r=radius, phi=angle, z=z_values, origin=(0.0, 0.0, 0.0))

# # sets the direction to isotropic
# my_source.angle = openmc.stats.Isotropic()

# my_source.energy = openmc.stats.muir(e0=14080000.0, m_rat=5.0, kt=20000.0)

# %%
settings = openmc.Settings()
settings.batches = 30
settings.particles = 10000
# settings.max_tracks = 1000
settings.run_mode = "fixed source"
settings.source = my_source
settings.output = {'tallies':False}
# settings.verbosity = 9
# settings.export_to_xml()
openmc.Settings.weight_windows = 'weight_windows4.h5'
settings.weight_windows = 'weight_windows4.h5'


# settings = openmc.Settings.from_xml('settings.xml')

# %%
# mesh = openmc.RegularMesh()
# mesh.dimension = [250, 250, 200]
# mesh.lower_left = [101.34958471648798, -381.16417913860056, -407.6900000000001]  # x,y,z coordinates start at 0 as this is a sector model
# mesh.upper_right = [996.0300000000002, 0.0, 407.69]
# %%
# makes a mesh tally using the previously created mesh and records heating on the mesh
# mesh_n_tally = openmc.Tally(name="n_flux_on_mesh")
# mesh_n_filter = openmc.MeshFilter(mesh)
# mesh_n_particle_filter = openmc.ParticleFilter('neutron')
# mesh_n_tally.filters = [mesh_n_filter,mesh_n_particle_filter]
# mesh_n_tally.scores = ["flux"]
# tallies = openmc.Tallies([mesh_n_tally])
# tallies.export_to_xml()

# %%
filter1 = openmc.MaterialFilter(m6_mat)
filter2 = openmc.MaterialFilter(m17_mat)
filter3 = openmc.MaterialFilter(m26_mat)

tbr_tally_ib = openmc.Tally(name="TBR_IB")
tbr_tally_ib.scores = ["(n,Xt)"]
tbr_tally_ib.filters = [filter1]

tbr_tally_ob = openmc.Tally(name="TBR_OB")
tbr_tally_ob.scores = ["(n,Xt)"]
tbr_tally_ob.filters = [filter2]

flux_ibvv = openmc.Tally(name="IBLT")
flux_ibvv.scores = ["flux"]
flux_ibvv.filters = [filter3]

# tallies = openmc.Tallies([tbr_tally_ib,tbr_tally_ob])
# tallies.export_to_xml()
# This spectrum tally is on the outer shell and shows then energy distribution
# of neutrons present in the cell.

# energy_filter = openmc.EnergyFilter.from_group_structure('CCFE-709')
# surface_filter = openmc.MaterialFilter(m16_mat)
# outer_surface_spectra_tally = openmc.Tally(name='outer_surface_spectra_tally')
# outer_surface_spectra_tally.scores = ['flux']
# outer_surface_spectra_tally.filters = [surface_filter, energy_filter]
# outer_surface_spectra_tally.id = 12
# %%

umesh = openmc.UnstructuredMesh("dagmc.h5m", library='moab')
mesh_filter = openmc.MeshFilter(umesh)
tally = openmc.Tally()
tally.filters = [mesh_filter]
tally.scores = ['flux']


# umesh2 = openmc.UnstructuredMesh(, library='moab')
# mesh_filter2 = openmc.MeshFilter(umesh2)
# tally2 = openmc.Tally()
# tally2.filters = [mesh_filter2]
# tally2.scores = ['flux']

# tallies = openmc.Tallies([tally,tbr_tally_ib,tbr_tally_ob])
tallies = openmc.Tallies([tally,tbr_tally_ib,tbr_tally_ob,flux_ibvv])
# tallies.export_to_xml()

# %%
model = openmc.model.Model(geometry, mats,settings,tallies)
!rm *.xml *h5
model.export_to_model_xml()

# %%
# sp_file = model.run(mpi_args=['mpiexec','-n','8'])
# sp_file = model.run(threads=8)
# sp_file = model.run(mpi_args=['mpiexec','-n','2'])
model.run()

# %%
import numpy as np
sp = openmc.StatePoint('statepoint.1.h5')
ib_tbr = sp.get_tally(name='TBR_IB')
df1 = ib_tbr.get_pandas_dataframe()

ob_tbr = sp.get_tally(name='TBR_OB')
df2 = ob_tbr.get_pandas_dataframe()

tbr = df1.iloc[0]['mean']+df2.iloc[0]['mean']
std = np.sqrt(df1.iloc[0]['std. dev.']**2+df2.iloc[0]['std. dev.']**2)
print('TBR = '+str(tbr)+' STD = '+str(std))
print()
print('IB = '+str(df1.iloc[0]['mean'])+' and OB = '+str(df2.iloc[0]['mean']))
print()
print('IB = '+str(df1.iloc[0]['std. dev.'])+' and OB = '+str(df2.iloc[0]['std. dev.']))
print()
leakage_mean = sp.global_tallies[3]['mean']
print('Leakage = '+str(leakage_mean))
# %%
from dagmc_geometry_slice_plotter import plot_slice


plot = plot_slice(
    dagmc_file_or_trimesh_object='fnsf_final_2.h5m',
    plane_normal=[0, 0, 1]
)
# %%
model = openmc.model.Model()
model.from_model_xml(path='/home/fnovais/OpenMC_Cubit/model.xml')
model.from_xml(tallies='/home/fnovais/OpenMC_Cubit/tallies.xml')
# %%
with openmc.StatePoint("statepoint.30.h5") as sp:
    tally = sp.tallies[tally.id]

    umesh = sp.meshes[umesh.id]
    centroids = umesh.centroids
    mesh_vols = umesh.volumes

    flux = tally.get_values(scores=['flux']).reshape(umesh.dimension)
    error = tally.get_values(value='rel_err').reshape(umesh.dimension)
data_dict = {'Flux' : flux*1.834368e20/16}
data_dict_2 = {'rel err' : error*100}

umesh.write_data_to_vtk(str(dagmc_univ.filename)+"_flux.vtk", data_dict)
umesh.write_data_to_vtk(str(dagmc_univ.filename)+"_err.vtk", data_dict_2)

# %%
import dagmc_h5m_file_inspector as di

dict_data = di.get_volumes_and_materials_from_h5m("fnsf_final_2.h5m")

flipped = {} 

# iterate over the original dictionary and check if each value is associated 
# with more than one key
for key, value in dict_data.items(): 
    if value not in flipped: 
        flipped[value] = [key] 
    else: 
        flipped[value].append(key) 

# printing all values that are assosiated with more then one key
for key, value in flipped.items():
    if len(value)>=1:
        print(value)  


for i in range(26):
    sum_materials = sum(1 for v in dict_data.values() if v == 'm'+str(i))
    print('m'+str(i)+' = '+str(sum_materials)) 