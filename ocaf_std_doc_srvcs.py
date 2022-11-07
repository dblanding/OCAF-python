#!/usr/bin/env python
#
# Copyright 2022 Doug Blanding (dblanding@gmail.com)
#
# This file contains the PythonOCC equivalent code for the C++ code
# presented in the Open CASCADE Technology OCAF Documentation at:
# https://dev.opencascade.org/doc/overview/html/occt_user_guides__ocaf.html
#

from OCC.Core.TCollection import (TCollection_AsciiString,
                                  TCollection_ExtendedString)
from OCC.Core.TDocStd import TDocStd_Application, TDocStd_Document
from OCC.Core.XCAFApp import XCAFApp_Application_GetApplication
from OCC.Extend.DataExchange import read_step_file_with_names_colors
from OCC.Core.STEPCAFControl import STEPCAFControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone

# The Application

# There are several different "flavors" of applications & documents
# Here, XDE (Extended Data Exchange) has been chosen, enabling STEP
title = "Main document"
doc = TDocStd_Document(TCollection_ExtendedString(title))
"""
app = XCAFApp_Application_GetApplication()
app.NewDocument(TCollection_ExtendedString("MDTV-XCAF"), doc)
"""
filename = "/home/doug/step-files/as1-oc-214.stp"
step_reader = STEPCAFControl_Reader()
step_reader.SetColorMode(True)
step_reader.SetLayerMode(True)
step_reader.SetNameMode(True)
step_reader.SetMatMode(True)
step_reader.SetGDTMode(True)

status = step_reader.ReadFile(filename)
if status == IFSelect_RetDone:
    step_reader.Transfer(doc)

# see if I can retrieve the app from doc
# app = doc.Application()  # gives runtime error: document has not yet been opened by any application
