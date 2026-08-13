import bpy
import bmesh

selection_order = []

def store_selection_order(scene):

    if bpy.context.object and bpy.context.object.mode == "EDIT":
        selected_object = bpy.context.object

        if selected_object.type == "MESH":
            b_mesh = bmesh.from_edit_mesh(selected_object.data)

            for vertex in b_mesh.verts:
                if vertex.select and vertex.index not in selection_order:
                    selection_order.append(vertex.index)

def connect_vertices():
    selected_object = bpy.context.object

    if selected_object and selected_object.type == "MESH" and selected_object.mode == "EDIT":
        b_mesh = bmesh.from_edit_mesh(selected_object.data)

        for i in range(len(selection_order) - 1):
            vertex1 = b_mesh.verts[selection_order[i]]
            vertex2 = b_mesh.verts[selection_order[i + 1]]
            
            if not b_mesh.edges.get((vertex1, vertex2)):
                b_mesh.edges.new((vertex1, vertex2))

        bmesh.update_edit_mesh(selected_object.data)
        selection_order.clear()

class ModalOperator(bpy.types.Operator):
    bl_idname = "wm.vertex_connect"
    bl_label = "connect vertices on escape"

    def modal(self, context, event):

        if event.type == "ESC":
            connect_vertices()
            return {"FINISHED"}

        return {"PASS_THROUGH"}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

def register():
    bpy.utils.register_class(ModalOperator)
    bpy.app.handlers.depsgraph_update_post.clear()
    bpy.app.handlers.depsgraph_update_post.append(store_selection_order)
    bpy.ops.wm.vertex_connect("INVOKE_DEFAULT")

def unregister():
    bpy.utils.unregister_class(ModalOperator)
    bpy.app.handlers.depsgraph_update_post.clear()

if __name__ == "__main__":
    register()