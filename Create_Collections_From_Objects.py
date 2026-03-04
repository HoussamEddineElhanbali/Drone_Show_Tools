import bpy

selected_objects = bpy.context.selectable_objects
scene_collection = bpy.context.scene.collection

for object in selected_objects:
    new_collection = bpy.data.collections.new(object.name)
    new_collection.objects.link(object)
    scene_collection.children.link(new_collection)
    scene_collection.objects.unlink(object)