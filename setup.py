# pyright: reportUnknownVariableType=none
from setuptools import Extension, setup

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    cmdclass = {}
else:

    class bdist_wheel_abi3(bdist_wheel):
        def get_tag(self) -> tuple[str, str, str]:
            python, abi, plat = super().get_tag()

            if python.startswith("cp"):
                import sys

                return f"cp3{sys.version_info[1]}", "abi3", plat

            return python, abi, plat

    cmdclass = {"bdist_wheel": bdist_wheel_abi3}

extensions = [
    Extension(
        name="audioop._audioop",
        sources=["audioop/_audioop.c"],
        depends=["audioop/_audioop.c.h"],
        define_macros=[("Py_LIMITED_API", "0x030C0000")],
        py_limited_api=True,
    )
]

setup(ext_modules=extensions, cmdclass=cmdclass)
