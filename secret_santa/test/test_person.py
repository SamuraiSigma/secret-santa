"""Automated tests for the Person class."""

import unittest
from santa.person import Person


class TestPerson(unittest.TestCase):
    """Tests the Person class."""

    def test_init(self):
        """Test the __init__() method."""
        foobar = Person('Foobar', 'foo@bar.com')
        self.assertEqual(foobar.name, 'Foobar')
        self.assertEqual(foobar.email, 'foo@bar.com')
        self.assertIsNone(foobar.santa)

        bob = Person('Bob', 'happy@bob.com.us', foobar)
        self.assertEqual(bob.name, 'Bob')
        self.assertEqual(bob.email, 'happy@bob.com.us')
        self.assertEqual(bob.santa, foobar)

    def test_invalid_email_init(self):
        """Test the __init__() method with an invalid email argument."""
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', '')
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', 'foo@')
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', '@bar.com.uk')
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', 'foo$@bar.com')
        with self.assertRaises(ValueError):
            foobar = Person('Foobar', 'foo@&()bar.com.us')

    def test_set_santa(self):
        """Test the santa setter method."""
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
