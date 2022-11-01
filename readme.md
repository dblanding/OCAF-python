# Translating OCAF (Open Cascade Application Framework) code from C++ to Python

* Open CasCade Technology (OCCT) is is a C++ library with pretty good documentation showing you how to use it.
* pythonOCC provides a python wrapper for the OpenCASCADE C++ technology, extending the OCCT audience (mostly C++ developers) to the Python community.
* If you are going to use OpenCascade (either C++ or Python) to make your own application, you  will very likely need to get familiar with OCAF.
    * Unfortunately, there isn't a lot of online documentation showing the details of how to use OCAF in C++.
    * In PythonOCC the available resources are even scarcer.
    * Hence, the impetus for this repository
    * As an example, consider using the TDF_ChildIterator in C++ vs. Python:

C++ code:
``` C++
TDF_ChildIterator itchild;
for (itchild.Initialize(Box2Label,Standard_True); itchild.More();itchild.Next()) {
    aChild = itchild.Value();
    // Do something with aChild
  }
```
Python code:
``` Python
itchild = TDF_ChildIterator()
while itchild.More():
    a_child = itchild.Value()
    # Do something with a_child
    itchild.Next()
```

## This repository is a collection of various PythonOCC code snipets that I have come across relating to the use of OCAF.

#### The [OCAF section of the official OpenCascade documentation](https://dev.opencascade.org/doc/overview/html/occt_user_guides__ocaf.html) does a nice job of explaining how OCAF works and shows several useful C++ code snippets.
* [Here](docs/ocaf_doc.md) I have gone through the C++ code examples and converted them to Python


