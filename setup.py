from __future__ import absolute_import, unicode_literals

import os

from setuptools import find_packages, setup

version = __import__('logtailer').__version__


def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="nucoro-django-logtailer",
    version=version,
    url='https://github.com/fireantology/django-logtailer',
    license='BSD',
    platforms=['OS Independent'],
    description="Allows to read log files from disk with a tail like web "
                "console on Django admin interface. Nucoro Fork.",
    long_description=read('README.rst'),
    author='Mauro Rocco, Nucoro',
    author_email='support@nucoro.com',
    packages=find_packages(),
    install_requires=(
        'Django>=1.8',
    ),
    include_package_data=True,
    zip_safe=False,
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
