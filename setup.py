#!/usr/bin/env python

from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='click-hotoffthehamster-alias',
    # Latest click-contrib/master: f7e4dd40 2019-08-24 v1.0.1.
    # - (lb): "Upstream" uses 'v' prefix in version tags, but not
    #   me, so can tag 1.0.1.
    version='1.0.1a1',
    description='Add aliases to click-hotoffthehamster commands',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Hot Off The Hamster',
    author_email='hotoffthehamster@gmail.com',
    url='https://github.com/hotoffthehamster/click-hotoffthehamster-alias',
    license='MIT',
    packages=['click_hotoffthehamster_alias'],
    install_requires=[
        'click-hotoffthehamster >= 7.1.1 , < 8',
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
