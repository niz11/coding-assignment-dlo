import unittest
import urllib.parse
from unittest.mock import patch
from dlo.dlo_url_generator import generate_dlo_url

class TestGenerateURL(unittest.TestCase):
    def setUp(self):
        self.userid = "1"
        self.usertype = "careprovider"
        self.secret = "secret"
        self.base_url = "https://ca-darejano.minddistrict.dev/"
        self.redirecturl = None

    def test_generate_dlo_url_with_valid_inputs(self):
        actual_url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url)

        self.assertTrue(actual_url.startswith(self.base_url))
        self.assertTrue("userid=1" in actual_url)
        self.assertTrue("usertype=careprovider" in actual_url)
        self.assertTrue("nonce=" in actual_url)
        self.assertTrue("timestamp=" in actual_url)
        self.assertTrue("token=" in actual_url)
        self.assertNotIn("redirect=", actual_url)

    def test_generate_dlo_url_with_invalid_usertype_raises_error(self):
        invalid_usertype = "invalid"
        with self.assertRaises(ValueError):
            generate_dlo_url(self.userid, invalid_usertype, self.secret, self.base_url)

    def test_generate_dlo_url_with_invalid_userid_raises_error(self):
        invalid_userid = ""
        with self.assertRaises(ValueError):
            generate_dlo_url(invalid_userid, self.usertype, self.secret, self.base_url)
    
    def test_generate_dlo_url_with_redirect_url(self):
        redirect_url = "https://google.com"
        actual_url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url, None, redirect_url)
        url_encoded_redirect = urllib.parse.quote(redirect_url, safe='')
        self.assertIn(f"redirect={url_encoded_redirect}", actual_url)
    
    def test_generate_dlo_url_with_path(self):
        path = "/c/"
        actual_url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url, path)
        self.assertTrue(actual_url.startswith(self.base_url + path[1:] + "?"))
        path = "c/"
        actual_url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url, path)
        self.assertTrue(actual_url.startswith(self.base_url + path + "?"))
        path = "c"
        actual_url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url, path)
        self.assertTrue(actual_url.startswith(self.base_url + path + "?"))
        path = '/c/@@allclients'
        actual_url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url, path)
        self.assertTrue(actual_url.startswith(self.base_url + path[1:] + "?"))
    

    def test_generate_dlo_url_nonce(self):
        nonces = []
        for _ in range(100):
            url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url)
            nonce = url.split('nonce=')[1].split('&')[0]
            if nonce in nonces:
                self.fail("Duplicate nonces generated")
            nonces.append(nonce)
        assert True

    @patch('dlo.dlo_url_generator.generate_signature', return_value='dummy_token')
    def test_token_generation(self, mock_sign):
        actual_url = generate_dlo_url(self.userid, self.usertype, self.secret, self.base_url)
        self.assertIn('token=dummy_token', actual_url)

if __name__ == '__main__':
    unittest.main()