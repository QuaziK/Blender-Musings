import bpy

src_file = "C:\\Users\\Yegor\\Documents\\blender\\Warframe Asset Libs\\Asset Lib (Grineer).blend" 

D = bpy.data

# remove all sup-directories ('dir/mat_name')
for mat in D.materials:
    mat.name = mat.name.split('\\')[-1]
  
# remove all iteration digits and set them all to one material
for o in D.objects:
    for slot in o.material_slots:
        slot.material = D.materials.get(slot.material.name.split('.')[0])

# load materials to replace with
with D.libraries.load(src_file, link=True) as (src, me):
    # dict {key: value} = {material.name: material}
    me.materials = [name for name in src.materials if name in D.materials]
    
replacements = {}
for mat in me.materials:
    new_mat = mat.copy()
    new_mat.name = mat.name
    replacements[new_mat.name] = new_mat
    
# change all materials to newly linked ones
for o in D.objects:
    for slot in o.material_slots:
        try:
            slot.material = replacements[str(slot.material.name.split('.')[0])+".001"]
        except:
            print(f'No replacement for {slot.material.name}')

# purge all unused data blocks
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)