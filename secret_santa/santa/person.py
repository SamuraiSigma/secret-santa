"""Contains the Person class."""

from mail.mail_util import MailUtil


class Person:
    """Represents a person participating in a Secret Santa event."""

    def __init__(self, name, email, santa=None):
        """Initialize a Person object with the given attributes.

        Args:
            name:  The person's name.
            email: The person's email address.
            santa: The person's secret santa (default: None).

        Raises:
            ValueError: Email with invalid format. Note: The email is
            not checked to see if it actually exists!
        """
        self._name = name
        if not MailUtil.is_valid_email(email):
            raise ValueError('"%s": email with invalid format!' % email)
        self._email = email
        self._santa = santa

    @property
    def name(self):
        """Return this person's name."""
        return self._name

    @property
    def email(self):
        """Return this person's email."""
        return self._email

    @property
    def santa(self):
        """Return this person's secret santa."""
        return self._santa

    @santa.setter
    def santa(self, santa):
        """Set this person's secret santa as the specified santa."""
        self._santa = santa

    def __repr__(self):
        """Show this person's name and email, along with their secret santa.

        Returns:
            String 'name (email) -> santa', using this person's attributes.
        """
        info = self.name + ' (' + self.email + ') -> '
        if self.santa is None:
            info += 'None'
        else:
            info += self.santa.name
        return info

    def __eq__(self, other):
        """Check if two Person objects have the same name and email.

        Arg:
            other: Person object that will be compared to this person.

        Returns:
            True if both objects have the same name and email, False otherwise.
        """
        # For safety, check if other is also a Person object
        return type(self) == type(other) and \
            self.name == other.name and self.email == other.email
