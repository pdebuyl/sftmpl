=====================
Single file templater
=====================

sftmpl takes a single file as input and uses the built-in string format method
to replace the occurences of brace-enclosed variables by values given on the
command-line.

The aim of sftmpl is to simplify the generation of configuration file in
computing protocols by providing a command-line enabled customization of these
configuration files.

Install
-------

Obtain the distribution file and use

    python setup.py install

The source repository is https://github.com/pdebuyl/sftmpl.git and the code may
be obtained via the command

    git clone https://github.com/pdebuyl/sftmpl.git

Use
---

sftmpl uses the curly brace named fields defined in `PEP 3101
<https://www.python.org/dev/peps/pep-3101/>`_.

For the following input file `myconfig.txt`, you must provide the command-line
options `-N`, `--parameter` and `--N_steps`::

    # Config for "myprog"
    N = {N}
    parameter = {parameter}
    
    run {N_steps} steps

The invocation is as follows when sftmpl is installed

    sftmpl myconfig.txt -N 10 --parameter 0.1 --N_steps 500

and the following result is output to the standard output::

    # Config for "myprog"
    N = 10
    parameter = 0.1

    run 500 steps

Misc
----

Author: Pierre de Buyl

License: Modified BSD (see `LICENSE`).
