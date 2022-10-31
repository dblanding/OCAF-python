#!/usr/bin/env python
#
# Copyright 2022 Doug Blanding (dblanding@gmail.com)
#
# This file contains the PythonOCC equivalent code for the C++ code
# presented in the Open CASCADE Technology OCAF Documentation at:
# https://dev.opencascade.org/doc/overview/html/occt_user_guides__ocaf.html
# It has lots of extra snippets of code and print() functions
# sprinkled in to allow a student to explore the details of OCAF
# labels and attributes while using PythonOCC rather than C++.
# :-)

from OCC.Core.TCollection import (TCollection_AsciiString,
                                  TCollection_ExtendedString)
from OCC.Core.TDataStd import TDataStd_Name, TDataStd_Integer
from OCC.Core.TDocStd import TDocStd_Document
from OCC.Core.TDF import (TDF_Tool, TDF_TagSource,
                          TDF_ChildIterator,)
from OCC.Core.XCAFApp import XCAFApp_Application_GetApplication
from OCC.Core.XCAFDoc import (XCAFDoc_DocumentTool_ColorTool,
                              XCAFDoc_DocumentTool_ShapeTool,)


def get_entry(label):
    """Return entry of label"""
    entry_str = TCollection_AsciiString()
    TDF_Tool.Entry(label, entry_str)
    entry = entry_str.ToCString()
    return entry

def get_name(label):
    """Return name of label"""
    return label.GetLabelName()


# Create an application and document with empty root_label
title = "Main document"
doc = TDocStd_Document(TCollection_ExtendedString(title))
app = XCAFApp_Application_GetApplication()
app.NewDocument(TCollection_ExtendedString("MDTV-XCAF"), doc)
shape_tool = XCAFDoc_DocumentTool_ShapeTool(doc.Main())
color_tool = XCAFDoc_DocumentTool_ColorTool(doc.Main())
# type(doc.Main()) = <class 'OCC.Core.TDF.TDF_Label'>
# 0:1 doc.Main().EntryDumpToString()
# 0:1:1   shape_tool is at this label entry
# 0:1:2   color_tool at this entry
# 0:1:1:1 create root_label at this entry
root = shape_tool.NewShape()
name = "Top"  # name for root_label
TDataStd_Name.Set(root, TCollection_ExtendedString(name))

# Tag

# Creating child labels using random delivery of tags
child1 = TDF_TagSource.NewChild(root)
child2 = TDF_TagSource.NewChild(root)
print(get_entry(root))  # 0:1:1:1
print(get_entry(child1))  # 0:1:1:1:1
print(get_entry(child2))  # 0:1:1:1:2

# Creation of a child label by user delivery from a tag
a_child = root.FindChild(27, True)  # new label is created
if not a_child.IsNull():
    tag = a_child.Tag()
    print(f"{tag = }")

a_child = root.FindChild(27, False)  # new label is not created
if not a_child.IsNull():
    a_tag = a_child.Tag()
    print(f"{a_tag = }")  # But it is still found

# Label

# Label creation
root_label_depth = root.Depth()
print(f"\n{root_label_depth = }")  # 3
print(f"root label entry is {get_entry(root)}\n")  # 0:1:1:1


# Creating child labels

# creating a label with tag 10 at Root
lab1 = doc.Main().Root().FindChild(10)

# creating labels 7 and 2 on label 10
lab2 = lab1.FindChild(7)
lab3 = lab1.FindChild(2)

level1 = root .FindChild(3)
level2 = level1.FindChild(1)

# Retrieving child labels
itl = TDF_ChildIterator()
itl.Initialize(root)
print("Entries of children of root:")
while itl.More():
    a_child = itl.Value()
    print(f"\t{get_name(a_child)} [{get_entry(a_child)}]")
    itl.Next()

# Retrieving the father label
father = lab3.Father()
print(f"father of lab3 is {get_entry(father)}")
isroot = father.IsRoot()
print(f"father is root: {isroot}")
father = lab1.Father()
print(f"father of lab1 is {get_entry(father)}")
isroot = father.IsRoot()
print(f"father is root: {isroot}")

# Attribute

# Retrieving an attribute from a label
current = level1
INT = TDataStd_Integer()
if current.FindAttribute(TDataStd_Integer.GetID(), INT):
    print("Found it")
else:
    print("Didn't find it")

# Identifying an attribute using a GUID
guid = INT.ID()
print(f"{current = }")  # <class 'TDF_Label'>
print(f"{INT = }")  # <class 'TDataStd_Integer'>
print(f"{guid =  }")  # <class 'Standard_GUID'>

# Attaching an attribute to a label
current.AddAttribute(INT)
attach = INT.Label()
print(f"{attach = }")  # <class 'TDF_Label'>

# Try again to retrieve an attribute from a label
if current.FindAttribute(TDataStd_Integer.GetID(), INT):
    print("Found it")
else:
    print("Didn't find it")

# Testing the attachment to a label
if current.HasAttribute():
    nb_att = current.NbAttributes()
    print(f"The label has {nb_att} attribute(s) attached")

# Removing an attribute from a label
current.ForgetAttribute(guid)

# Test again the attachment to a label
nb_att = current.NbAttributes()
print(f"The label has {nb_att} attribute(s) attached")
