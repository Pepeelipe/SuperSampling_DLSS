#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import bpy

#Operador del addon
class Test_OT_Operator(bpy.types.Operator):
    
    #Informacion del operador
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple operator"
    bl_description = "Center 3D cursor"
    
    #Accion del operador
    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        
        return {'FINISHED'}