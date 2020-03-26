#!/usr/bin/env python

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='click-alias',
    version='1.0.1',
    description='Enable aliases for Click',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Hot Off The Hamster',
    author_email='hotoffthehamster@gmail.com',
    url='https://github.com/hotoffthehamster/click-alias',
    license='MIT',
    packages=['click_alias'],
    install_requires=[
        'click',
    ],
    extras_require={
        'dev': [
            'flake8',
            'flake8-import-order',
            'tox-travis',
            'pytest',
            'pytest-cov',
            'coveralls',
            'wheel',
        ]
    }
)
