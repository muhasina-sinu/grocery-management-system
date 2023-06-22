from sql_connection import *

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select product_id,name,uom,price,uom.uom_name from grocery.products inner join uom on products.uom=uom.uom_id ORDER BY product_id;")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def add_new_product(connection,product):
    curosr = connection.cursor()
    query = ("insert into grocery.products (name,uom,price) values (%s,%s,%s)")
    data = (product['name'],product['uom'],product['price'])
    curosr.execute(query,data)
    connection.commit()
    
    return curosr.lastrowid
    
def delete_product(connection, product_id):
    curosr = connection.cursor() 
    query = ("delete from grocery.products where product_id="+str(product_id)) 
    curosr.execute(query)
    connection.commit()
    
if __name__ == "__main__":
    connection = get_sql_connection()
    get_all_products(connection)