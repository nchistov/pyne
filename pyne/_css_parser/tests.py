import unittest
from parser import parse


class ParserTestCase(unittest.TestCase):
    def test_parse_id(self):
        expected = {'p': {}}
        actual = parse('p {}')
        self.assertEqual(actual, expected)

    def test_parse_id_with_hash(self):
        expected = {'p': {'hash': '#main'}}
        actual = parse('#main p {}')
        self.assertEqual(actual, expected)
