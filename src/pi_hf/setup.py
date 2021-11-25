from setuptools import setup, find_packages
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='pi_hf',
    version='0.0.0',
    description=('Human Factor benchmarking for the walking on stairs protocol.'),
    long_description=long_description,
    author='RRD',
    author_email='whoever@stepbystep.com',
    url='https://github.com/',
    license='Beerware',
    packages= find_packages(),
    scripts=['script/run_pi_hf'],
    entry_points = {
        "console_scripts": ['run_hf = pi_hf:main_script']
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )
