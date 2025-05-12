import bpy
import random
import mathutils
import math

def vector_len(v1):
    return math.sqrt(v1.x**2 + v1.y**2 + v1.z**2)

C = bpy.context
D = bpy.data
CUBE_SIZE = 2
VECTOR_THRESHHOLD = vector_len(mathutils.Vector((CUBE_SIZE,CUBE_SIZE,CUBE_SIZE)))

for _ in range(15):

    x, y, z = random.randint(-5,5),random.randint(-5,5),random.randint(-5,5)

    flag = True

    for obj in D.objects:
        if vector_len(mathutils.Vector((x,y,z)) - obj.location) <= VECTOR_THRESHHOLD:
            flag = False
            
    if flag:    
        bpy.ops.mesh.primitive_cube_add(size=CUBE_SIZE, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
