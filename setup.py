# coding: utf-8

"""
    CLOUD API

    IONOS Enterprise-grade Infrastructure as a Service (IaaS) solutions can be managed through the Cloud API, in addition or as an alternative to the \"Data Center Designer\" (DCD) browser-based tool.    Both methods employ consistent concepts and features, deliver similar power and flexibility, and can be used to perform a multitude of management tasks, including adding servers, volumes, configuring networks, and so on.  # noqa: E501

    The version of the OpenAPI document: 6.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup  # noqa: H301
import os
import codecs

NAME = "ionoscloud"
VERSION = "v6.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r', 'utf-8').read()

if os.path.isfile("README.md"):
    long_desc = read('README.md')
else:
    long_desc = "Ionos Cloud API Client Library for Python"

setup(
    name=NAME,
    version=VERSION,
    description="Python SDK for the Ionos Cloud API",
    author='Ionos Cloud',
    author_email='sdk@cloud.ionos.com',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/ionos-cloud/ionos-cloud-sdk-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "CLOUD API"],
    install_requires=REQUIRES,
    packages=['ionoscloud', 'ionoscloud.api', 'ionoscloud.models'],
    include_package_data=True,
    classifiers=[
         'Natural Language :: English',
         'Environment :: Web Environment',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: Apache Software License',
         'Operating System :: POSIX',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3',
         'Topic :: Software Development :: Libraries :: Python Modules',
         'Topic :: Software Development :: Libraries :: Application Frameworks',
         'Topic :: Internet :: WWW/HTTP']
)
