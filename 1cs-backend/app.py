import json
import time
from flask import Flask, request, Response, session
import mysql.connector
from passlib.hash import sha256_crypt
from flask_cors import CORS, cross_origin

from python_freeipa import ClientMeta

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# client = ClientMeta('ipa.example.test')
# client.login('admin', 'Secret123')

# @app.route('/widgets')
# def get_widgets():
#     mydb = mysql.connector.connect(
#         host="mysqldb",
#         user="root",
#         password="p@ssw0rd1",
#         database="inventory"
#     )
#     cursor = mydb.cursor()
#     cursor.execute("SELECT * FROM widgets")
#
#     row_headers = [x[0] for x in cursor.description]
#     results = cursor.fetchall()
#
#     json_data = []
#
#     for result in results:
#         json_data.append(dict(zip(row_headers, result)))
#
#     cursor.close()
#
#     return json.dumps(json_data)

# wait for MYSQL container to be ready

ready = False
while not ready:
    try:
        mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1"
        )
        cursor = mydb.cursor()
        cursor.execute("DROP DATABASE IF EXISTS startup")
        cursor.execute("CREATE DATABASE startup")
        cursor.execute("USE startup")
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute(
            "CREATE TABLE users (id int(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255) UNIQUE , password VARCHAR(255), role VARCHAR(255), business VARCHAR(255), can_log_in BOOLEAN)")
        cursor.close()
        mydb.close()
        ready = True
    except mysql.connector.errors.InterfaceError:
        continue


# Authentication

@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    # get values from json request body
    data = request.json
    name = data['name']
    email = data['email']
    password = sha256_crypt.encrypt(data['password'])
    role = data['role']
    business = data['business']
    can_log_in = False

    if role == "manager":
        can_log_in = True

    # connect to db
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="startup"
    )

    # create cursor
    cursor = mydb.cursor()

    # execute query
    cursor.execute(
        "INSERT INTO users(name, email, password, role, business, can_log_in) VALUES(%s, %s, %s, %s, %s, %s)",
        (name, email, password, role, business, can_log_in))

    # commit data to db
    mydb.commit()

    # close connection
    cursor.close()
    mydb.close()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/login', methods=['POST'])
@cross_origin()
def log_in():
    # get values from json request body
    data = request.json
    email = data['email']
    password_candidate = data['password']

    # connect to db
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="startup"
    )

    # create cursor
    cursor = mydb.cursor(dictionary=True)

    # get user by email
    result = cursor.execute("SELECT * FROM users where email = %s", [email])
    # return cursor.fetchone()

    try:
        # get stored hash
        result_data = cursor.fetchone()
        password = result_data['password']

        # compare passwords
        if sha256_crypt.verify(password_candidate, password):
            # password matched
            session['logged_in'] = True
            session['name'] = result_data['name']
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        else:
            raise Exception

    except Exception as Ex:
        error = "Email not found"
        return json.dumps({'success': False}), 404, {'ContentType': 'application/json'}

    return 'Not yet implemented'


# Manager and Employee Routes

@app.route('/checklist', )
def get_checklist():
    return 'Not yet implemented'


@app.route('/checklist/update', methods=['post'])
def update_checklist():
    return 'Not yet implemented'


@app.route('/customer/order/new', methods=['post'])
def customer_order():
    name = request.form['customer-name']
    contact_number = request.form['customer-contact-number']
    order = request.form['customer-order']
    # c.execute("INSERT INTO CUSTOMER_ORDER(CUSTOMER_NAME,CONTACT_NUMBER,CUSTOMER_ORDER) \
    #  VALUES (?,?,?)", (name, contact_number, order,))
    # conn.commit()
    return 'OK'


@app.route('/customer/orders/')
def get_customer_orders():
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
def update_employee(id):
    return 'Not yet implemented'


@app.route("/employee/new", methods=['post'])
def add_employee():
    uid = "-1"
    forename = "John"
    surname = "Doe"
    # FreeIPA Interaction
    # user = client.user_add(uid, forename, surname, forename + " " + surname, o_preferredlanguage='EN')
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
