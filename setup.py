# Author:
#  Romain Bentz (pixis - @hackanddo)
# Website:
#  https://beta.hackndo.com [FR]
#  https://en.hackndo.com [EN]

import pathlib

from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="lsassy",
    version="3.0.0",
    author="Pixis",
    author_email="hackndo@gmail.com",
    description="Tool to remotely extract credentials",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["assets"]),
    include_package_data=True,
    url="https://github.com/hackanddo/lsassy",
    zip_safe=True,
    license="MIT",
    install_requires=[
        'impacket',
        'netaddr',
        'pypykatz>=0.3.0'
    ],
    python_requires='>=3.6',
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'lsassy = lsassy.lsassy:run',
        ],
    },
    test_suite='tests.tests'
)
