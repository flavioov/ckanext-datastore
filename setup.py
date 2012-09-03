from setuptools import setup, find_packages
import sys, os

# Relase under a dgu sub-release.
version = '0.1.0.dgu1'

setup(
	name='ckanext-datastore',
	version=version,
	description="Provides a web-api to tabular data.",
	long_description="""\
    The CKAN DataStore provides a database for structured storage of data together
    with a powerful Web-accesible Data API, all seamlessly integrated into the CKAN
    interface and authorization system.
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='CKAN team.',
	author_email='ckan-dev@okfn.org',
    url='https://github.com/okfn/ckan/tree/2733-feature-datastore/ckanext/datastore',
	license='AGPL',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.datastore'],
	include_package_data=True,
	zip_safe=False,
    install_requires = [],
	entry_points=\
	"""
    [ckan.plugins]
    datastore=ckanext.datastore.plugin:DatastorePlugin
	""",
)
