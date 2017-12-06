"""Automated tests for the Matchmaker class."""

import unittest
from unittest.mock import Mock

from santa.matchmaker import Matchmaker


class TestMatchmaker(unittest.TestCase):
    """Tests the Matchmaker class."""

    def test_match_zero_person(self):
        """Test the match() method with a list of zero Person objects."""
        matchmaker = Matchmaker()

        with self.assertRaises(ValueError):
            matchmaker.match([])

    def test_match_one_person(self):
        """Test the match() method with a list of one Person object."""
        matchmaker = Matchmaker()

        with self.assertRaises(ValueError):
            matchmaker.match([Mock('Lonely', 'forever@alone.com')])

    def test_match_two_person(self):
        """Test the match() method with a list of two Person objects."""
        red = Mock()
        red.name = 'Red'
        red.email = 'red@red.com'

        blue = Mock()
        blue.name = 'Blue'
        blue.email = 'blue@blue.com'

        matchmaker = Matchmaker()
        matchmaker.match([red, blue])
        assert red.santa is blue
        assert blue.santa is red

    def test_match_typical(self):
        """Test the match() method in a typical condition."""
        matchmaker = Matchmaker()

        # Test many times, checking if each case produced a derangement
        for i in range(200):
            people = []
            for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                person = Mock()
                person.name = c
                person.email = c + '@com.com'
                people.append(person)

            matchmaker.match(people)
            for person in people:
                assert person.santa is not person
