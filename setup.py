from setuptools import setup

import sftmpl

setup(name="sftmpl",
      version=sftmpl.__version__,
      description="Single file templater",
      long_description=open('README.rst', 'r').read(),
      author=sftmpl.__author__,
      author_email="pdebuyl at sign pdebuyl dot be",
      license="BSD",
      url="http://github.com/pdebuyl/sftmpl",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
      ],
      packages=['sftmpl'],
      entry_points={
          'console_scripts': [
              'sftmpl=sftmpl:main',
          ],
      },
)
