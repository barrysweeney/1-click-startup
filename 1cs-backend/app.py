import json
import time
from flask import Flask, request, Response, session
import mysql.connector
from passlib.hash import sha256_crypt
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# enable CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# wait for MYSQL container to be ready for connection before allowing requests to database

ready = False
while not ready:
    try:
        # connect to db with parameters matching docker-compose.yaml file
        mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1"
        )
        # create cursor
        cursor = mydb.cursor()
        # create and use database "startup" if it doesn't exist
        # todo: implement persistent database storage with volume mounting
        cursor.execute("CREATE DATABASE startup IF NOT EXISTS ")
        cursor.execute("USE startup")
        # create "users" table if it doesn't exist
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id int(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255) UNIQUE , password VARCHAR(255), role VARCHAR(255), business VARCHAR(255), can_log_in BOOLEAN)")
        # close connection
        cursor.close()
        mydb.close()
        # break out of while loop by setting ready to True
        ready = True
    except mysql.connector.errors.InterfaceError:
        # try to connect again
        continue


# Authentication

# User registration route
@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    # get values from json request body
    data = request.json
    name = data['name']
    email = data['email']
    role = data['role']
    business = data['business']
    # encrypt plain text password
    password = sha256_crypt.encrypt(data['password'])
    # employees can't log in until manager approves
    can_log_in = False
    # managers can log in immediately
    if role == "manager":
        can_log_in = True

    # connect to db with parameters matching docker-compose.yaml file
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="startup"
    )

    # create cursor
    cursor = mydb.cursor()

    # execute query to add user to database users table
    cursor.execute(
        "INSERT INTO users(name, email, password, role, business, can_log_in) VALUES(%s, %s, %s, %s, %s, %s)",
        (name, email, password, role, business, can_log_in))

    # commit data to db
    mydb.commit()

    # close connection
    cursor.close()
    mydb.close()

    # return success message
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


# User login route
@app.route('/login', methods=['POST'])
@cross_origin()
def log_in():
    # get values from json request body
    data = request.json
    email = data['email']
    password_candidate = data['password']

    # connect to db with parameters matching docker-compose.yaml file
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

    try:
        # get stored user with matching email
        result_data = cursor.fetchone()
        # get stored hashed password
        password = result_data['password']

        # compare password user entered with stored hashed password
        if sha256_crypt.verify(password_candidate, password):
            # return success message if passwords match
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        else:
            # otherwise raise an Exception
            raise Exception

    # catch Exception if error with finding user with the entered email or if passwords don't match
    except Exception as Ex:
        error = "User with the email and password combination not found"
        return json.dumps({'success': False, 'error': error}), 404, {'ContentType': 'application/json'}


# Manager and Employee Routes


# Get checklist items from the database since the manager will be able to edit these by adding or removing tasks
@app.route('/checklist')
def get_checklist():
    return 'Not yet implemented'


# Update the checklist when a checkbox has been checked or unchecked
@app.route('/checklist/update', methods=['post'])
def update_checklist():
    return 'Not yet implemented'


# store new customer order in the database
@app.route('/customer/order/new', methods=['post'])
def customer_order():
    # get form values from request
    name = request.form['customer-name']
    contact_number = request.form['customer-contact-number']
    order = request.form['customer-order']
    # insert values from form into new record in CUSTOMER_ORDER table
    c.execute("INSERT INTO CUSTOMER_ORDER(CUSTOMER_NAME,CONTACT_NUMBER,CUSTOMER_ORDER) \
     VALUES (?,?,?)", (name, contact_number, order,))
    # commit changes to the database
    conn.commit()
    # return success message
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


# get all customer orders from the database
@app.route('/customer/orders/')
def get_customer_orders():
    return 'Not yet implemented'


# record current stock levels by saving them to the database with a timestamp
@app.route('/stock/record', methods=['post'])
def record_stock():
    return 'Not yet implemented'


# record current temperature levels by saving them to the database with a timestamp
@app.route('/temperatures/record', methods=['post'])
def record_temperature():
    return 'Not yet implemented'


# contact employee via email using their ID and
@app.route('/employee/contact/<id>', methods=['post'])
def contact_employee(id):
    return 'Not yet implemented'


# Employee Exclusive Routes

# contact manager via email
# todo: consider using ids here as well since there could be more than 1 manager
@app.route('/manager/contact', methods=['post'])
def contact_manager():
    return 'Not yet implemented'


# Manager Exclusive Routes

# contact supplier via email using their id
@app.route('/supplier/contact/<id>', methods=['post'])
def contact_supplier(id):
    return 'Not yet implemented'


# update supplier details, storing them in the database
@app.route('/supplier/update', methods=['post'])
def update_supplier():
    return 'Not yet implemented'


# store details of a new supplier in the database
@app.route('/supplier/new', methods=['post'])
def add_new_supplier():
    return 'Not yet implemented'


# delete a supplier from the database
# todo: consider data protection act and archiving here
@app.route('/supplier/delete', methods=['post'])
def delete_supplier():
    return 'Not yet implemented'


# order stock
# todo: consider changing this route since you could contact individual supplier for each stock item
@app.route('/stock/order', methods=['post'])
def order_stock():
    return 'Not yet implemented'


# contact all employees via email to send them the same message
@app.route('/employee/contact/all', methods=['post'])
def contact_all_employees():
    return 'Not yet implemented'


# record sales for the day, and store them with a timestamp to the database
@app.route('/sales/record', methods=['post'])
def record_sales():
    return 'Not yet implemented'


# get an employees details from the database using their id
@app.route("/employee/<id>")
def get_employee(id):
    return 'Not yet implemented'


# update an employees details using their id, storing updated details in the database
@app.route("/employee/update/<id>", methods=['post'])
def update_employee(id):
    return 'Not yet implemented'


# add a new employees details to the database
@app.route("/employee/new", methods=['post'])
def add_employee():
    return 'Not yet implemented'


# delete an employee from the database
# todo: consider data protection act and archiving here
@app.route("/employee/delete/<id>")
def delete_employee(id):
    return 'Not yet implemented'


# pay employee by id
@app.route('/employee/pay/<id>')
def pay_employee(id):
    return 'Not yet implemented'


# pay all employees
@app.route('/employee/pay/all')
def pay_all_employees():
    return 'Not yet implemented'


# add task to daily checklist (eg: clean microwave)
@app.route('/checklist/add', methods=['post'])
def add_to_checklist():
    return 'Not yet implemented'


# remove task from daily checklist
@app.route('/checklist/remove')
def remove_from_checklist():
    return 'Not yet implemented'


# get dashboard information such as sales, profits, growth etc
@app.route("/dashboard")
def get_dashboard(id):
    return 'Not yet implemented'


if __name__ == '__main__':
    app.run()
