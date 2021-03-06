import bpy
from bpy.types import Header, Menu, Operator, UIList, PropertyGroup
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       BoolVectorProperty,
                       PointerProperty,
                       EnumProperty,
                       CollectionProperty)


class cd_OT_add_menu_item(Operator):
    bl_idname = "cd.add_menu_item"
    bl_label = "Add Menu Item"
    bl_description = "This will add a menu item in the interface splitter menu"

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons["InterfaceSplitter"].preferences
        item = addon_prefs.menu_items.add()
        addon_prefs.menu_item_index = len(addon_prefs.menu_items) - 1
        return {'FINISHED'}


class cd_OT_delete_menu_item(Operator):
    bl_idname = "cd.delete_menu_item"
    bl_label = "Delete Menu Item"
    bl_description = "This will delete a menu item in the interface splitter menu"
    
    menu_item_name: StringProperty(name="Menu Item Name")
    ui_type: StringProperty(name="Space Type")
    is_separator: BoolProperty(name="Is Separator")

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons["InterfaceSplitter"].preferences
        for index, item in enumerate(addon_prefs.menu_items):
            if item.name == self.menu_item_name and item.ui_type == self.ui_type and item.is_separator == self.is_separator:
                addon_prefs.menu_items.remove(index)
                break
        return {'FINISHED'}


class cd_OT_split_region(Operator):
    bl_idname = "cd.split_region"
    bl_label = "Split Region"
    bl_description = "This will split the current interface"
    
    ui_type: StringProperty(name="UI Type")
    split_direction: StringProperty(name="Split Direction")
    split_factor: FloatProperty(name="Factor",subtype='PERCENTAGE',min=0,max=100)

    sub_type_editors = {"DOPESHEET_EDITOR","IMAGE_EDITOR","CLIP_EDITOR"}

    def execute(self, context):
        #LOAD ALL AREAS INTO A LIST
        areas = []
        for window in context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                areas.append(area)

        #SPLIT CURRENT AREA
        bpy.ops.screen.area_split(direction=self.split_direction,factor=self.split_factor/100)

        #LOOK FOR NEW AREA THAT IS NOT IN LIST THEN SET THE TYPE
        for window in context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                if area not in areas:
                    area.ui_type = self.ui_type   

        return {'FINISHED'}

classes = (
    cd_OT_add_menu_item,
    cd_OT_delete_menu_item,
    cd_OT_split_region,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()                            