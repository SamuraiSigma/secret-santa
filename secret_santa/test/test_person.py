"""Automated tests for the Person class."""

import unittest
from unittest.mock import patch

from santa.person import Person


class TestPerson(unittest.TestCase):
    """Tests the Person class."""

    @patch('santa.person.MailUtil.is_valid_email', return_value=True)
    def test_init(self, mock_mail_util):
        """Test the __init__() method.

        Arg:
            mock_mail_util: MailUtil.is_valid_email() patch returning True.
        """
        foobar = Person('Foobar', 'foo@bar.com')
        self.assertEqual(foobar.name, 'Foobar')
        self.assertEqual(foobar.email, 'foo@bar.com')
        self.assertIsNone(foobar.santa)

        bob = Person('Bob', 'happy@bob.com.us', foobar)
        self.assertEqual(bob.name, 'Bob')
        self.assertEqual(bob.email, 'happy@bob.com.us')
        self.assertEqual(bob.santa, foobar)

    @patch('santa.person.MailUtil.is_valid_email', return_value=False)
    def test_invalid_email_init(self, mock_mail_util):
        """Test the __init__() method assuming an invalid email is used.

        Arg:
            mock_mail_util: MailUtil.is_valid_email() patch returning False.
        """
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', '')
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', 'foo@')
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', '@bar.com.uk')
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', 'foo$@bar.com')

    @patch('santa.person.MailUtil.is_valid_email', return_value=True)
    def test_set_santa(self, mock_mail_util):
        """Test the santa setter method.

        Arg:
            mock_mail_util: MailUtil.is_valid_email() patch returning True.
        """
        alice = Person('Alice', 'alice@123.com')
        bob = Person('Bob', 'bob@321.com.us')
        carl = Person('Carl', 'carl@213.com.uk', alice)

        alice.santa = bob
        self.assertEqual(alice.santa, bob)
        self.assertIsNone(bob.santa)

        bob.santa = alice
        self.assertEqual(alice.santa, bob)
        self.assertEqual(bob.santa, alice)

        carl.santa = bob
        self.assertEqual(carl.santa, bob)
        self.assertEqual(bob.santa, alice)
