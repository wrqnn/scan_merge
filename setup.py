#!/usr/bin/env python3
"""Setuptools configuration."""

from setuptools import setup, find_packages

setup(
    name='scan_merge',
    version='1.0',
    description='Tool to merge ',
    author='Arvid Norlander',
    author_email='VorpalBlade@users.noreply.github.com',
    url='https://github.com/VorpalBlade/scan_merge',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: TODO',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Topic :: Multimedia :: Graphics :: Capture :: Scanners',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'argcomplete',
        'funcy',
        'pypdf2'
    ],
    entry_points={'console_scripts': [
        'scan_merge=scan_merge:main',
    ]},
)