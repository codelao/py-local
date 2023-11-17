import os
from py_local import NAME, VERSION
from setuptools import setup


path = os.path.dirname(__file__)
with open(path + '/README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description='Local Network Module for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Lao',
    url='https://github.com/codelao/py-local',
    license='MIT',
    install_requires=[
        'fake-useragent>=1.3.0', 'colorama>=0.4.6'
    ],
    packages=[
        'py_local'
    ]
)
