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
        newRotate = "TRACKBALL"
        oldRotate = bpy.context.preferences.inputs.view_rotate_method
        if oldRotate == "TRACKBALL":
            newRotate = "TURNTABLE"

        print("Swapping to: " + newRotate)
        bpy.context.preferences.inputs.view_rotate_method = newRotate
        # print(bpy.context.preferences.inputs.view_rotate_method)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OrbitToggleOperator)

def unregister():
    bpy.utils.unregister_class(OrbitToggleOperator)

if __name__ == "__main__":
    register()

