import bpy

bl_info = {
    "name": "Orbit Toggle",
    "description": "Swap between Orbit/Turntable",
    "blender": (3, 4, 0),
    "category": "3D View",
}

# source: https://github.com/aachman98/Sorcar/blob/master/__init__.py#L113
def register_keymaps():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        if "3D View" not in kc.keymaps:
            kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        km = kc.keymaps["3D View"]
        kmi = km.keymap_items.new('orbit_toggle.toggle', 'F5', 'PRESS')

def unregister_keymaps():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps["3D View"]
        for kmi in km.keymap_items:
            if kmi.idname == 'orbit_toggle.toggle':
                km.keymap_items.remove(kmi)
                break

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
    register_keymaps()

def unregister():
    bpy.utils.unregister_class(OrbitToggleOperator)
    unregister_keymaps()

if __name__ == "__main__":
    register()

