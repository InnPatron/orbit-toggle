import bpy

bl_info = {
    "name": "Orbit Toggle",
    "description": "Swap between Orbit/Turntable",
    "blender": (3, 4, 0),
    "category": "3D View",
}

class OrbitToggleOperator(bpy.types.Operator):
    bl_idname = "orbit_toggle.toggle"
    bl_label = "Toggle Orbit"

    def execute(self, context):
        print(bpy.context.preferences.inputs.ndof_view_rotate_method)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OrbitToggleOperator)

def unregister():
    bpy.utils.unregister_class(OrbitToggleOperator)
    del bpy.types.Scene.sprite_sheet_data

if __name__ == "__main__":
    register()

