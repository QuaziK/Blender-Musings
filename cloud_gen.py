import bpy

C = bpy.context
D = bpy.data

# generate MetaBall and convert it to mesh
bpy.ops.object.metaball_add(type='BALL', radius=2, enter_editmode=False, align='WORLD', location=C.scene.cursor.location, scale=(1, 1, 1))
bpy.ops.object.convert(target='MESH')
cloud_mesh = C.selected_objects[-1]

# add subsurf
bpy.ops.object.modifier_add(type='SUBSURF')
C.object.modifiers["Subdivision"].render_levels = 1

# create cloud texture
tex = D.textures.new("Cloud", 'CLOUDS')
tex.noise_scale = 1

# add displacement modifier
modifier = cloud_mesh.modifiers.new(name="Displace", type='DISPLACE')

# set texture to cloud texture
modifier.texture = D.textures['Cloud']

# hide in render and viewport
cloud_mesh.hide_render = True
cloud_mesh.hide_set(True)

# generate empty volume
bpy.ops.object.volume_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
cloud_volume = C.selected_objects[-1]

# add mesh to volume modifier and set parameters
bpy.ops.object.modifier_add(type='MESH_TO_VOLUME')
C.object.modifiers["Mesh to Volume"].object = cloud_mesh
C.object.modifiers["Mesh to Volume"].voxel_amount = 200

# add volume displace modifier and set texture
modifier = cloud_volume.modifiers.new(name="Volume Displace", type='VOLUME_DISPLACE')
modifier.texture = D.textures['Cloud']
