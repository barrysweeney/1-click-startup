from flask import Flask
from python_freeipa import ClientMeta

from nextcloud import NextCloud

NEXTCLOUD_URL = "http://localhost"

app = Flask(__name__)
client = ClientMeta('ipa.example.test')
client.login('admin', 'Secret123')


# Authentication


@app.route('/sign-up', methods=['POST'])
def sign_up():
    return 'Not yet implemented'


@app.route('/log-in', methods=['POST'])
def sign_up():
    return 'Not yet implemented'


# Manager and Employee Routes


@app.route('/checklist/update', methods=['post'])
def update_checklist():
    return 'Not yet implemented'


@app.route('/customer/order/new', methods=['post'])
def customer_order():
    return 'Not yet implemented'


@app.route('/stock/record', methods=['post'])
def record_stock():
    return 'Not yet implemented'


@app.route('/temperatures/record', methods=['post'])
def record_temperature():
    return 'Not yet implemented'


# Employee Exclusive Routes


@app.route('/manager/contact', methods=['post'])
def contact_manager():
    return 'Not yet implemented'


# Manager Exclusive Routes


@app.route('/supplier/contact', methods=['post'])
def contact_supplier():
    return 'Not yet implemented'


@app.route('/stock/order', methods=['post'])
def order_stock():
    return 'Not yet implemented'


@app.route('/employee/contact/<id>', methods=['post'])
def contact_employee(id):
    return 'Not yet implemented'


@app.route('/employee/contact/all', methods=['post'])
def contact_all_employees():
    return 'Not yet implemented'


@app.route('/sales/record/', methods=['post'])
def record_sales():
    return 'Not yet implemented'


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
