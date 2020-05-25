#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
import setuptools

setup(
    name='qyt_devnet',
    version='0.0.3',
    author='cq_bomb',
    author_email='collinsctk@qytang.com',
    url='https://github.com/collinsctk/DevNet_Huawei',
    license='GNU General Public License v3.0',
    description=u'乾颐堂网络设备自动化封装',
    packages=setuptools.find_packages(),
    # packages=['qyt_devnet'],
    install_requires=['paramiko', 'paramiko_expect', 'pysnmp'],
    python_requires='>=3.6',
)