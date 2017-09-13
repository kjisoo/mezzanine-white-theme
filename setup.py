import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

    # allow setup.py to be run from any path
    os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="mezzanine-white-theme",
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    author='Kim jisoo',
    author_email='kim@jisoo.net',
    license='MIT License',
    url='https://github.com/kjisoo/mezzanine-white-theme',
    description="Theme for mezzanine",
    long_description=README,
    long_description=README,
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
