from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='PrintTable',
    url='https://github.com/MrRobboWilliamson/print-table',
    author='Rob Williamson',
    author_email='robmwilliamson@gmail.com',
    # Needed to actually package something
    packages=['printable'],
    # Needed for dependencies
    install_requires=['ordered-set==4.0.2'],
    # *strongly* suggested for sharing
    version='0.0.2',
    # The license can be anything you like
    license='MIT',
    description='This package provides a class to print tables nicely in the console',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read(),
)