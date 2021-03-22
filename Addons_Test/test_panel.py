#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import bpy

#Referencia visual del addon
class Test_PT_Panel(bpy.types.Panel):
    
    #Informacion del addon
    bl_idname = "Test_PT_Panel"
    bl_label = "Test Panel"
    bl_category = "Test addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    #Interfaz del addon                
    def draw(self, context):
        layout = self.layout
                    
        row = layout.row()
        row.operator('view3d.cursor_center', text="Center 3D cursor")