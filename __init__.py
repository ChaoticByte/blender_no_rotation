import bpy
from mathutils import Euler

def update_rotations(*args):
    for ok, o in bpy.data.objects.items():
        o.rotation_euler = Euler((0, 0, 0))

def register():
    for h in list(bpy.app.handlers.depsgraph_update_pre):
        if h.__name__ == "update_rotations":
            bpy.app.handlers.depsgraph_update_pre.remove(h)
    bpy.app.handlers.depsgraph_update_pre.append(update_rotations)

register()
