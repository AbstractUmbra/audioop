from setuptools import Extension, setup

# While the code is compatible with 3.12 because of the Limited API version,
# install is limited to >=3.13 in package metadata to avoid clobbering the stdlib audioop.

extensions = [
    Extension(
        name="audioop._audioop",
        sources=["audioop/_audioop.c"],
        depends=["audioop/_audioop.c.h"],
        define_macros=[("Py_LIMITED_API", "0x030C0000")],
        py_limited_api=True,
    )
]

options = {"bdist_wheel": {"py_limited_api": "cp312"}}

setup(ext_modules=extensions, options=options)
