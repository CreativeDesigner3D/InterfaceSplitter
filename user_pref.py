import bpy
from bpy.types import AddonPreferences, PropertyGroup
from bpy.props import (
        BoolProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty,
        CollectionProperty,
        EnumProperty,
        )

ui_types = [('VIEW_3D',"3D View","3D View"),
            ('VIEW',"Image Editor","Image Editor"),
            ('UV',"UV Editor","UV Editor"),
            ('ShaderNodeTree',"Shader Editor","Shader Editor"),
            ('CompositorNodeTree',"Compositor Editor","Compositor Editor"),
            ('TextureNodeTree',"Texture Node Editor","Texture Node Editor"),
            ('SEQUENCE_EDITOR',"Video Sequencer","Video Sequencer"),
            ('CLIP_EDITOR',"Movie Clip Editor","Movie Clip Editor"),
            ('DOPESHEET',"Dope Sheet","Dope Sheet"),
            ('TIMELINE',"Timeline","Timeline"),
            ('FCURVES',"Graph Editor","Graph Editor"),
            ('DRIVERS',"Drivers","Drivers"),
            ('NLA_EDITOR',"Nonlinear Animation","Nonlinear Animation"),
            ('TEXT_EDITOR',"Text Editor","Text Editor"),
            ('CONSOLE',"Python Console","Python Console"),
            ('INFO',"Info","Info"),
            ('OUTLINER',"Outliner","Outliner"),
            ('PROPERTIES',"Properties","Properties"),
            ('FILE_BROWSER',"File Browser","File Browser"),
            ('PREFERENCES',"Preferences","Preferences")]    

split_directions = [('HORIZONTAL',"Horizontal","Horizontal"),
                    ('VERTICAL',"Vertical","Vertical")]

class Menu_Item(PropertyGroup):
    ui_type: EnumProperty(name="UI Type",items=ui_types)

    split_direction: EnumProperty(name="Split Direction",items=split_directions)
    split_factor: FloatProperty(name="Factor",subtype='PERCENTAGE',min=0,max=100)

    is_separator: BoolProperty(name="Is Separator", default=False)

    use_custom_icon: BoolProperty(name="Use Custom Icon")
    icon_name: StringProperty(name="Icon Name")

    def get_icon(self):
        if self.use_custom_icon:
            return self.icon_name

        if self.ui_type == 'VIEW_3D':
            return 'VIEW3D'

        if self.ui_type == 'VIEW':
            return 'IMAGE'

        if self.ui_type == 'UV':
            return 'UV'

        if self.ui_type == 'ShaderNodeTree':
            return 'NODE_MATERIAL'

        if self.ui_type == 'CompositorNodeTree':
            return 'NODE_COMPOSITING'

        if self.ui_type == 'TextureNodeTree':
            return 'NODE_TEXTURE'                         

        if self.ui_type == 'SEQUENCE_EDITOR':
            return 'SEQUENCE'        

        if self.ui_type == 'CLIP_EDITOR':
            return 'TRACKER'

        if self.ui_type == 'DOPESHEET':
            return 'CON_ACTION'

        if self.ui_type == 'TIMELINE':
            return 'TIME'

        if self.ui_type == 'FCURVES':
            return 'GRAPH'

        if self.ui_type == 'DRIVERS':
            return 'AUTO'

        if self.ui_type == 'NLA_EDITOR':
            return 'NLA'        

        if self.ui_type == 'TEXT_EDITOR':
            return 'TEXT'        

        if self.ui_type == 'CONSOLE':
            return 'CONSOLE'        

        if self.ui_type == 'OUTLINER':
            return 'OUTLINER'        

        if self.ui_type == 'PROPERTIES':
            return 'PROPERTIES'        

        if self.ui_type == 'FILE_BROWSER':
            return 'FILEBROWSER'        

        if self.ui_type == 'PREFERENCES':
            return 'PREFERENCES'                        


class InterfaceSplitter_Pref(AddonPreferences):
    bl_idname = "InterfaceSplitter"

    use_custom_menu: BoolProperty(name="Use Custom Menu",default=False)

    menu_items: CollectionProperty(
        name="Menu Items",
        description="Items that will show in the Interface Splitter Menu",
        type=Menu_Item
    )
    menu_item_index: IntProperty(name="Menu Item Index",description="Index of current selected Menu Item")

    def draw(self, context):
        layout = self.layout
        layout.prop(self,'use_custom_menu')
        if self.use_custom_menu:
            split = layout.split(factor=.35)
            col_list = split.column()
            col_props = split.column()
            col_list.operator('cd.add_menu_item')
            col_list.template_list("CD_UL_menu_items", "", self, "menu_items", self, "menu_item_index", rows=15)

            col_props.label(text="PROPERTIES")

            if len(self.menu_items) > self.menu_item_index:
                menu_item = self.menu_items[self.menu_item_index]

                box = col_props.box()
                row = box.row()
                split = row.split()
                row.prop(menu_item,'is_separator')

                if not menu_item.is_separator:
                    row = box.row()
                    row.prop(menu_item,'name')                
                    row = box.row()
                    row.prop(menu_item,'ui_type',text="Space")
                    row = box.row()
                    row.label(text="Split Direction:")
                    row = box.row()
                    row.prop(menu_item,'split_direction',expand=True)
                    row = box.row()
                    row.label(text="Split Factor:")
                    row.prop(menu_item,'split_factor',text="")
                    row = box.row()
                    row.prop(menu_item,'use_custom_icon')
                    row = box.row()
                    icon = menu_item.get_icon()
                    if menu_item.use_custom_icon:
                        row.prop(menu_item,'icon_name',text="Name")
                    try:
                        row.label(text="Icon",icon=icon)
                    except:
                        row.label(text="Cannot Find Icon")

classes = (
    Menu_Item,
    InterfaceSplitter_Pref,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()        