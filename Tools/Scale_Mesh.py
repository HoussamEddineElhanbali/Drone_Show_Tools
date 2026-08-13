import bpy
from mathutils import Vector

#set the minimum distance you want between vertices
distance_target = 1.5

selected_object = bpy.context.active_object

def scale_object():
    vertices = []

    for vertex in selected_object.data.vertices:
        vertices.append(vertex.co)

    minimum_distance = 0
    #always multiply to world matrix(world coordinates) to get the distance between vertices in the world space to avoid repetition scaling
    world_scale = selected_object.matrix_world

    for i in range(len(vertices)):

        for j in range(i + 1, len(vertices)):
            holder = (vertices[i] @ world_scale - vertices[j] @ world_scale).length

            if minimum_distance == 0 or minimum_distance > holder:
                minimum_distance = holder

    factor = distance_target / minimum_distance
    print(factor)

    selected_object.scale = (selected_object.scale.x * factor, selected_object.scale.y * factor, selected_object.scale.z * factor)

if selected_object is not None and selected_object.type == "MESH":
    scale_object()
else:
    print("please select a mesh")