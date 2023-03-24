import requests
import unittest

def request_func():
    resp = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    if resp.status_code == 200:
        return resp.text, resp.json(), resp.encoding, resp.cookies
    return resp.status_code, resp.url, "error"
print(request_func())
#'{\n  "authenticated": true, \n  "user": "user"\n}\n', {'authenticated': True, 'user': 'user'}
class test_request_func(unittest.TestCase):

    def test_first_1(self):
        self.assertTrue(request_func(),'{\n  "authenticated": true, \n  "user": "user"\n}\n')

    def test_first_2(self):
        self.assertEqual(request_func(), {'authenticated': True, 'user': 'user'})

if __name__ == '__main__':
    unittest.main()


