# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md') as file:
    readme = file.read()

with open('LICENSE') as legal:
    license = legal.read()

setup(
    name='civil-register',
    packages=['test'],
    entry_points={'console_scripts': ['runfile = source.build:main']},
    version='1.0.0',
    description='This is a webpage built with Django framework',
    long_description=readme,
    author='Jeaustin Sirias & Felipe Cortes',
    author_email='jeaustin.sirias@ucr.ac.cr',
    url='https://github.com/JeaustinSirias/EIE_Django_project',
    license=license,
    include_package_data=True,
)
 
