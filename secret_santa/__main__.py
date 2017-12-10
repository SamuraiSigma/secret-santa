"""Runs the Secret Santa program."""

import sys
from getopt import GetoptError

from view.cli.cli import CLI


if __name__ == '__main__':
    cli = None

    try:
        cli = CLI(sys.argv[1:])
    except (GetoptError, ValueError) as err:
        print('Error:', err)
        CLI.usage()

    if cli is not None:
        cli.run()
