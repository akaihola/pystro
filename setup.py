from distutils.core import setup

import os
import tempfile

setup(
    name='pystro',
    version=__import__('pystro').__version__,
    description='Python string manipulation library',
    author='Antti Kaihola',
    author_email='akaihol+pystro@ambitone.com',
    packages=['pystro'],
    py_modules=['pystro.specialchars', 'pystro.itertools'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ]
)
