import unittest
import requests
def post_request_fun():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    if r.status_code == 200:
        return r.json(), r.encoding, r.content, r.cookies
    return r.status_code, r.text, "error"
print(post_request_fun())

class test_post_request_case(unittest.TestCase):

    def test_post_json_method(self):
        self.assertTrue(post_request_fun())

    def test_post_encoding_method(self):
        self.assertTrue(post_request_fun(),'utf-8')

    def test_post_content_method(self):
        self.assertTrue(post_request_fun(), b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "key1": "value1", \n    "key2": "value2"\n  }, \n  "headers": {\n    "Accept": "*/*", \n  "Accept-Encoding": "gzip, deflate", \n    "Content-Length": "23", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.28.2", \n    "X-Amzn-Trace-Id": "Root=1-641d7ff7-3da08e7243b892d22819f2de"\n  }, \n  "json": null, \n  "origin": "43.230.42.192", \n  "url": "http://httpbin.org/post"\n}\n')

    def test_post_cookies_method(self):
        self.assertTrue(post_request_fun(),'<RequestsCookieJar[]>')

if __name__ == '__main__':
    unittest.main()