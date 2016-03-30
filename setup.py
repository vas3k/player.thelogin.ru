# -*- coding=utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

import logging

from setuptools import find_packages, setup

logger = logging.getLogger(__name__)


setup(
    name="player",
    version="0.0.0",
    author="themylogin",
    packages=find_packages(exclude=[]),
    test_suite="nose.collector",
    install_requires=[
        "alembic",
        "beautifulsoup4",
        "celery",
        "Flask",
        "Flask-Script",
        "Flask-SQLAlchemy",
        "html2text",
        "mutagen",
        "numpy",
        "pillow",
        "pyinotify",
        "python-mpd2",
        "raven",
        "requests",
        "scikit-image",
        "themyutils",
    ],
)
