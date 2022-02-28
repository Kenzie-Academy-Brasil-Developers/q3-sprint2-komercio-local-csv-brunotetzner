from asyncore import read
import csv


def func_list_products(page, number_of_products):

    csv_open = open("./data/products.csv", "r")
    reader = list(csv.DictReader(csv_open))
    csv_open.close()

    try:
        count = int(page) * int(number_of_products) - int(number_of_products)
        list_of_products = list()

        while count < int(number_of_products)*int(page):
            list_of_products.append(reader[count])
            count+=1

        return {"data":list_of_products}
     
    except IndexError:
        return {"data": reader[0:3]}
    
    except TypeError:
        return {"data": reader[0:3]}



def func_get_one_product(id):

    csv_open = open("./data/products.csv", "r")
    reader = list(csv.DictReader(csv_open))
    id = str(id)
    csv_open.close()

    for product in  reader:
        if product['id'] == id:
            return product
  



def func_create_product(name, price):

    csv_read = open("./data/products.csv", "r")
    read = list(csv.DictReader(csv_read))
    csv_read.close()

    new_product = {"name": name, "price":price, 'id': int(read[len(read)-1]['id'])+1}
    
    field_names = ["id", "name","price"]
    open_csv = open("./data/products.csv", "a+")
    writer = csv.DictWriter(open_csv, fieldnames=field_names)
    writer.writerow(new_product)
    open_csv.close()

    return new_product, 201



def func_edit_product(name, price, id):
    
    edited_product = {"id": id, "name": name, "price": price}
    csv_read = open("./data/products.csv", "r")
    read = list(csv.DictReader(csv_read))
    list_csv = list()
   
    boolean = False
    for product in read:
        if id == product['id']:
            boolean = True
    if boolean == False:
        return {"error": f"product id {id} not found"}, 404

    for product in read:
        if edited_product['id'] == product['id']:
            if edited_product['price'] == None:
                edited_product['price'] = product['price']
            elif edited_product['name'] == None: 
                edited_product['name'] = product['name']
            list_csv.append(edited_product)
        else:
          list_csv.append(product)
    csv_read.close()
    
    
    field_names = ["id", "name", "price"]
    keys = {"id":"id", "name":"name", "price":"price"}
    clear_csv = open("./data/products.csv", "w")
    writer = csv.DictWriter(clear_csv, fieldnames=field_names)
    writer.writerow(keys)
    clear_csv.close()
    
    add_to_csv = open("./data/products.csv", "a+")

    count = 0
    while count < len(list_csv):
        writer = csv.DictWriter(add_to_csv, fieldnames=field_names)
        writer.writerow(list_csv[count])
        count+=1
    add_to_csv.close()

    return edited_product, 200



def func_delete_product(id):
    csv_read = open("./data/products.csv", "r")
    read = list(csv.DictReader(csv_read))
    list_csv = list()

    boolean = False
    for product in read:
        if str(id) == product['id']:
            boolean = True
    if boolean == False:
        return {"error": f"product id {id} not found"}, 404


    removed_product = dict()
    for product in read:
        if str(id) == product['id']:
           removed_product = product
           pass
        else:
          list_csv.append(product)
    csv_read.close()
    

    field_names = ["id", "name", "price"]
    keys = {"id":"id", "name":"name", "price":"price"}
    clear_csv = open("./data/products.csv", "w")
    writer = csv.DictWriter(clear_csv, fieldnames=field_names)
    writer.writerow(keys)
    clear_csv.close()
    
    add_to_csv = open("./data/products.csv", "a+")

    count = 0
    while count < len(list_csv):
        writer = csv.DictWriter(add_to_csv, fieldnames=field_names)
        writer.writerow(list_csv[count])
        count+=1
    add_to_csv.close()
    return removed_product,200
  


        