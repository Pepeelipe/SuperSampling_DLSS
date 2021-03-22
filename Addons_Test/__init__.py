#!/usr/bin/env python
# coding: utf-8

bl_info = {
    "name" : "Test_addon",
    "author" : "Pepe_Elipe",
    "description" : "simple addon",
    "blender" : (2, 80, 0),
    "location" : "view3D",
    "warning" : "",
    "category" : "Generic"
}

#Modulo de blender en python
import bpy

#Importamos los archivos
from test_op import Test_OT_Operator
from test_panel import Test_PT_Panel

#Creamos las clases
classes = (Test_OT_Operator, Test_PT_Panel)

#Setteamos las funciones register y unregister
register, unregister = bpy.utils.register_classes_factory(classes)