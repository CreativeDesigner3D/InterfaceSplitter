bl_info = {
    "name": "Interface Splitter",
    "author": "Andrew Peel",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D Viewport Header Interface Menu",
    "description": "Adds a new drop down menu to the 3D Viewport that allows you to quickly split the interface",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}

from .ui import bp_view3d_ui_header
from .ops import bp_ops

def register():
    bp_ops.register()
    bp_view3d_ui_header.register()

def unregister():
    bp_ops.unregister()
    bp_view3d_ui_header.unregister()