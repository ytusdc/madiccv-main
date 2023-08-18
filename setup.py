#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

from pkg_resources import parse_requirements

# with open("requirements.txt", encoding="utf-8") as fp:
#     install_requires = [str(requirement) for requirement in parse_requirements(fp)]

setup(
    name="madiccv",
    version="1.0.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A short description of your package",
    long_description="eds sdk for python",
    license="Apache License, Version 2.0",
    url="http://test.com",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=find_packages(),
    # install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'test = test.help:main'
        ]
    }
)