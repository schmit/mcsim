# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mcsim',
    version='0.0.1',
    description='Simple module for Monte Carlo simulations',
    long_description=readme,
    author='Sven Schmit',
    author_email='schmit@stanford.edu',
    url='https://github.com/schmit/mc_sim',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
