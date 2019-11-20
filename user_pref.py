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

space_types = [('VIEW_3D',"3D View","3D View"),
               ('IMAGE_EDITOR',"Image Editor","Image Editor"),
               ('NODE_EDITOR',"Node Editor","Node Editor"),
               ('SEQUENCE_EDITOR',"Sequence Editor","Sequence Editor"),
               ('CLIP_EDITOR',"Clip Editor","Clip Editor"),
               ('DOPESHEET_EDITOR',"Dopesheet Editor","Dopesheet Editor"),
               ('GRAPH_EDITOR',"Graph Editor","Graph Editor"),
               ('NLA_EDITOR',"NLA Editor","NLA Editor"),
               ('TEXT_EDITOR',"Text Editor","Text Editor"),
               ('CONSOLE',"Console","Console"),
               ('OUTLINER',"Outliner","Outliner"),
               ('PROPERTIES',"Properties","Properties"),
               ('FILE_BROWSER',"File Browser","File Browser"),
               ('PREFERENCES',"Preferences","Preferences")]    

split_directions = [('HORIZONTAL',"Horizontal","Horizontal"),
                    ('VERTICAL',"Vertical","Vertical")]

sub_type_editors = {"DOPESHEET_EDITOR","IMAGE_EDITOR","CLIP_EDITOR"}

image_editor_modes = [('VIEW',"View","View"),
                      ('UV',"UV","UV"),
                      ('PAINT',"Paint","Paint"),
                      ('MASK',"Mask","Mask")]

node_shader_type = [('OBJECT',"Object","Object"),
                    ('WORLD',"World","World"),
                    ('LINESTYLE',"Line Style","Line Style")]

graph_editor_modes = [('FCURVES',"FCurves","FCurves"),
                      ('DRIVERS',"Drivers","Drivers")]

clip_editor_modes = [('TRACKING',"Tracking","Tracking"),
                     ('MASK',"Mask","Mask")]

dope_sheet_modes = [('DOPESHEET',"Dope Sheet","Dope Sheet"),
                    ('TIMELINE',"Time Line","Time Line"),
                    ('ACTION',"Action","Action"),
                    ('SHAPEKEY',"Shape Key","Shape Key"),
                    ('GPENCIL',"Grease Pencil","Grease Pencil"),
                    ('MASK',"Mask","Mask"),
                    ('CACHEFILE',"Cache File","Cache File")]

class Menu_Item(PropertyGroup):
    space_type: EnumProperty(name="Space Type",items=space_types)

    image_editor_mode: EnumProperty(name="Mode",items=image_editor_modes)
    node_editor_type: EnumProperty(name="Mode",items=node_shader_type)
    clip_editor_mode: EnumProperty(name="Mode",items=clip_editor_modes)
    graph_editor_mode: EnumProperty(name="Mode",items=graph_editor_modes)
    dope_sheet_mode: EnumProperty(name="Mode",items=dope_sheet_modes)

    split_direction: EnumProperty(name="Split Direction",items=split_directions)
    split_factor: FloatProperty(name="Factor",subtype='PERCENTAGE',min=0,max=100)

    is_separator: BoolProperty(name="Is Separator", default=False)

    use_custom_icon: BoolProperty(name="Use Custom Icon")
    icon_name: StringProperty(name="Icon Name")

    def get_icon(self):
        if self.use_custom_icon:
            return self.icon_name

        if self.space_type == 'VIEW_3D':
            return 'VIEW3D'

        if self.space_type == 'IMAGE_EDITOR':
            if self.image_editor_mode == 'VIEW':
                return 'IMAGE'
            if self.image_editor_mode == 'UV':
                return 'UV'
            if self.image_editor_mode == 'PAINT':
                return 'IMAGE'
            if self.image_editor_mode == 'MASK':
                return 'IMAGE'              

        if self.space_type == 'NODE_EDITOR':
            if self.node_editor_type == 'OBJECT':
                return 'NODE_MATERIAL'
            if self.node_editor_type == 'WORLD':
                return 'WORLD_DATA'
            if self.node_editor_type == 'LINESTYLE':
                return 'LINE_DATA'                      

        if self.space_type == 'SEQUENCE_EDITOR':
            return 'SEQUENCE'        

        if self.space_type == 'CLIP_EDITOR':
            if self.clip_editor_mode == 'TRACKING':
                return 'ANIM' 
            if self.clip_editor_mode == 'MASK':
                return 'OVERLAY'        

        if self.space_type == 'DOPESHEET_EDITOR':
            if self.dope_sheet_mode == 'DOPESHEET':
                return 'ACTION'        
            if self.dope_sheet_mode == 'TIMELINE':
                return 'TIME'        
            if self.dope_sheet_mode == 'ACTION':
                return 'ARMATURE_DATA'   
            if self.dope_sheet_mode == 'SHAPEKEY':
                return 'SHAPEKEY_DATA'   
            if self.dope_sheet_mode == 'GPENCIL':
                return 'GREASEPENCIL'   
            if self.dope_sheet_mode == 'MASK':
                return 'OVERLAY'   
            if self.dope_sheet_mode == 'CACHEFILE':
                return 'FILE'   

        if self.space_type == 'GRAPH_EDITOR':
            if self.graph_editor_mode == 'FCURVES':
                return 'GRAPH'        
            if self.graph_editor_mode == 'DRIVERS':
                return 'AUTO'              

        if self.space_type == 'NLA_EDITOR':
            return 'NLA'        
        if self.space_type == 'TEXT_EDITOR':
            return 'TEXT'        
        if self.space_type == 'CONSOLE':
            return 'CONSOLE'        
        if self.space_type == 'OUTLINER':
            return 'OUTLINER'        
        if self.space_type == 'PROPERTIES':
            return 'PROPERTIES'        
        if self.space_type == 'FILE_BROWSER':
            return 'FILEBROWSER'        
        if self.space_type == 'PREFERENCES':
            return 'PREFERENCES'                        

    def draw_space_mode(self,layout):
        if self.space_type == 'IMAGE_EDITOR':
            layout.prop(self,'image_editor_mode')
        elif self.space_type == 'NODE_EDITOR':
            layout.prop(self,'node_editor_type')
        elif self.space_type == 'DOPESHEET_EDITOR':
            layout.prop(self,'dope_sheet_mode')            
        elif self.space_type == 'CLIP_EDITOR':
            layout.prop(self,'clip_editor_mode')
        elif self.space_type == 'GRAPH_EDITOR':
            layout.prop(self,'graph_editor_mode')        
        else:
            pass  

    def set_space_mode(self):
        if self.space_type == 'IMAGE_EDITOR':
            return self.image_editor_mode
        if self.space_type == 'NODE_EDITOR':
            return self.node_editor_type
        if self.space_type == 'CLIP_EDITOR':
            return self.clip_editor_mode
        if self.space_type == 'GRAPH_EDITOR':
            return self.graph_editor_mode      
        if self.space_type == 'DOPESHEET_EDITOR':
            return self.dope_sheet_mode               
        return ""     


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
                    row.prop(menu_item,'space_type',text="Space")
                    row = box.row()
                    menu_item.draw_space_mode(row)
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