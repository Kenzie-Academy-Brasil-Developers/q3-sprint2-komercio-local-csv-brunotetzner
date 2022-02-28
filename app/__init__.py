from flask import Flask, request
from .products import func_create_product, func_edit_product, func_delete_product,func_get_one_product,func_list_products
import csv
app = Flask(__name__)

@app.get('/products')
def list_products():
    page = request.args.get("page")
    number_of_products = request.args.get("per_page")                  
    return func_list_products(page, number_of_products)
    
@app.get('/products/<int:id>')
def get_one_product(id):
    id=str(id)
    return func_get_one_product(id)
    

@app.post("/products")
def create_product():
    data = request.get_json()
    name = data.get("name")
    price= data.get("price")

    return func_create_product(name, price)

@app.patch("/products/<int:id>")
def change_product(id):
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    id=str(id)

    return func_edit_product(name, price, id)
    
    


@app.delete("/products/<int:id>")
def delete_product(id):
     return func_delete_product(id)


          
