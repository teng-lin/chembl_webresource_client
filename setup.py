#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mnowotka'

import sys

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='chembl_webresource_client',
    version='0.7.0',
    author='Michal Nowotka',
    author_email='mnowotka@ebi.ac.uk',
    description='Python client fot accessing ChEMBL webservices.',
    url='https://www.ebi.ac.uk/chembldb/index.php/ws',
    license='CC BY-SA 3.0',
    packages=['chembl_webresource_client'],
    long_description=open('README.rst').read(),
    install_requires=[
        'requests==2.2.1',
        'requests-cache==0.4.4',
        'grequests==0.2.0',
        'easydict',
    ],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering :: Chemistry'],
    zip_safe=False,
)
