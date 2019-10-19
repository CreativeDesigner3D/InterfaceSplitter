import bpy
from bpy.types import Header, Menu, Panel

class InterfaceMenu(bpy.types.Menu):
    bl_label = "Interface Splitter"
    bl_idname = "VIEW_MT_interface_menu"

    def draw(self, context):
        layout = self.layout

        props = layout.operator("bp_general.split_region",text="Outliner",icon='OUTLINER')
        props.space_type = 'OUTLINER'
        props.split_direction = 'VERTICAL'
        props.split_factor = .2

        props = layout.operator("bp_general.split_region",text="Properties",icon='PROPERTIES')
        props.space_type = 'PROPERTIES'
        props.split_direction = 'VERTICAL'
        props.split_factor = .2

        layout.separator()

        props = layout.operator("bp_general.split_region",text="Node Editor",icon='NODETREE')
        props.space_type = 'NODE_EDITOR'
        props.split_direction = 'VERTICAL'
        props.split_factor = .5

        props = layout.operator("bp_general.split_region",text="UV Editor",icon='UV')
        props.space_type = 'IMAGE_EDITOR'
        props.space_sub_type = 'UV'
        props.split_direction = 'VERTICAL'
        props.split_factor = .5

        props = layout.operator("bp_general.split_region",text="Text Editor",icon='TEXT')
        props.space_type = 'TEXT_EDITOR'
        props.split_direction = 'VERTICAL'
        props.split_factor = .5

        layout.separator()
        
        props = layout.operator("bp_general.split_region",text="Timeline",icon='TIME')
        props.space_type = 'DOPESHEET_EDITOR'
        props.space_sub_type = 'TIMELINE'
        props.split_direction = 'HORIZONTAL'
        props.split_factor = .1

        layout = self.layout
        props = layout.operator("bp_general.split_region",text="Dope Sheet",icon='ACTION')
        props.space_type = 'DOPESHEET_EDITOR'
        props.space_sub_type = 'DOPESHEET'
        props.split_direction = 'HORIZONTAL'
        props.split_factor = .1

def draw_item(self, context):
    layout = self.layout
    layout.menu(InterfaceMenu.bl_idname)
            
classes = (
    InterfaceMenu,
)

register, unregister = bpy.utils.register_classes_factory(classes)

bpy.types.VIEW3D_MT_editor_menus.append(draw_item)

if __name__ == "__main__":
    register()                    