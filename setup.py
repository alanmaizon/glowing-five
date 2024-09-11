# Module 3 - Python - UCD Professional Academy - Alan Maizon

import sys
from setuptools import setup

install_requires = [
    'Flask==2.0.2'
    # other dependencies...
]

if sys.platform == 'win32':
    install_requires.append('pywin32==306')

setup(
    name='glowing-five',
    version='1.0',
    install_requires=install_requires,
    # other setup options...
)
