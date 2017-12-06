"""Contains the MessageTemplate class."""

import warnings


class MessageTemplate:
    """Reads message template with changeable person and secret santa name."""

    # Pattern for person name
    PERSON_PATTERN = '\p'

    # Pattern for secret santa name
    SANTA_PATTERN = '\s'

    # Pattern for special character used on person and secret santa beginning
    SPECIAL_CHAR_PATTERN = '\\\\'

    def __init__(self, filename):
        """Read the message template to be sent to participants from a file.

        Arg:
            filename: Name of the file containing the message pattern. The
                      message may contain PERSON_PATTERN and SANTA_PATTERN
                      strings to be replaced later with person and secret
                      santa names, respectively.
        """
        with open(filename) as fd:
            self._message = fd.read()

        if self.PERSON_PATTERN not in self._message:
            warnings.warn('Person name pattern "%s" not found'
                          % self.PERSON_PATTERN, RuntimeWarning)

        if self.SANTA_PATTERN not in self._message:
            warnings.warn('Secret santa name pattern "%s" not found'
                          % self.SANTA_PATTERN, RuntimeWarning)

    def replace(self, person):
        """Replace person name and their secret santa in message template.

        Arg:
            person: Person object whose name and secret santa's name will be
                    replaced in the message pattern.

        Returns:
            The message template, written with person name and secret santa.
        """
        return self._message.replace(self.SPECIAL_CHAR_PATTERN, '\\') \
                            .replace(self.PERSON_PATTERN, person.name) \
                            .replace(self.SANTA_PATTERN, person.santa.name)
