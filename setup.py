#!/usr/bin/env python

from distutils.core import setup

setup(
    name='toshibot',
    version='0.1',
    description='Software for Toshi, the ambient robot.',
    author='Ambient Robots',
    author_email='hello@ambientrobots.com',
    url='https://github.com/shantanubala/toshibot',
    packages=['toshibot'],
    install_requires=[
        "click",
        "requests",
        "sh",
    ],
    entry_points={
        'console_scripts': [
            'toshibot = toshibot:cli',
        ],
    }
)