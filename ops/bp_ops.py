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
                       

class bp_OT_split_region(Operator):
    bl_idname = "bp.split_region"
    bl_label = "Split Region"
    bl_description = "This will split the current interface"
    
    space_type: StringProperty(name="Space Type")
    space_sub_type: StringProperty(name="Space Sub Type")
    split_direction: StringProperty(name="Split Direction")
    split_factor: FloatProperty(name="Factor")

    sub_type_editors = {"DOPESHEET_EDITOR","IMAGE_EDITOR","CLIP_EDITOR"}

    def execute(self, context):
        #LOAD ALL AREAS INTO A LIST
        areas = []
        for window in context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:
                areas.append(area)

        #SPLIT CURRENT AREA
        bpy.ops.screen.area_split(direction=self.split_direction,factor=self.split_factor)

        #LOOK FOR NEW AREA THAT IS NOT IN LIST THEN SET THE TYPE
        for window in context.window_manager.windows:
            screen = window.screen
            for area in screen.areas:           
                if area not in areas:      
                    area.type = self.space_type
                    for space in area.spaces:
                        if space.type in self.sub_type_editors and self.space_sub_type != "":
                            space.mode = self.space_sub_type
        return {'FINISHED'}

classes = (
    bp_OT_split_region,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()                            