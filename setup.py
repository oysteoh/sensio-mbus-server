# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sensio-mbus-server',     
    version='0.0.1',  
    description='Simple python modbus server with a simple file backend storing data',
    long_description=long_description, 
    long_description_content_type='text/markdown',  
    url='https://github.com/oysteoh/sensio-mbus-server',  
    author='Øystein Olai Heggen', 
    author_email='oystein.heggen@gmail.com',  

    classifiers=[  
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Home Automation :: Modbus',        
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    
    packages=find_packages(exclude=['contrib', 'docs', 'tests']), 

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
 
    install_requires=['socketserver', 'umodbus'],

    entry_points={  
        'console_scripts': [
            'sensio-mbus-server=server:main',
        ],
    }
)