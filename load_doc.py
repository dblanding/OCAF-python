#!/usr/bin/env python
#
# Copyright 2022 Doug Blanding (dblanding@gmail.com)
#
# This file contains the PythonOCC code for loading an OCAF document
# previously saved to file by save_doc.py
#
# Together, these two files show how to save and load an OCAF
# document from file using PythonOCC rather than C++.
# :-)

from OCC.Core.TCollection import (TCollection_AsciiString,
                                  TCollection_ExtendedString)
from OCC.Core.TDF import TDF_Tool, TDF_ChildIterator
from OCC.Core.TDataStd import TDataStd_Integer
from OCC.Core.TDocStd import TDocStd_Application, TDocStd_Document
from OCC.Core.BinDrivers import bindrivers_DefineFormat

def get_entry(label):
    """Return entry of label"""
    entry_str = TCollection_AsciiString()
    TDF_Tool.Entry(label, entry_str)
    entry = entry_str.ToCString()
    return entry

app = TDocStd_Application()
bindrivers_DefineFormat(app)
doc = TDocStd_Document(TCollection_ExtendedString("BinOcaf"))
app.Open(TCollection_ExtendedString("/home/doug/Desktop/test.cbf"), doc)

# An integer was saved as an attribute on the root label.
root = doc.Main()
print(f"root label has entry [{get_entry(root)}]")

# Retrieve children of root
itl = TDF_ChildIterator()
itl.Initialize(root)

while itl.More():
    a_child = itl.Value()
    print(f"\t{get_name(a_child)} [{get_entry(a_child)}]")
    itl.Next()
else:
    print("No child labels were found under root")
