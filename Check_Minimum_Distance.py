import bpy
from mathutils import Vector
import bmesh

selected_object = bpy.context.active_object
vertices = []

def search_for_closest_vertices():

    # gather all vertices in a list
    if selected_object.type == "MESH":

        if selected_object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")

        bpy.ops.mesh.select_all(action="DESELECT")
        bmesh_object = bmesh.from_edit_mesh(selected_object.data)

        for vertex in bmesh_object.verts:
            vertices.append(vertex)
    else:
        print("select a mesh please")
        return
    
    vertices_pair = []
    minimum_distance = 0

    #compare all the vertices and get the minimum distance
    for i in range(len(vertices) - 1):

        for j in range(i + 1, len(vertices)):
            vector_length = (vertices[i].co - vertices[j].co).length

            if minimum_distance == 0 or vector_length < minimum_distance:
                minimum_distance = vector_length
                vertices_pair = [vertices[i],vertices[j]]

    vertices_pair[0].select = True
    vertices_pair[1].select = True

    print(f"minimum distance is : {minimum_distance}")

    bmesh.update_edit_mesh(selected_object.data)

if selected_object is not None:
    search_for_closest_vertices()

else:
    print("select an object please")