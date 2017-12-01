"""Contains the MailUtil class."""

import re


class MailUtil:
    """Contains email-related utility methods."""

    # Regex for a valid email format (according to RFC 5322)
    EMAIL_RE = re.compile('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

    @classmethod
    def is_valid_email(cls, email):
        """Check if the given email has a valid format.

        Arg:
            email: Email address whose format will be validated.

        Returns:
            True if the email has a valid format, or False otherwise.
        """
        return re.fullmatch(cls.EMAIL_RE, email) is not None
