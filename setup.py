from distutils.core import setup

import sfmt

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name="sftmpl",
      version=__version__,
      description="Single file templater",
      long_desc = open('README.rst','r').read(),
      author=sfmt.__author__,
      author_email=
      maintainer="Pierre de Buyl",
      maintainer_email="pdebuyl at sign pdebuyl.be",
      license="BSD",
      url="http://github.com/pdebuyl/pyh5md",
)

