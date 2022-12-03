import bpy, os
from bpy.utils import register_class, unregister_class

bl_info = {
    "name" : "Render and Shutdown",
    "location" : "Top toolbar > Render > Render Animation and Shutdown",
    "description" : "Adds a menu entry to shut your computer down after rendering",
    "blender" : (3, 3, 0),
    "category" : "Render",
}

class ras(bpy.types.Operator):
    """All select and delete"""
    bl_label = "Render Animation and Shutdown"
    bl_idname = "ras.renderandshutdown"
    bl_description = "Renders the full timeline then shuts your computer down. Shutdown will not occur if the render is interrupted"
    def execute(self, context):
        def get_outta_here(a,b):
            os.system("shutdown /s /t 30")
        bpy.app.handlers.render_complete.append(get_outta_here)
        bpy.ops.render.render('INVOKE_DEFAULT', animation=True, write_still=True)
        return {'FINISHED'}

def menu_draw(self, context):
        self.layout.operator("ras.renderandshutdown")

def wrap(register_bool):
    register_class(ras) if register_bool else unregister_class(ras)
    bpy.types.TOPBAR_MT_render.append(menu_draw) if register_bool else bpy.types.TOPBAR_MT_render.remove(menu_draw)

def register():
    wrap(True)

def unregister():
    wrap(False)

if __name__ == "__main__":
    register()
