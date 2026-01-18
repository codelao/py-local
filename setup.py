import os
from setuptools import setup


path = os.path.dirname(__file__)
with open(path + '/README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open(path + '/py_local/__init__.py', 'r') as config:
    contents = config.read()
result = contents.split()
__version__ = result[2][1:-1]

setup(
    name='py-local',
    version=__version__,
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
