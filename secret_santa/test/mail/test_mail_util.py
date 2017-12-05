"""Automated tests for the MailUtil class."""

import unittest
from mail.mail_util import MailUtil


class TestMailUtil(unittest.TestCase):
    """Tests the MailUtil class."""

    def test_is_valid_format_true(self):
        """Test the is_valid_format() method with valid email formats."""
        emails = [
            'foo@bar.com',
            'a@b.c',
            'red@blue.foobar.us',
            'red@blue.yellow.green'
        ]
        for email in emails:
            self.assertTrue(MailUtil.is_valid_format(email))

    def test_is_valid_format_false(self):
        """Test the is_valid_format() method with invalid email formats."""
        emails = [
            '',
            'abc',
            'foo@',
            '@bar',
            'foo@bar',
            'foo$bar.com.us',
            'foo@$bar.com'
        ]
        for email in emails:
            self.assertFalse(MailUtil.is_valid_format(email))
