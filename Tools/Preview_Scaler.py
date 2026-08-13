import bpy
from mathutils import Vector

#change the target size if you want bigger drones preview
target_size = 0.9
#assuming the drones have fixed size 0.3
default_size = 0.3
selected_objects = bpy.context.selected_objects

def set_scale(scale_factor,object):
    if scale_factor is not None:
        object.scale.x *= scale_factor.x
        object.scale.y *= scale_factor.y
        object.scale.z *= scale_factor.z

def scale_objects():
    for object in selected_objects:
        scale_factor = None

        if object.dimensions.x < 0.8:
            scale_factor = Vector((target_size / object.dimensions.x, target_size / object.dimensions.x, target_size / object.dimensions.x))
            set_scale(scale_factor,object)
        else:
            scale_factor = Vector((default_size / object.dimensions.x, default_size / object.dimensions.x, default_size / object.dimensions.x))
            set_scale(scale_factor,object)

if selected_objects != []:
    scale_objects()
else:
    print("select a mesh please")