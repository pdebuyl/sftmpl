#!/usr/bin/env python
# Copyright 2014 Pierre de Buyl
# License: modified BSD
from __future__ import print_function

"""Single file templater

This program takes a single file as input and uses the built-in string format
method to replace the occurence of brace-enclosed variables by values given on
the command-line.
"""

__author__ = "Pierre de Buyl <pdebuyl at sign pdebuyl.be>"
__version__ = "0.1"


def main():
    import sys
    import argparse

    desc = """Generic templater
    Replaces occurences of the form {variable} by the value of the command-line
    argument "--variable value". Single character variables may use a single
    dash. The output is to standard out.

    Example:
    %s template.txt --name perl

    Will transform "The name is {name}" into "The name is perl" in the output.
    """ % (sys.argv[0],)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, description=desc)
    parser.add_argument('template_file', type=str, help='template file')
    parser.add_argument('args', nargs=argparse.REMAINDER,
                        help=('List of variables to replace in the template '
                              'file of the form --variable value or -x value'))
    args = parser.parse_args()

    EMPTY = 0
    INUSE = 1

    # Parse the content of args.args
    state = EMPTY
    values = {}
    for a in args.args:
        if state == EMPTY:
            if len(a) > 2 and a.startswith('--'):
                key = a[2:]
                state = INUSE
                continue
            elif len(a) == 2 and a.startswith('-'):
                key = a[1:]
                state = INUSE
                continue
            else:
                raise ValueError('Invalid argument')
        if state == INUSE:
            values[key] = a
            state = EMPTY

    if state == INUSE:
        print("Command-line variable %s incomplete" % key, file=sys.stderr)
        sys.exit(0)

    tmpl = open(args.template_file, 'r').read()

    try:
        print(tmpl.format(**values), end='')
    except KeyError:
        for l in tmpl.splitlines():
            try:
                l.format(**values)
            except KeyError as e:
                print("Variable %s is not defined" % e, file=sys.stderr)

if __name__ == '__main__':
    main()
