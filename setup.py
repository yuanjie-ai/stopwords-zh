#!/usr/bin/env python

"""The setup script."""
import time
from setuptools import setup, find_packages
# from stopwords-zh import __version__

version = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().split('\n')

setup(
    author="stopwords-zh",
    author_email='yuanjie@example.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="stopwords-zh",
    entry_points={
        'console_scripts': [
            'stopwords=stopwords.clis.cli:cli'
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='stopwords-zh',
    name='stopwords-zh',
    packages=find_packages(include=['stopwords', 'stopwords.*']),

    test_suite='tests',
    url='https://github.com/yuanjie-ai/stopwords-zh',
    version=version, # '0.0.0',
    zip_safe=False,
)

