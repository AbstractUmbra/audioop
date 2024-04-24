from setuptools import Extension, setup

extensions = [
    Extension(
        name="audioop._audioop",
        sources=["audioop/_audioop.c"],
        depends=["audioop/_audioop.c.h"],
        define_macros=[("Py_LIMITED_API", "0x030D0000")],
        py_limited_api=True,
    )
]

options = {"bdist_wheel": {"py_limited_api": "cp313"}}

setup(ext_modules=extensions, options=options)
