#this script create a custom panel in blender 3d viewport that allows you to execute external python scripts with the click of a button

import bpy
from bpy.types import Panel, Operator

scripts_paths = [
    #this is an example of the path where i store the scripts 
    "C:\\Program Files\\Blender Foundation\\Blender 4.1\\4.1\\scripts\\Houssam\\Preview_Scaler.py",
    "C:\\Program Files\\Blender Foundation\\Blender 4.1\\4.1\\scripts\\Houssam\\Scale_Mesh.py",
    #you can add as many as you want
]

class UserPanel(Panel):
    bl_label = "User Tools" #you can change the name of the panel here
    bl_idname = "PT_CustomPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Drone Show Tools"

    def draw(self,context):
        layout = self.layout
        tool = context.scene.user_tool

        #you can add as many values you want to reference in your scripts
        layout.prop(tool, "custom_value")

        for script in scripts_paths:
            script_name = script.split("\\")[-1]
            layout.operator(ExecuteScriptOperator.bl_idname, text=script_name).script = script

class ExecuteScriptOperator(Operator):
    bl_idname = "script.execute"
    bl_label = "Execute Script"
    script: bpy.props.StringProperty()

    def execute(self, context):
        tool = context.scene.user_tool

        custom_variables = {
            "__name__": "__main__",
            #create the local variable that refers to the custom properties
            "custom_value": tool.custom_value,
            "context": context
        }

        with open(self.script, "r") as script_file:
            exec(script_file.read(), custom_variables)

        return {"FINISHED"}

class UserToolProperties(bpy.types.PropertyGroup):
    #dont forget to decalre the type of each variable you add
    custom_value: bpy.props.IntProperty(name="Custom Value", default=10)

def register():
    bpy.utils.register_class(UserPanel)
    bpy.utils.register_class(ExecuteScriptOperator)
    bpy.utils.register_class(UserToolProperties)
    bpy.types.Scene.user_tool = bpy.props.PointerProperty(type=UserToolProperties)

def unregister():
    bpy.utils.unregister_class(UserPanel)
    bpy.utils.unregister_class(ExecuteScriptOperator)
    bpy.utils.unregister_class(UserToolProperties)
    del bpy.types.Scene.user_tool

if __name__ == "__main__":
    register()