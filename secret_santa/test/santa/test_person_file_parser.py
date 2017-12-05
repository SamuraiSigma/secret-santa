"""Automated tests for the PersonFileParser class."""

import unittest
from unittest.mock import patch
from io import StringIO

from santa.person_file_parser import PersonFileParser


class TestPersonFileParser(unittest.TestCase):
    """Tests the PersonFileParser class."""

    def __mock_person_constructor(self, name, email):
        """Mock used when calling Person().

        Args:
            name:  Name of the mocked Person.
            email: Email of the mocked Person.

        Return: A list containing the arguments.
        """
        return [name, email]

    @patch('santa.person_file_parser.Person')
    def __patch_and_check(self, data, answer, mock_person):
        """Patch Person and check if parsed values are equal to expected.

        Args:
            data:        Data to be used in mock file.
            answer:      Expected answer when parsing mocked file.
            mock_person: Patch for Person objects.
        """
        mock_person.side_effect = self.__mock_person_constructor
        with patch('builtins.open', return_value=StringIO(data)) as mock_file:
            people = PersonFileParser.parse(mock_file)
            self.assertEqual(people, answer)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_open):
        """Check for error when file is not found.

        Arg:
            mock_open: Patch that raises FileNotFoundError when opening file.
        """
        with self.assertRaises(FileNotFoundError):
            PersonFileParser.parse(mock_open)

    def test_empty_file(self):
        """An empty file (no data or comments)."""
        self.__patch_and_check('', [])

    def test_invalid_lines(self):
        """Error when a line has an invalid format."""
        data = """test|t@test.com
        gandalf|you@shallnotpass.com"""
        with patch('builtins.open', return_value=StringIO(data)) as mock_file:
            with self.assertRaises(RuntimeError):
                PersonFileParser.parse(mock_file)

    def test_regular_no_comments(self):
        """Regular file, without comments."""
        data = """red;r@rgb.com
        green;g@rgb.com
        blue;b@rgb.com"""

        answer = [
            ['red', 'r@rgb.com'],
            ['green', 'g@rgb.com'],
            ['blue', 'b@rgb.com']
        ]

        self.__patch_and_check(data, answer)

    def test_scattered_spaces(self):
        """Lines may contain spaces before and after data."""
        data = """   apple;ap@apple.com
         pear; pe@pear.com
        grape  ;  gr@grape.com
            banana;ba@banana.com   """

        answer = [
            ['apple', 'ap@apple.com'],
            ['pear', 'pe@pear.com'],
            ['grape', 'gr@grape.com'],
            ['banana', 'ba@banana.com']
        ]

        self.__patch_and_check(data, answer)

    def test_skip_lines(self):
        """File with empty lines mixed in with valid lines."""
        data = """

        foo;foo@foo.com.foo


        bar;bar@bar.com.bar

        """

        answer = [
            ['foo', 'foo@foo.com.foo'],
            ['bar', 'bar@bar.com.bar']
        ]

        self.__patch_and_check(data, answer)

    def test_only_comments(self):
        """File that only contains commnets."""
        data = """# What a wonderful day to find bugs
            # Until next time!"""
        self.__patch_and_check(data, [])

    def test_data_and_comments(self):
        """File with data and comments (beginning and middle of lines)."""
        data = """# Hello!
        red;red@r.com.uk
        blue;blue@b.com  # Shall we try breaking the code?
        # How about here?
        green;green@g.com.us
        # This guy shouldn't be read: banana;@yellow.com
        yellow;yellow@y.com.jp
        white;white@w.com.br # .com... Hehehehehe!
        # The end"""

        answer = [
            ['red', 'red@r.com.uk'],
            ['blue', 'blue@b.com'],
            ['green', 'green@g.com.us'],
            ['yellow', 'yellow@y.com.jp'],
            ['white', 'white@w.com.br']
        ]

        self.__patch_and_check(data, answer)
