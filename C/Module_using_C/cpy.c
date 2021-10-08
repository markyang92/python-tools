/*
 * cpy.c
 */

#include <stdio.h>
#include <python3.8/Python.h>


#define HANDLING_1
//#define HANDLING_2

int add(int a, int b){
    printf("add: %d, %d\n", a, b);
    return a+b;
}

PyObject* py_add(PyObject* self, PyObject* args){

#ifdef HANDLING_1
    // Handling Python Args I.
    /* 
     * 1. Get Python args (Tuple) to PyTupleObject* tp.
     * 2. p1 (PyLongObject*) point to tp(Tuple)->[0] (First element in the Tuple)
     */
    PyTupleObject* tp = (PyTupleObject*)args;
    PyLongObject* p1 = (PyLongObject*)(tp->ob_item[0]);
    PyLongObject* p2 = (PyLongObject*)(tp->ob_item[1]);

    int n1 = p1->ob_digit[0]; 
    int n2 = p2->ob_digit[0]; 

    int result = add(n1,n2);

#endif

#ifdef HANDLING_2
    // Handling Python Args II.
    /*
     * 1. PyArg_ParseTuple(args, -> "ii" (int, int), -> &x, &y);
     *    It makes easier deal with python args than over Handling I.
     */

    int x,y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y))
        return NULL;
    int result = add(x,y);
#endif

    // Create PyLongObject instance from the C int result
    PyObject* ret=Py_BuildValue("i", result);
    // You should return 'PyObject*'
    return ret;

}

// This Array has some information about the method in this module.
PyMethodDef Methods[]={
    {"add", py_add, METH_VARARGS, "Integer add"},
    { NULL, NULL, 0, NULL}
};

// cpy module information
struct PyModuleDef cpy_module = {
    PyModuleDef_HEAD_INIT,
    "cpy",                      // Module Name
    "cpy module doc string",    // Doc string
    -1,                         // Size of per-interpreter state or -1
    Methods                     // 함수 정보를 담은 배열 (위)
};

// Init Module
PyMODINIT_FUNC PyInit_cpy(void){
    return PyModule_Create(&cpy_module);
}