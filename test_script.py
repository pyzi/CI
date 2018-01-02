# This is the script for our test

import unittest

class ForVideo(unittest.TestCase):
    def setUp(self):
        print("some text")
    def tearDown(self):
        print("some text")
    
if __name__=="__main__":
    unittest.main()

