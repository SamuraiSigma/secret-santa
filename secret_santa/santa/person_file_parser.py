"""Contains the PersonFileParser class."""

from santa.person import Person


class PersonFileParser:
    """Parses a CSV-type file containing Secret Santa participants."""

    # Character for inline comments in file
    COMMENT_CHAR = '#'

    # Character separating name from email in file
    SEP_CHAR = ';'

    @classmethod
    def parse(cls, filename):
        """Parse a file containing Secret Santa participants.

        Arg:
            filename: Name of the containing participants. Each line must have
                      a participant name and their email, separated by the
                      SEP_CHAR defined in this class.

        Returns:
            A list if Person objects correspondent to each Person in the file.

        Raises:
            RuntimeError: Invalid line found while parsing file.
        """
        people = []

        with open(filename) as fd:
            for line in fd:
                # Remove comments and clean spaces
                clean_line = line.split(cls.COMMENT_CHAR)[0]
                clean_line = clean_line.strip()

                # Ignore empty lines
                if clean_line == '':
                    continue

                parts = clean_line.split(cls.SEP_CHAR)
                if len(parts) != 2:
                    raise RuntimeError('Invalid line in "%s":\n%s'
                                       % (filename, line))

                # Create and add Person to the list
                name = parts[0]
                email = parts[1]
                people.append(Person(name, email))

        return people
