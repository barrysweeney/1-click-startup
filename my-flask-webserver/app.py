from flask import Flask
from python_freeipa import ClientMeta

from nextcloud import NextCloud

NEXTCLOUD_URL = "http://localhost"

app = Flask(__name__)
client = ClientMeta('ipa.example.test')
client.login('admin', 'Secret123')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/users/<id>")
def get_user(id):
    return 'Not yet implemented'


@app.route("/users/update/<id>")
def update_user(id):
    return 'Not yet implemented'


@app.route("/users/new/<uid>/<forename>/<surname>")
def create_user(uid, forename, surname):
    user = client.user_add(uid, forename, surname, forename + " " + surname, o_preferredlanguage='EN')
    return 'Not yet implemented'


@app.route("/users/delete/<id>")
def delete_user(id):
    return 'Not yet implemented'


if __name__ == '__main__':
    app.run()
