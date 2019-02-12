# https://packaging.python.org/tutorials/packaging-projects/
# https://setuptools.readthedocs.io/en/latest/

import ast
import re
import os
from setuptools import find_packages, setup

DEPENDENCIES = []
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURDIR, "README.md"), "r") as f:
    README = f.read()


def get_version() -> str:
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with open(os.path.join(CURDIR, "deduce", "__init__.py"), "r") as init:
        match = _version_re.search(init.read())
        version = match.group("version")
    return str(ast.literal_eval(version))


setup(
    name="deduce",
    version=get_version(),
    author="Florimond Manca",
    author_email="florimond.manca@gmail.com",
    description="String conversion and validation powered by type annotations",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bocadilloproject/deduce",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=[],
    scripts=[],
    zip_safe=False,
    install_requires=DEPENDENCIES,
    python_requires=">=3.6",
    # license and classifier list:
    # https://pypi.org/pypi?%%3Aaction=list_classifiers
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
