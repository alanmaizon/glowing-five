# Module 3 - Python - UCD Professional Academy - Alan Maizon

import sys
from setuptools import setup

install_requires = [
    'Flask==2.0.2',
    'Flask-SocketIO==5.1.1',
    # other dependencies...
]

if sys.platform == 'win32':
    install_requires.append('pywin32==306')

setup(
    name='flask-chat-app',
    version='1.0',
    install_requires=install_requires,
    # other setup options...
)

