from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-dara',
	version=version,
	description="dara metadata schema for ckan",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Hendrik Bunke',
	author_email='h.bunke@zbw.eu',
	url='http://zbw.eu',
	license='BSD',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.dara'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
            'hashids',
            'lxml',
            'toolz'
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here
    dara=ckanext.dara.plugin:DaraMetadataPlugin
	""",
)
