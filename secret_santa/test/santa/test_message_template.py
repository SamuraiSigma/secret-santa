"""Automated tests for the MessageTemplate class."""

import unittest
from unittest.mock import Mock, patch, mock_open

from santa.message_template import MessageTemplate


class TestMessageTemplate(unittest.TestCase):
    """Tests the MessageTemplate class."""

    @patch('santa.message_template.warnings.warn')
    def test_init_empty_file(self, mock_warn):
        """Test the __init__() method with an empty file."""
        MessageTemplate('')
        self.assertTrue(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_init_only_person_pattern(self, mock_warn):
        """Test the __init__() method with person pattern only."""
        data = """Hi, $p. How are you? This $$ is a trick."""
        MessageTemplate(data)
        self.assertTrue(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_init_only_santa_pattern(self, mock_warn):
        """Test the __init__() method with santa pattern only."""
        data = """My secret santa is $s. And I like $."""
        MessageTemplate(data)
        self.assertTrue(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_init_regular(self, mock_warn):
        """Test the __init__() method with a regular file."""
        data = """Hi, $p! Your secret santa is $s. Look at these: $$"""
        MessageTemplate(data)
        self.assertFalse(mock_warn.called)

    @patch('santa.message_template.warnings.warn')
    def test_replace(self, mock_warn):
        """Test the replace() method."""
        red = Mock()
        red.name = 'Red'
        red.email = 'red@fire.com'

        blue = Mock()
        blue.name = 'Blue'
        blue.email = 'blue@water.com.uk'
        blue.santa = red

        data = """Hi, $p. You got $s. Roses are $$p, violets are $$, $$s."""
        answer = """Hi, Blue. You got Red. Roses are $p, violets are $, $s."""

        template = MessageTemplate(data)
        message = template.replace(blue)
        self.assertEqual(message, answer)
