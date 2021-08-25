# Copyright 2021 Arun Donti
# SPDX-License-Identifier: MIT
import setuptools

with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='text-prepender',
    author='Arun Donti',
    author_email='dontirun@gmail.com',
    description="""Add text (like legal text) to the top of code without breaking it.""",  # noqa: E501
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dontirun/text-prepender',
    project_urls={
        'Bug Tracker': 'https://github.com/dontirun/text-prepender/issues',  # noqa: E501
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    entry_points={
        'console_scripts': [
            'text-prepender = textprepender.__main__:main',
        ],
    },
    license='MIT',
    test_suite='unittest',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
