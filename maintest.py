import unittest
import json

test_json = {
    "test_user": {
        "id": "test",
        "name": "Test User",
        "favorite_color": "Black"
    }
}

filename = "users.json"

def usermain_page():
    myfile = open(filename, mode='r', encoding='utf-8')
    json_data = json.load(myfile)
    myfile.close()
    result = "{"
    i = 0
    for user in json_data:
        item = json_data[user]
        if i != 0:
            result = result + ", "
        i = 1
        result = result + str(user) + ": { name: " + str(item['name']) + "," + " favorite_color: " + str(item['favorite_color']) + " }"
    result = result + "}"
    return (json.dumps(result))


def show_user_page(username):
    myfile = open(filename, mode='r', encoding='utf-8')
    json_data = json.load(myfile)
    myfile.close()
    result = "{"
    for user in json_data:
        if user == username:
            item = json_data[user]
            result = result + str(user) + ": {"
            result = result + " id: " + str(item['id']) + ","
            result = result + " name: " + str(item['name']) + ","
            result = result + " favorite_color: " + str(item['favorite_color']) + " }"
    result = result + "}"
    if result == "{}":
        return "User doesn't exist"
    else:
        return (json.dumps(result))


class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(usermain_page(), '"{test_user: { name: Test User, favorite_color: Black }}"')

    def test2(self):
        self.assertEqual(show_user_page("test_user"), '"{test_user: { id: test, name: Test User, favorite_color: Black }}"')

    def test3(self):
        self.assertEqual(show_user_page("test_user123"), "User doesn't exist")


# --------Main------------------
if __name__ == '__main__':
    myfile = open(filename, mode='w', encoding='utf-8')
    json.dump(test_json, myfile)
    myfile.close()
    unittest.main()
# ------------------------------
