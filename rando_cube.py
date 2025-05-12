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
CUBE_NUM = 15
AREA = 10

for _ in range(CUBE_NUM):

    x, y, z = random.randint(-AREA,AREA),random.randint(-AREA,AREA),random.randint(-AREA,AREA)

    flag = True

    for obj in D.objects:
        if vector_len(mathutils.Vector((x,y,z)) - obj.location) <= VECTOR_THRESHHOLD:
            flag = False
            
    if flag:    
        bpy.ops.mesh.primitive_cube_add(size=CUBE_SIZE, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))

bpy.ops.object.select_all(action='SELECT')

for obj in C.selected_objects:
    mod = obj.modifiers.new("Bevel", 'BEVEL')
    mod.width = .4
    mod.segments = 4
    
bpy.ops.object.shade_auto_smooth()
