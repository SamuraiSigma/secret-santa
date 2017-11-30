"""Contains the Main class."""

import sys
import getopt

from santa.person_file_parser import PersonFileParser


class Main:
    """Reads command line arguments and runs the Secret Santa program."""

    # Filename containing names and emails of participants
    people_filename = ''

    @classmethod
    def usage(cls):
        """Show how to use the program."""
        print('USAGE:\n'
              '\tpython ' + sys.argv[0] + ' [options] <-p FILE>\n\n'

              'COMMAND LINE ARGUMENTS:\n'
              '\t-h, --help\n'
              '\t\tShow how to use the program, leaving it afterwards.\n\n'

              '\t-p FILE, --people=FILE\n'
              '\t\tUse FILE as a list of participants and their emails, '
              'separated by "' + PersonFileParser.SEP_CHAR + '".')

    @classmethod
    def read_args(cls, argv):
        """Parse arguments from the given argv array.

        Arg:
            argv: Array to be parsed for arguments.
        """
        try:
            opts, args = getopt.gnu_getopt(argv, 'hp:', ['help', 'people='])
        except getopt.GetoptError as err:
            print('Error:', err)
            cls.usage()
            sys.exit(1)

        for opt, arg in opts:
            if opt in ['-h', '--help']:
                cls.usage()
                sys.exit(0)
            elif opt in ['-p', '--people']:
                cls.people_filename = arg

    @classmethod
    def run(cls):
        """Read command line arguments and run Secret Santa."""
        cls.read_args(sys.argv[1:])

        if cls.people_filename == '':
            cls.usage()
            sys.exit(2)

        people = PersonFileParser.parse(cls.people_filename)
        for person in people:
            print(person)


if __name__ == '__main__':
    Main.run()
