from dlo.dlo_url_generator import generate_dlo_url
import unittest
# python3 -m unittest discover -s test -p "test_*.py"
userid = "1"
usertype = "careprovider"
secret = "secret"
base_url = "https://ca-darejano.minddistrict.dev/"
redirecturl = None

class TestGenerateURL(unittest.TestCase):
    def test_generate_dlo_url_with_valid_inputs(self):
        actual_url = generate_dlo_url(userid, usertype, secret, base_url, redirecturl)

        self.assertTrue(actual_url.startswith("https://ca-darejano.minddistrict.dev/"))
        self.assertTrue("userid=1" in actual_url)
        self.assertTrue("usertype=careprovider" in actual_url)
        self.assertTrue("nonce=" in actual_url)
        self.assertTrue("timestamp=" in actual_url)
        self.assertTrue("token=" in actual_url)

    def test_generate_dlo_url_with_invalid_usertype(self):
        usertype = "invalid"

        with self.assertRaises(ValueError):
            generate_dlo_url(userid, usertype, secret, base_url, redirecturl)

    def test_generate_dlo_url_with_invalid_userid(self):
        userid = ""

        with self.assertRaises(ValueError):
            generate_dlo_url(userid, usertype, secret, base_url, redirecturl)

if __name__ == '__main__':
    unittest.main()