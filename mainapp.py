from flask import Flask
import json

application = Flask(__name__)

filename = "users.json"

@application.route("/")
def index():
    return "Main Page"

@application.route("/users")
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

@application.route("/users/<username>")
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

# --------Main------------------
if __name__ == "__main__":
    app_json = {
            "duncan_long": {
                "id": "drekaner",
                "name": "Duncan Long",
                "favorite_color": "Blue"
            },
            "kelsea_head": {
                "id": "wagshark",
                "name": "Kelsea Head",
                "favorite_color": "Ping"
            },
            "phoenix_knox": {
                "id": "jikininer",
                "name": "Phoenix Knox",
                "favorite_color": "Green"
            },
            "adina_norton": {
                "id": "slimewagner",
                "name": "Adina Norton",
                "favorite_color": "Red"
            }
    }
    myfile = open(filename, mode='w', encoding='utf-8')
    json.dump(app_json, myfile)
    myfile.close()
    #application.run()
    application.run(host='0.0.0.0')
# ------------------------------
