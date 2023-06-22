import json
from flask import Flask, request, jsonify,render_template,send_file
import products_dao
from sql_connection import *

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    return render_template('manage.html',products=products)

@app.route('/addProduct', methods=['GET','POST'])
def add_product():
    if request.method == "POST":
        if request.form.get("gridRadios") == 'option1':
            x =1
        else: x=2
        product = {
        "name" : request.form.get("name"),
        "uom" : x,
        "price" : request.form.get("price")
        }
        products_dao.add_new_product(connection,product)
        return render_template('index.html')
    
@app.route('/deleteProduct', methods=['GET','POST'])
def del_product():
    pass

if __name__ == "__main__":
    print("starting python flask server")
    app.run(debug=True, port=5000)
    