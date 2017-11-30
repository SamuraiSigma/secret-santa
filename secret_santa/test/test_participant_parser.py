"""Automated tests for the ParticipantParser class."""

import os
import unittest

from santa.person import Person
from santa.participant_parser import ParticipantParser

# Directory with test files
CASE_DIR = os.path.dirname(__file__) + '/participant_parser_cases/'


class TestParticipantParser(unittest.TestCase):
    """Tests the ParticipantParser class."""

    def test_file_not_found(self):
        """Check for error when file is not found."""
        with self.assertRaises(FileNotFoundError):
            ParticipantParser.parse('')

    def test_empty_file(self):
        """An empty file (no data or comments)."""
        people = ParticipantParser.parse(CASE_DIR + 'empty.csv')
        self.assertEqual(people, [])

    def test_invalid_lines(self):
        """Error when a line has an invalid format."""
        with self.assertRaises(RuntimeError):
            ParticipantParser.parse(CASE_DIR + 'invalid_lines.csv')

    def test_regular_no_comments(self):
        """Regular file, without comments."""
        answer = []
        answer.append(Person("test", "t@test.com"))
        answer.append(Person("foo", "b@bar.com"))
        answer.append(Person("apple", "r@red.com"))
        answer.append(Person("banana", "y@yellow.com"))
        answer.append(Person("grape", "p@purple.com"))

        people = ParticipantParser.parse(CASE_DIR + 'regular.csv')
        self.assertEqual(people, answer)

    def test_scattered_spaces(self):
        """Lines may contain spaces before and after data."""
        answer = []
        answer.append(Person("test", "t@test.com"))
        answer.append(Person("foo", "b@bar.com"))
        answer.append(Person("apple", "r@red.com"))
        answer.append(Person("banana", "y@yellow.com"))

        people = ParticipantParser.parse(CASE_DIR + 'scattered_spaces.csv')
        self.assertEqual(people, answer)

    def test_skip_lines(self):
        """File with empty lines mixed in with valid lines."""
        answer = []
        answer.append(Person("foo", "b@bar.com"))
        answer.append(Person("banana", "y@yellow.com"))

        people = ParticipantParser.parse(CASE_DIR + 'skip_lines.csv')
        self.assertEqual(people, answer)

    def test_file_only_comments(self):
        """File that only contains comments."""
        people = ParticipantParser.parse(CASE_DIR + 'only_comments.csv')
        self.assertEqual(people, [])

    def test_data_and_comments(self):
        """File with data and comments (beginning and middle of lines)."""
        answer = []
        answer.append(Person("test", "t@test.com"))
        answer.append(Person("foo", "b@bar.com"))
        answer.append(Person("apple", "r@red.com"))
        answer.append(Person("grape", "p@purple.com"))
        answer.append(Person("pear", "g@green.com"))

        people = ParticipantParser.parse(CASE_DIR + 'data_and_comments.csv')
        self.assertEqual(people, answer)
