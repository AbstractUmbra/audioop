from setuptools import Extension, setup

extensions = [Extension("audioop", ["audioop.c"], py_limited_api=True, define_macros=[("Py_LIMITED_API", "0x030B0000")])]

setup(ext_modules=extensions)
