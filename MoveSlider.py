import bpy

#change to the number of frames you want to skip 
frames_to_skip = 10
current_frame = bpy.context.scene.frame_current

bpy.context.scene.frame_set(current_frame + frames_to_skip)