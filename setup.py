import sysconfig

from setuptools import Extension, setup


Py_GIL_DISABLED = sysconfig.get_config_var("Py_GIL_DISABLED")
macros = []
options = {}
if not Py_GIL_DISABLED:
    macros.append(("Py_LIMITED_API", "0x030D0000"))
    options["bdist_wheel"] = {"py_limited_api": "cp313"}

extensions = [
    Extension(
        name="audioop._audioop",
        sources=["audioop/_audioop.c"],
        depends=["audioop/_audioop.c.h"],
        define_macros=macros,
        py_limited_api=not Py_GIL_DISABLED,
    )
]

setup(ext_modules=extensions, options=options)
