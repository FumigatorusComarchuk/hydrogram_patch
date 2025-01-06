import sys

from setuptools import find_packages, setup

MINIMAL_PY_VERSION = (3, 9)
if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError(
        "hydrogram_patch works only with Python {}+".format(
            ".".join(map(str, MINIMAL_PY_VERSION))
        )
    )


setup(
    name="hydrogram_patch",
    version="1.6.1",
    license="MIT",
    author="kotttee",
    python_requires=">=3.9",
    description="This package will add middlewares, routers and fsm for hydrogram",
    url="https://github.com/FumigatorusComarchuk/hydrogram_patch",
    install_requires=[],
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),
)
