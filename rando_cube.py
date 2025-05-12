import bpy
import random

for _ in range(5):

    x, y, z = 3 * [random.randint(-5,5)]
    
    for 
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))

