"""Contains the MessageTemplate class."""

import re
import warnings


class MessageTemplate:
    """Reads message template with changeable person and secret santa name."""

    # Character used for patterns
    SPECIAL_CHAR = '$'

    # Character used after SPECIAL_CHAR to designate person name
    PERSON_CHAR = 'p'

    # Character used after SPECIAL_CHAR to designate secret santa name
    SANTA_CHAR = 's'

    def __init__(self, message):
        """Read the message template to be sent to participants.

        Arg:
            message: String representing the message pattern. It may contain
                     patterns using SPECIAL_CHAR And other characters to be
                     replaced later with person and secret santa names,
                     respectively.
        """
        self._message = message

        person_re = '([^\%c])\%c%c' % \
                    (self.SPECIAL_CHAR, self.SPECIAL_CHAR, self.PERSON_CHAR)
        self._person_re = re.compile(person_re)

        santa_re = '([^\%c])\%c%c' % \
                   (self.SPECIAL_CHAR, self.SPECIAL_CHAR, self.SANTA_CHAR)
        self._santa_re = re.compile(santa_re)

        if re.search(self._person_re, self._message) is None:
            warnings.warn('Person name pattern "%s" not found'
                          % self.SPECIAL_CHAR + self.PERSON_CHAR,
                          RuntimeWarning)

        if re.search(self._santa_re, self._message) is None:
            warnings.warn('Secret santa name pattern "%s" not found'
                          % self.SPECIAL_CHAR + self.SANTA_CHAR,
                          RuntimeWarning)

    def replace(self, person):
        """Replace person name and their secret santa in message template.

        Arg:
            person: Person object whose name and secret santa's name will be
                    replaced in the message pattern.

        Returns:
            The message template, written with person name and secret santa.
        """
        # r'\1' returns the character captured before the person/santa pattern
        message = re.sub(self._person_re, r'\1' + person.name, self._message)
        message = re.sub(self._santa_re, r'\1' + person.santa.name, message)
        return message.replace(2*self.SPECIAL_CHAR, self.SPECIAL_CHAR)
