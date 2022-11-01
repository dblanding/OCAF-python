#!/usr/bin/env python
#
# Copyright 2022 Doug Blanding (dblanding@gmail.com)
#
# This file contains the PythonOCC equivalent code for the C++ code
# presented in Quaoar's Workshop Lesson 10: First Steps with OCAF
# https://www.youtube.com/playlist?list=PL_WFkJrQIY2iVVchOPhl77xl432jeNYfQ
# The tutorial is intended to allow a student to explore the details of
# some basic OCAF functionality (including savin a document to file).
# This file enables a student to do this using PythonOCC rather than C++.
# File load_doc.py shows how the document can be loaded from file.
# :-)

from OCC.Core.TCollection import (TCollection_AsciiString,
                                  TCollection_ExtendedString,)
from OCC.Core.TDF import TDF_Tool
from OCC.Core.TDataStd import TDataStd_Integer
from OCC.Core.TDocStd import TDocStd_Application, TDocStd_Document
from OCC.Core.BinDrivers import bindrivers_DefineFormat

def get_entry(label):
    """Return entry of label"""
    entry_str = TCollection_AsciiString()
    TDF_Tool.Entry(label, entry_str)
    entry = entry_str.ToCString()
    return entry

# Create an application and document
doc = TDocStd_Document(TCollection_ExtendedString("BinOcaf"))
app = TDocStd_Application()
app.NewDocument(TCollection_ExtendedString("BinOcaf"), doc)

# Sst the document format for save / load
bindrivers_DefineFormat(app)

# Add a root label
mainLab = doc.Main()
print(f"root label has entry [{get_entry(mainLab)}]")

INT = TDataStd_Integer()
INT.Set(199)
mainLab.AddAttribute(INT)
attach = INT.Label()

# Any attributes attached to mainLab?
nb_att = mainLab.NbAttributes()
print(f"Label lab1 has {nb_att} attribute(s) attached")

# Save the document in native Cascade Binary Format
status = app.SaveAs(doc, TCollection_ExtendedString("/home/doug/Desktop/test.cbf"))
if status == 0:
    print("Document saved to file")
else:
    print("Document failed to save")