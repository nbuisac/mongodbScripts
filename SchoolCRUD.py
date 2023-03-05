'''
Created on 5 de març 2023

@author: nbuisac
'''
import pymongo

## Definim les variables amb què treballarem

InsertOne = {
    "name" : "Narcis",
    "major" : "Computers",
    "gpa" : 5.2
}

UpdateOneSet = {
    "$set" : { "gpa" : 4.1 }
}

IncrementaGpa = {
    "$inc" : { "gpa" : 0.2 }
}

DecrementaGpa = {
    "$inc" : { "gpa" : -0.1 }
}

InsertMany = [    
    { "name": 'Narcis', "major": 'Computers', "gpa": 5.2 },
    { "name": 'Maria', "major": 'Marketing', "gpa": 4.4 },
    { "name": 'Paula', "major": 'Computers', "gpa": 4.6 }
]

UpdateManyCond = { "gpa" : { "$gt" : 4.0 } }
UpdateManySet_Inc = { "$inc" : { "gpa": 0.2 } }
UpdateManySet_Dec = { "$inc" : { "gpa": -0.1 } }

## Funcions que utilitzarem
def mostraDades(dades):
    q = 0
    for fila in dades:
        print(fila)
        q = q + 1
    print("Files totals: ", q );

def mostraTots(colleccio):
    dades = colleccio.find()
    mostraDades(dades)

def mostraCondicio(colleccio, condicio):
    dades = colleccio.find(condicio)
    mostraDades(dades)


client = pymongo.MongoClient("localhost", 27017)

## Crea o es connecta a una base de dades
db = client.school
print(db.name)

estudiants = db.students

mostraTots(estudiants)

## Afegim un estudiant
resultat = estudiants.insert_one(InsertOne)
print("Estudiant afegit amb _id: ", resultat.inserted_id, resultat.acknowledged)
if resultat.acknowledged:
    mostraTots(estudiants)
else:
    print("Error inserint l'estudiant")

dades = estudiants.find({"name" : InsertOne["name"]})
print("Estudiant afegit ... ")
mostraDades(dades)


resultat = estudiants.update_one({"name" : InsertOne["name"]}, UpdateOneSet)
if resultat.acknowledged:
    dades = estudiants.find({"name" : InsertOne["name"]})
    print("Estudiant(s) modificat(s) (", resultat.modified_count, "/", resultat.matched_count, ")", sep="")
    mostraDades(dades)
else:
    print("Cap estudiant modificat")

resultat = estudiants.delete_one({"name" : InsertOne["name"]})
if resultat.acknowledged:
    print("Estudiants eliminats", resultat.deleted_count)
else:
    print("Error eliminant l'estudiant")


## Afegim varis estudiants
resultat = estudiants.insert_many(InsertMany)
if resultat.acknowledged:
    print("Estudiants afegits amb _id:")
    mostraDades(resultat.inserted_ids)
else:
    print("Error inserint varis estudiants")

## Modifiquem el estudiants incrementant en 0.2 el gpa
resultat = estudiants.update_many(UpdateManyCond, UpdateManySet_Inc)
if resultat.acknowledged:
    print("Estudiant(s) modificat(s) (", resultat.modified_count, "/", resultat.matched_count, ")", sep="")
    mostraCondicio(estudiants, UpdateManyCond)
else:
    print("Cap estudiant modificat")

## Modifiquem el estudiants decrementant en 0.1 el gpa
resultat = estudiants.update_many(UpdateManyCond, UpdateManySet_Dec)
if resultat.acknowledged:
    print("Estudiant(s) modificat(s) (", resultat.modified_count, "/", resultat.matched_count, ")", sep="")
    mostraCondicio(estudiants, UpdateManyCond)
else:
    print("Cap estudiant modificat")

resultat = estudiants.delete_many(UpdateManyCond)
if resultat.acknowledged:
    print("Estudiant(s) eliminat(s):", resultat.deleted_count)
    mostraCondicio(estudiants, UpdateManyCond)
else:
    print("Cap estudiant modificat")

client.close()
