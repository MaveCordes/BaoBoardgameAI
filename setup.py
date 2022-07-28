#!/usr/bin/env python

import os
from setuptools import setup, find_packages

with open(os.path.join("easyAI", "version.py"), "r") as f:
    __version__ = f.read().split(" ")[2].strip("\n").strip('"')

setup(
    name="easyAI",
    version=__version__,
    description="Simple Python Boardgame Bao powered by zulko easyAI",
    long_description=open("README.md").read(),
    license="",
    keywords="Bao AI game powered by easyAI",
    packages=find_packages(exclude="docs"),
    install_requires=["numpy"],
)
