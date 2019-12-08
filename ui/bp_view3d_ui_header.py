import bpy
from bpy.types import Header, Menu, Panel, UIList

class InterfaceMenu(bpy.types.Menu):
    bl_label = "Interface"
    bl_idname = "VIEW_MT_interface_menu"

    def draw_default_menu(self,layout):
        props = layout.operator("cd.split_region",text="Outliner",icon='OUTLINER')
        props.ui_type = 'OUTLINER'
        props.split_direction = 'VERTICAL'
        props.split_factor = 20

        props = layout.operator("cd.split_region",text="Properties",icon='PROPERTIES')
        props.ui_type = 'PROPERTIES'
        props.split_direction = 'VERTICAL'
        props.split_factor = 20

        layout.separator()

        props = layout.operator("cd.split_region",text="Material Editor",icon='NODE_MATERIAL')
        props.ui_type = 'ShaderNodeTree'
        props.split_direction = 'VERTICAL'
        props.split_factor = 50

        props = layout.operator("cd.split_region",text="UV Editor",icon='UV')
        props.ui_type = 'UV'
        props.split_direction = 'VERTICAL'
        props.split_factor = 50

        props = layout.operator("cd.split_region",text="Text Editor",icon='TEXT')
        props.ui_type = 'TEXT_EDITOR'
        props.split_direction = 'VERTICAL'
        props.split_factor = 50

        layout.separator()
        
        props = layout.operator("cd.split_region",text="Timeline",icon='TIME')
        props.ui_type = 'TIMELINE'
        props.split_direction = 'HORIZONTAL'
        props.split_factor = 10

        layout = self.layout
        props = layout.operator("cd.split_region",text="Dope Sheet",icon='ACTION')
        props.ui_type = 'DOPESHEET'
        props.split_direction = 'HORIZONTAL'
        props.split_factor = 10

    def draw(self, context):
        layout = self.layout
        preferences = context.preferences
        addon_prefs = preferences.addons["InterfaceSplitter"].preferences

        if len(addon_prefs.menu_items) == 0 or not addon_prefs.use_custom_menu:
            self.draw_default_menu(layout)
        else:
            for item in addon_prefs.menu_items:
                if item.is_separator:
                    layout.separator()
                else:
                    props = layout.operator("cd.split_region",text=item.name,icon=item.get_icon())
                    props.ui_type = item.ui_type
                    props.split_direction = item.split_direction
                    props.split_factor = item.split_factor

class CD_UL_menu_items(UIList):
    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if item.is_separator:
            layout.label(text="---Separator---")
        else:
            try:
                layout.label(text=item.name,icon=item.get_icon())
            except:
                layout.label(text=item.name,icon='BLANK1')
        props = layout.operator('cd.delete_menu_item',icon='X',text="",emboss=False) 
        props.menu_item_name = item.name
        props.ui_type = item.ui_type
        props.is_separator = item.is_separator

def draw_item(self, context):
    layout = self.layout
    layout.menu(InterfaceMenu.bl_idname)

classes = (
    InterfaceMenu,
    CD_UL_menu_items,
)

register, unregister = bpy.utils.register_classes_factory(classes)

bpy.types.VIEW3D_MT_editor_menus.append(draw_item)

if __name__ == "__main__":
    register()                    