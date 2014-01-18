#!/usr/bin/env python3

__doc__ = """
A Raspberry Pi-powered virtual assistant
"""

from setuptools import setup
import sys
import os
import shutil

if sys.version < '3':
	print("Must be run with python3")
elif os.getenv("USER") == "root":
	setup(
		name='pipal',
		version='0.1',
		author='Aaron Lehrian',
		author_email='aaron.lehrian@gmail.com',
		description='A Raspberry Pi-powered virtual assistant ',
		license='GPL v3',
		keywords='pipal lights speech weather assistant',
		url='http://code.google.com/p/pipal',
		packages=[],
		long_description=__doc__,
		classifiers=[
			'Development Status :: 5 - Production/Stable',
			'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
			'Natural Language :: English',
			'Programming Language :: Python :: 3.3',
			'Intended Audience :: End Users/Desktop',
			'Operating System :: POSIX :: Linux',
			'Topic :: Utilities',
			'Topic :: Multimedia :: Sound/Audio :: Speech'
		]
	)
	shutil.copy("./bin/pipal", "/usr/bin")
else:
	print("Must be run as root. Try 'sudo python3 setup.py install'")