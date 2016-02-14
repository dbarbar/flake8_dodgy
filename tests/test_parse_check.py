from unittest import TestCase
from flake8_dodgy.flake8_dodgy import parse_check


class TestParseCheck(TestCase):
    def test_parse_check(self):
        input_check = (
            'the_key',
            'the_message',
            ('regexp1', 'regexp2'),
            any
        )

        actual = parse_check(input_check)

        expected_check = {
            'key': 'the_key',
            'message': 'the_message',
            'regexps': ('regexp1', 'regexp2'),
            'condition': any
        }

        self.assertDictEqual(actual, expected_check)
