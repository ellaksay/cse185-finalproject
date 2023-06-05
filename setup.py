import os
import glob
from setuptools import setup, find_packages

# version-keeping code based on pybedtools
curdir = os.path.abspath(os.path.dirname(__file__))
MAJ = 0
MIN = 0
REV = 0
VERSION = '%d.%d.%d' % (MAJ, MIN, REV)
with open(os.path.join(curdir, 'my_pet/version.py'), 'w') as fout:
        fout.write(
            "\n".join(["",
                       "# THIS FILE IS GENERATED FROM SETUP.PY",
                       "version = '{version}'",
                       "__version__ = version"]).format(version=VERSION)
        )


setup(
    name='SET',
    version=VERSION,
    description='CSE185 SET Trimmer Project',
    author='Brianna Sanchez, Ella Say, Anu Selvaraj',
    entry_points={
        "console_scripts": [
            "set=my_set.set:main"
        ],
    },
)
