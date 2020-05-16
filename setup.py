#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
import setuptools

setup(
    name='qyt_devnet',
    version='0.0.2',
    author='cq_bomb',
    author_email='collinsctk@qytang.com',
    url='https://github.com/collinsctk/DevNet_Huawei',
    description=u'乾颐堂',
    packages=setuptools.find_packages(),
    # packages=['qyt_devnet'],
    install_requires=['paramiko', 'paramiko_expect', 'pysnmp'],
    python_requires='>=3.6',
)