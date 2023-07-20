from setuptools import Extension, setup

extensions = [Extension("audioop", ["audioop.c"])]

setup(ext_modules=extensions)
