#! /usr/bin/env python3
"""Install script."""

from setuptools import setup


setup(
    name='tenantcalendar',
    use_scm_version={
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm'],
    install_requires=[
        'cmslib',
        'comcatlib',
        'hwdb',
        'mdb',
        'peewee',
        'peeweeplus',
        'werkzeug',
        'wsgilib'
    ],
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info@homeinfo.de>',
    maintainer='Richard Neumann',
    maintainer_email='<r.neumann@homeinfo.de>',
    packages=['tenantcalendar'],
    license='GPLv3',
    description='Tenant calendar library.'
)
