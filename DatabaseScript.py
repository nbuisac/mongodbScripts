'''
Created on 2 de març 2023

@author: nbuisac
'''
import pymongo

client = pymongo.MongoClient("localhost", 27017)

## Crea o es connecta a una base de dades
db = client.test
print(db.name)

## eliminem la col·lecció si aquesta existís
db.my_collection.drop()

## inserim un document a la col·lecció
print(db.my_collection.insert_one({"x":10}).inserted_id)
print(db.my_collection.insert_one({"x":20, "name" : "Pepe"}).inserted_id)
print(db.my_collection.insert_one({"x":30, "name" : "Alberto", "surname" : "Soto"}).inserted_id)


dades = db.my_collection.find()
for fila in dades:
    print(fila)
 
#Loop through a collection in a descending order
print("Dades en ordre descendent")
for item in db.my_collection.find().sort("x", pymongo.DESCENDING):
    print(item)
#Update one element in a collection    
myquery = { "name": "Alberto" }
newvalues = { "$set": { "name": "Jordi" } }
db.my_collection.update_one(myquery, newvalues)
#print "customers" after the update:
print("Nous registres després de modificar")
for item in db.my_collection.find():
    print(item)