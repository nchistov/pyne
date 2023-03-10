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

    def test_parse_number_value(self):
        expected = {'p': {'value': {'color': 0}}}
        actual = parse('p { color: 0 }')
        self.assertEqual(actual, expected)

    def test_parse_named_value(self):
        expected = {'p': {'value': {'margin': '50px'}}}
        actual = parse('p { margin: 50px }')
        self.assertEqual(actual, expected)

    def test_parse_tuple_value(self):
        expected = {'p': {'value': {'color': [0, 0, 0]}}}
        actual = parse('p { color: (0, 0, 0) }')
        self.assertEqual(actual, expected)

    def test_parse_list_value(self):
        expected = {'p': {'value': {'color': [0, 0, 0]}}}
        actual = parse('p { color: [0, 0, 0] }')
        self.assertEqual(actual, expected)

    def test_parse_dict_value(self):
        expected = {'p': {'value': {'color': {'red': 0, 'green': 0, 'blue': 0}}}}
        actual = parse("p { color: {'red': 0, 'green': 0, 'blue': 0} }")
        self.assertEqual(actual, expected)
