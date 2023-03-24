import requests
import unittest
def request_func():
    new_data = {
    "userID": 1,
    "id": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."}
    resp = requests.post("https://jsonplaceholder.typicode.com/posts",params = new_data)
    if resp.status_code == 201:
        return resp.json(), resp.ok, resp.text, resp.encoding
    return resp.status_code
print(request_func())

class test_post_request_case(unittest.TestCase):

    def test_post_json_method(self):
        self.assertTrue(request_func(), {'id': 101})

    def test_post_ok_method(self):
        self.assertTrue(request_func(), True)

    def test_post_text_method(self):
        self.assertEqual(request_func(), '{\n  "id": 101\n}')

    def test_post_encoding_method(self):
        self.assertEqual(request_func(), 'utf-8')



if __name__ == '__main__':
    unittest.main()

