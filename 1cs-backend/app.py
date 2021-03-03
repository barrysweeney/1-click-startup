from flask import Flask
from python_freeipa import ClientMeta

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

@app.route('/checklist',)
def get_checklist():
    return 'Not yet implemented'


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


# TODO: integrate email service
@app.route('/employee/contact/<id>', methods=['post'])
def contact_employee(id):
    return 'Not yet implemented'


# Employee Exclusive Routes

# TODO: integrate email service
@app.route('/manager/contact', methods=['post'])
def contact_manager():
    return 'Not yet implemented'


# Manager Exclusive Routes


# TODO: integrate email service
@app.route('/supplier/contact', methods=['post'])
def contact_supplier():
    return 'Not yet implemented'


@app.route('/supplier/update', methods=['post'])
def update_supplier():
    return 'Not yet implemented'


@app.route('/supplier/new', methods=['post'])
def add_new_supplier():
    return 'Not yet implemented'


@app.route('/supplier/delete', methods=['post'])
def delete_supplier():
    return 'Not yet implemented'


@app.route('/stock/order', methods=['post'])
def order_stock():
    return 'Not yet implemented'


# TODO: integrate email service
@app.route('/employee/contact/all', methods=['post'])
def contact_all_employees():
    return 'Not yet implemented'


@app.route('/sales/record', methods=['post'])
def record_sales():
    return 'Not yet implemented'


@app.route("/employee/<id>")
def get_employee(id):
    return 'Not yet implemented'


@app.route("/employee/update/<id>", methods=['post'])
def update_user(id):
    return 'Not yet implemented'


@app.route("/employee/new", methods=['post'])
def update_user():
    uid = "-1"
    forename = "John"
    surname = "Doe"
    # FreeIPA Interaction
    user = client.user_add(uid, forename, surname, forename + " " + surname, o_preferredlanguage='EN')
    return 'Not yet implemented'


@app.route("/employee/delete/<id>")
def delete_employee(id):
    return 'Not yet implemented'


@app.route('/employee/pay/<id>')
def pay_employee(id):
    return 'Not yet implemented'


@app.route('/employee/pay/all')
def pay_all_employees():
    return 'Not yet implemented'


@app.route('/checklist/add', methods=['post'])
def add_to_checklist():
    return 'Not yet implemented'


@app.route('/checklist/remove')
def remove_from_checklist():
    return 'Not yet implemented'


@app.route("/dashboard")
def get_dashboard(id):
    # interacts with process mining application to provide information to the managers frontend dashboard
    return 'Not yet implemented'


if __name__ == '__main__':
    app.run()
