import unittest
from parser import parse


class ParserTestCase(unittest.TestCase):
    def test_parse_id(self):
        expected = {'p': {'value': {}}}
        actual = parse('p {}')
        self.assertEqual(actual, expected)

    def test_parse_id_with_hash(self):
        expected = {'p': {'hash': '#main', 'value': {}}}
        actual = parse('#main p {}')
        self.assertEqual(actual, expected)

    def test_parse_value(self):
        expected = {'p': {'value': {'color': '(0, 0, 0)'}}}
        actual = parse('p { color: (0, 0, 0) }')
        self.assertEqual(actual, expected)
