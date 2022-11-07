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
from OCC.Core.TDataStd import TDataStd_Integer
from OCC.Core.TDocStd import TDocStd_Document
from OCC.Core.TDF import (TDF_Tool, TDF_TagSource,
                          TDF_ChildIterator,)


def get_entry(label):
    """Return entry of label"""
    entry_str = TCollection_AsciiString()
    TDF_Tool.Entry(label, entry_str)
    entry = entry_str.ToCString()
    return entry

# Create a document
title = "Main document"
doc = TDocStd_Document(TCollection_ExtendedString(title))
root = doc.Main()
