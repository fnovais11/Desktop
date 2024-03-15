# # %%
# from pathlib import Path
# from typing import List, Optional
# from pymoab import core, types, rng

# # Initialize PyMOAB Core using a context manager
# mb = core.Core()
# mb.load_file('fnsfsector_void2.mesh.h5m')

# # %%
# # Get tags and entities in a single step
# category_tag = mb.tag_get_handle(types.CATEGORY_TAG_NAME)
# id_tag = mb.tag_get_handle(types.GLOBAL_ID_TAG_NAME)
# name_tag = mb.tag_get_handle(types.NAME_TAG_NAME)
# geom_tag = mb.tag_get_handle(types.GEOM_DIMENSION_TAG_NAME, 1, types.MB_TYPE_INTEGER, types.MB_TAG_DENSE, create_if_missing=True)

# get_volumes = mb.get_entities_by_type_and_tag(mb.get_root_set(), types.MBENTITYSET, [category_tag], ['Volume'])
# get_groups = mb.get_entities_by_type_and_tag(mb.get_root_set(), types.MBENTITYSET, [category_tag], ['Group'])

# # Set data for the name_tag using enumerate
# for m_id, group_ent in enumerate(get_groups, start=1):
#     # mb.tag_set_data(name_tag, group_ent, "mat:{}".format('m' + str(m_id)))
#     mb.tag_set_data(name_tag, group_ent, "mat:{}".format('m' + str(m_id)))
# # Print information
# ids_volumes = sorted(mb.tag_get_data(id_tag, get_volumes, flat=True))
# ids_groups = sorted(mb.tag_get_data(id_tag, get_groups, flat=True))

# print('Volumes:', ids_volumes)
# print('Groups:', ids_groups)
# print('Number of Volumes:', len(get_volumes))
# print('Number of Groups:', len(get_groups))
# # %%
# # Combine material, volume, and group information into a single list of tuples
# entity_info = [(mb.tag_get_data(id_tag, group_ent)[0][0],
#                 mb.tag_get_data(name_tag, group_ent)[0][0],
#                 mb.tag_get_data(id_tag, group_ent)[0][0]) for group_ent in get_groups]

# # Print the combined information
# materials_list, volumes_list, group_list = zip(*entity_info)
# print('Materials:', materials_list)
# print('Volume IDs:', volumes_list)
# print('Group IDs:', group_list)

# # Write the modified mesh to a new file
# mb.write_file('TEMPORARY_FILE.h5m')

# # %%
# from pymoab import core, types, rng
# import dagmc

# # Create PyMOAB Core instance and DAGMC model
# mb = core.Core()
# model = dagmc.DAGModel('TEMPORARY_FILE.h5m')

# print(model.groups)
# print(model.volumes)

# # Get user input for the number of groups
# n_groups = int(input('Enter the number of groups: '))

# # Loop through each group
# for group_id in range(1, n_groups + 1):
#     # Create a new DAGMC group
#     new_group = dagmc.Group.create(model, name="mat:m{}".format(group_id), group_id=group_id)

#     # Get user input for the number of volumes in the group
#     n_volumes = int(input('Enter the number of volumes for group {}: '.format(group_id)))

#     # Loop through each volume in the group
#     for _ in range(n_volumes):
#         # Get user input for the volume number and add the volume to the group
#         volume_id = int(input('Enter volume number: '))
#         new_group.add_set(model.volumes[volume_id])

#     # Print information about the created group
#     print(new_group)


################################################################################

# Access an existing group
# group = model.groups['mat:m1']

# Iterate over volumes and add them to the existing group
# for i in range(2, len(model.volumes) + 1):
#     v1 = model.volumes[i]
#     group.add_set(v1)

# Print the updated list of groups
# print(model.groups)
    


# %%
# import dagmc

# # Create PyMOAB Core instance and DAGMC model
# model = dagmc.DAGModel('bw.mesh.rtt')
# model.volumes

# category_tag = model.category_tag
# name_tag = model.name_tag
# get_groups = model._sets_by_category('Group')

# from pymoab import core
# mb = core.Core()
# model.mb.tag_set_data(name_tag, get_groups, "mat:m1")


# %%
##############################################################################
# Get user input for the number of groups
# n_groups = int(input('Enter the number of groups: '))

# # Loop through each group
# for group_id in range(2, n_groups + 1):
#     # Create a new DAGMC group
#     new_group = dagmc.Group.create(model, name="mat:m{}".format(group_id), group_id=group_id)

#     # Get user input for the number of volumes in the group
#     n_volumes = int(input('Enter the number of volumes for group {}: '.format(group_id)))

#     # Loop through each volume in the group
#     for _ in range(n_volumes):
#         # Get user input for the volume number and add the volume to the group
#         volume_id = int(input('Enter volume number: '))
#         new_group.add_set(model.volumes[volume_id])

#     # Print information about the created group
#     print(new_group)

# Access an existing group
# group = model.groups['mat:m1']

# Iterate over volumes and add them to the existing group
# for i in range(2, len(model.volumes) + 1):
#     v1 = model.volumes[i]
#     group.add_set(v1)

# Print the updated list of groups
# print(model.groups)

# %%
import dagmc

# Create PyMOAB Core instance and DAGMC model
model = dagmc.DAGModel('mesh_10.rtt')
model.volumes

category_tag = model.category_tag
name_tag = model.name_tag
get_groups = model._sets_by_category('Group')

from pymoab import core
mb = core.Core()
model.mb.tag_set_data(name_tag, get_groups, "mat:m1")

# %%
# Get user input for the number of groups
n_groups = int(input('Enter the number of groups: '))

for group_id in range(1, n_groups + 1):
    input_string = input('Enter elements of a list separated by comma: \n')
    user_list = list(map(int, input_string.split(' ')))  # Convert input directly to integers
    
    new_group = dagmc.Group.create(model, name="mat:m{}".format(group_id), group_id=group_id)
    
    for vol_index in user_list:
        try:
            new_group.add_set(model.volumes[vol_index])
        except IndexError:
            print(f"Volume index {vol_index} is out of range.")
    
    print(new_group)

# %%
new_group = dagmc.Group.create(model, name="mat:Vacuum", group_id=30)

new_group.add_set(model.volumes[107])
new_group.add_set(model.volumes[110])
new_group.add_set(model.volumes[111])
new_group.add_set(model.volumes[112])

group = model.groups['mat:m1']
group.remove_set(model.volumes[1])
model.groups
# %%
# Write the modified DAGMC model to a new file
model.write_file('dagmc.h5m')
# %%
