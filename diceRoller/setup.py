from setuptools import setup, find_package

setup(
	name='diceRoller',
	version='1.1',
	package_dir={'dice': ''},
	packages=['dice'],
	description='A simple dice roller.'
	long_description='',
	url='https://github.com/TheKnerd/diceRoller.git',
	author='TheKnerd',
	author_email='kclayengineer@cableone.net',
	license='BSD 3 Clause',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Game Development',
		'License :: OSI Approved :: BSD 3 Clause',
		'Programming Language :: Python :: 2.7',
		],

		keywords='game development dice diceRoller',
	)
