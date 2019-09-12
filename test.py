from app import app
import unittest

class FlaskAppTest(unittest.TestCase):
    def test_index(self):
        client = app.test_client(self)
        response = client.get('/',content_type='html/text')
        self.assertEqual(response.status_code,200)    
    
    def test_index_data(self):
        client = app.test_client(self)
        response = client.get('/',content_type='html/text')
        self.assertTrue(b'DevLync' in response.data)

if __name__ == '__main__':
    unittest.main()
