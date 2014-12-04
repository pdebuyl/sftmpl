from setuptools import setup
from os import path

import sftmpl

setup(name="sftmpl",
      version=sftmpl.__version__,
      description="Single file templater",
      long_desc = open('README.rst','r').read(),
      author=sftmpl.__author__,
      author_email="pdebuyl at sign pdebuyl dot be",
      license="BSD",
      url="http://github.com/pdebuyl/sftmpl",
      packages = ['sftmpl'],
      entry_points={
          'console_scripts': [
              'sftmpl=sftmpl:main',
          ],
      },
)

