#!/usr/bin/env python
# coding: utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Setup script for DollyDolly."""
import os
import setuptools


readme = ''
if os.path.exists('README.md'):
    with open('README.md') as readme_file:
        readme = readme_file.read()

changes = ''
if os.path.exists('CHANGES.md'):
    with open('CHANGES.md') as changes_file:
        changes = changes_file.read()

requirements = []
with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

test_requirements = []

setuptools.setup(
    name = 'my_repo12345',
    version = '0.1.0',
    description = "This app is created from Dolly McDolly",
    long_description = '%s\n\n%s' % (readme, changes),
    author = "Dolly McDolly",
    author_email = 'Dolly@Dolly.com',
    url = 'https://github.com/Dolly@github.com/my_repo12345',
    packages = setuptools.find_packages(),
    package_dir = {'my_repo12345': 'my_repo12345'},
    include_package_data = True,
    install_requires = requirements,
    entry_points = {
        'console_scripts': [
            'my_repo12345 = my_repo12345.my_repo12345:main',
        ]
    },
    license = "MPL 2.0",
    keywords = 'my_repo12345',
    classifiers = [
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Topic :: Software Development :: Testing',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
