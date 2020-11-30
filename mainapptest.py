from flask import Flask
from mainapp import *
import unittest
import json

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(usermain_page(), '"{test_user: { name: Test User, favorite_color: Black }}"')

    def test2(self):
        self.assertEqual(show_user_page("test_user"), '"{test_user: { id: test, name: Test User, favorite_color: Black }}"')

    def test3(self):
        self.assertEqual(show_user_page("test_user123"), "User doesn't exist")

# --------Main------------------
if __name__ == '__main__':
    test_json = {
        "test_user": {
            "id": "test",
            "name": "Test User",
            "favorite_color": "Black"
        }
    }
    #filename = "users.json"
    myfile = open(filename, mode='w', encoding='utf-8')
    json.dump(test_json, myfile)
    myfile.close()
    unittest.main()
# ------------------------------
