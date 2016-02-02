import bpy
from bpy import context

charlist = list(map(chr, range(97, 123)));

for letter in charlist:
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.text_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text=letter)
    #bpy.context.space_data.context = 'DATA'
    #bpy.context.object.data.extrude = 0.1
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.convert(target='MESH')
    #bpy.context.space_data.system_bookmarks_active = 1
    bpy.ops.export_scene.fbx(filepath=letter + ".fbx", check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", version='BIN7400', use_selection=False, global_scale=1, apply_unit_scale=True, bake_space_transform=False, object_types={'MESH'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_step=1, bake_anim_simplify_factor=1, use_anim=True, use_anim_action_all=True, use_default_take=True, use_anim_optimize=True, anim_optimize_precision=6, path_mode='COPY', embed_textures=True, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)
