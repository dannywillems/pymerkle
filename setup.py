try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pymerkle',
    version='0.0.1',
    description='Merkle tree data structure library',
    long_description=open('README.rst').read(),
    author='Danny Willems',
    author_email='contact@danny-willems.be',
    url='https://github.com/dannywillems/pymerkle',
    packages=['pymerkle'],
    license='LGPL',
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest"
    ],
    install_requires=[
    ],
)
