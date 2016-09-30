#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


# should be loaded below
__version__ = None

setup(
    name="gitpr",
    version=0.0.1,
    description="Git PR",
    long_description="Buttom to submits PRs to a git repo",
    author="Niall Robinson",
    author_email="niall.robinson@informaticslab.co.uk",
    license="BSD-3-Clause",
    url="https://github.com/informaticslab/notebook-extensions",
    keywords="ipython jupyter",
    classifiers=[
        "Framework :: IPython",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License"
    ],
    packages=["gitpr"],
    setup_requires=["notebook"],
    include_package_data=True,
    entry_points={
        'console_scripts': ['nbpresent=nbpresent.export:main'],
    }
)