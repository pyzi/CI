# This is the script for our test

import unittest

class ForVideo(unittest.TestCase):
    def setUp(self):
        print("some text")
    def tearDown(self):
        print("some text")
    def test_ola(self):
        self.assert 'ola', 'tudo'
    
if __name__=="__main__":
    unittest.main()

