"""Automated tests for the MessageTemplate class."""

import unittest
from unittest.mock import Mock, patch, mock_open

from santa.message_template import MessageTemplate


class TestMessageTemplate(unittest.TestCase):
    """Tests the MessageTemplate class."""

    @patch('santa.message_template.warnings.warn')
    def test_init_empty_file(self, mock_warn):
        """Test the __init__() method with an empty file."""
        with patch('builtins.open', mock_open(read_data='')) as mock_file:
            MessageTemplate(mock_file)
            self.assertTrue(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_init_only_person_pattern(self, mock_warn):
        """Test the __init__() method with person pattern only."""
        data = """Hi, \p. How are you? This \\\\ is a trick."""
        with patch('builtins.open', mock_open(read_data=data)) as mock_file:
            MessageTemplate(mock_file)
            self.assertTrue(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_init_only_santa_pattern(self, mock_warn):
        """Test the __init__() method with santa pattern only."""
        data = """My secret santa is \s. And I like backslashes: \\."""
        with patch('builtins.open', mock_open(read_data=data)) as mock_file:
            MessageTemplate(mock_file)
            self.assertTrue(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_init_regular(self, mock_warn):
        """Test the __init__() method with a regular file."""
        data = """Hi, \p! Your secret santa is \s. Backslash FTW \\\\!"""
        with patch('builtins.open', mock_open(read_data=data)) as mock_file:
            MessageTemplate(mock_file)
            self.assertFalse(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_replace(self, mock_warn):
        """Test the replace() method."""
        red = Mock()
        red.name = 'Red'
        red.email= 'red@fire.com'

        blue = Mock()
        blue.name= 'Blue'
        blue.email= 'blue@water.com.uk'
        blue.santa = red

        data = """Hi, \p. You got \s. \\\\ bla bla."""
        answer = """Hi, Blue. You got Red. \\ bla bla."""

        with patch('builtins.open', mock_open(read_data=data)) as mock_file:
            template = MessageTemplate(mock_file)
            message = template.replace(blue)
            self.assertEqual(message, answer)
