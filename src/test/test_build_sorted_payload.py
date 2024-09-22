import unittest
from dlo.dlo_url_generator import build_sorted_payload

class TestBuildSortedPayload(unittest.TestCase):
    def test_empty_payload(self):
        payload = {}
        expected = ''
        result = build_sorted_payload(payload)
        self.assertEqual(result, expected)

    def test_single_key_payload(self):
        payload = {'key': 'value'}
        expected = 'keyvalue'
        result = build_sorted_payload(payload)
        print(result)
        self.assertEqual(result, expected)

    def test_multiple_keys_payload(self):
        payload = {'b': '2', 'a': '1', 'c': '3'}
        expected = 'a1b2c3'
        result = build_sorted_payload(payload)
        self.assertEqual(result, expected)

    def test_numeric_keys_payload(self):
        payload = {1: 'one', 3: 'three', 2: 'two'}
        expected = '1one2two3three'
        result = build_sorted_payload(payload)
        self.assertEqual(result, expected)

    def test_mixed_keys_payload(self):
        payload = {'a': '1', '2': 'two', 'b': '3'}
        expected = '2twoa1b3'
        result = build_sorted_payload(payload)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()