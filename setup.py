import sys
import sysconfig

from setuptools import Extension, setup

if sys.version_info[:2] < (3, 13):
    raise RuntimeError(
        """
        audioop-lts is only for python3.13+.

        audioop is part of the standard library still prior to then.

        If you are installing this from a system package manager
        (eg. pacman, apt, dnf, zypper) please report this
        to the redistribution provided by your distribution,
        as they should not be redistributing it for your python version.

        If you are getting this from pip installing another dependency
        you should inform that dependency.
        """
    )

Py_GIL_DISABLED = sysconfig.get_config_var("Py_GIL_DISABLED")
macros: list[tuple[str, str | None]] = []
options: dict[str, dict[str, str]] = {}
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
