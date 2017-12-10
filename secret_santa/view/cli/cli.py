"""Contains the CLI class."""

import sys
import getopt

from santa.matchmaker import Matchmaker
from santa.person_file_parser import PersonFileParser
from santa.message_template import MessageTemplate


class CLI:
    """CLI that reads command line arguments and runs the program."""

    # getopt command line arguments
    SHORT_ARGS = 'hp:m:t:'
    LONG_ARGS = ['help', 'people=', 'message=', 'title=']

    def __init__(self, args):
        """Parse program arguments from the given args array.

        Arg:
            args: Arguments passed to the program.

        Raises:
            ValueError: A necessary command line argument is undefined.
        """
        self._people_filename = None
        self._message_filename = None
        self._title = None

        opts, args = getopt.gnu_getopt(args, self.SHORT_ARGS, self.LONG_ARGS)

        # Extract command line arguments
        for opt, arg in opts:
            if opt in ['-h', '--help']:
                self.usage()
                sys.exit(0)
            elif opt in ['-p', '--people']:
                self._people_filename = arg
            elif opt in ['-m', '--message']:
                self._message_filename = arg
            elif opt in ['-t', '--title']:
                self._title = arg

        if self._people_filename is None:
            raise ValueError('Undefined participants file')

        if self._message_filename is None:
            raise ValueError('Undefined message template file')

        if self._title is None:
            self._title = ''

    @staticmethod
    def usage():
        """Show how to use the program."""
        print('USAGE\n'
              '\tpython ' + sys.argv[0] + ' [-h] [-t "title"]\n'
              '\t       <-p people_file> <-m message_file>\n\n'

              'COMMAND LINE ARGUMENTS\n'
              '\t-p FILE, --people=FILE\n'
              '\t\tUse FILE as a list of participants and their emails, '
              'separated by "' + PersonFileParser.SEP_CHAR + '".\n\n'

              '\t-m FILE, --message=FILE\n'
              '\t\tUse the message template contained in FILE as the body in '
              'sent emails.\n'

              '\t\tAny "' + MessageTemplate.SPECIAL_CHAR +
              MessageTemplate.PERSON_CHAR + '" chars in the message will be '
              'replaced by the receiver\'s name,\n'

              '\t\tand any "' + MessageTemplate.SPECIAL_CHAR +
              MessageTemplate.SANTA_CHAR + '" chars will be replaced by the '
              'receiver\'s santa\'s name.\n\n'

              '\t-t "title", --title="title"\n'
              '\t\tUse "title" as the title for all sent emails, or an empty '
              'string if not specified.\n\n'

              '\t-h, --help\n'
              '\t\tShow how to use the program, leaving it afterwards.')

    def run(self):
        """Run all events to organize a Secret Santa."""
        people = self.__read_people()
        message_template = self.__create_message_template()
        self.__match_people(people)

        for person in people:
            message = message_template.replace(person)
            print(message)

    def __read_people(self):
        """Read participant names and emails from previously specified file.

        Returns:
            A list of Person objects correspondent to each Person in the
            file.
        """
        return PersonFileParser.parse(self._people_filename)

    def __create_message_template(self):
        """Create message template from previously specified file.

        Returns:
            A MessageTemplate object whose template was read the previously
            specified file.
        """
        return MessageTemplate(self._message_filename)

    def __match_people(self, people):
        """Set a secret santa for all Person objects in the people list.

        Arg:
            people: List of Person objects participating in the event.
        """
        Matchmaker.match(people)
