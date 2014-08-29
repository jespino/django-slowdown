# -*- coding: utf-8 -*-
from setuptools import setup

description = """
A simple middleware to slow the django response.
"""

setup(
    name = "django-slowdown",
    url = "https://github.com/jespino/django-slowdown",
    author = "Jesús Espino",
    author_email = "jespinog@gmail.com",
    version=':versiontools:slowdown:',
    packages = [
        "slowdown",
    ],
    description = description.strip(),
    install_requires=['django >= 1.3.0'],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    zip_safe=False,
    include_package_data=False,
    package_data = {},
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
