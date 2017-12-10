"""Automated tests for the CLI class."""

import unittest
from getopt import GetoptError

from view.cli.cli import CLI


class TestCLI(unittest.TestCase):
    """Tests the CLI class."""

    def test_init_empty_args(self):
        """Test the __init__() method with an empty argument list."""
        with self.assertRaises(ValueError):
            CLI([])

    def test_init_invalid_args(self):
        """Test the __init__() method with invalid arguments."""
        test_args = [
            ['-@!'],
            ['-p', 'oi', '--zzz'],
            ['-t', '"text"', '--helo'],
            ['-help']
        ]

        for args in test_args:
            with self.assertRaises(GetoptError):
                CLI(args)

    def test_init_undefined_args(self):
        """Test the __init__() method by not specifying necessary arguments."""
        test_args = [
            ['-t', '"some text"'],
            ['-p', 'foo.txt'],
            ['-m', 'bar.txt']
        ]

        for args in test_args:
            with self.assertRaises(ValueError):
                CLI(args)

    def test_init_regular(self):
        """Test the __init__() method in a regular situation."""
        cli = CLI(['-p', 'bar.txt', '-m', 'foo.txt'])
        self.assertEqual(cli._message_filename, 'foo.txt')
        self.assertEqual(cli._people_filename, 'bar.txt')
        self.assertEqual(cli._title, '')

        cli = CLI(['-m', 'm.txt', '-t', 'barfoo', '-p', 'p.txt'])
        self.assertEqual(cli._message_filename, 'm.txt')
        self.assertEqual(cli._people_filename, 'p.txt')
        self.assertEqual(cli._title, 'barfoo')
