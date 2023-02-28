print("Estudiants inicials: " + db.students.find().count() );
printjson(db.students.find() );
print("Afegim un estudiant...");
printjson(db.students.insertOne({ "name": 'Narcis', "major": 'Computers', "gpa": 5.2} ) );
print("L'estudiant afegit");
printjson(db.students.findOne({ "name" : "Narcis" } ) );
print("Modifiquem l'estudiant");
printjson(db.students.updateOne({ "name": 'Narcis' },  { $set : { "gpa": 4.1 } } ) );
print("L'estudiant modificat");
printjson(db.students.findOne({ "name" : "Narcis" } ) );
print("Eliminem l'estudiant");
printjson(db.students.deleteOne({ "name": 'Narcis' } ) );
print("Afegim tres estudiants...");
printjson(db.students.insertMany([
    { "name": 'Narcis', "major": 'Computers', "gpa": 5.2 },
    { "name": 'Maria', "major": 'Marketing', "gpa": 4.4 },
    { "name": 'Paula', "major": 'Computers', "gpa": 4.6 }
]) );
print("Els estudiants afegits");
printjson(db.students.find({gpa : { $gt : 4.0 } } ) );
print("Modifiquem el estudiants incrementant en 0.2 el gpa");
printjson(db.students.updateMany({ gpa : { $gt : 4.0 } },  { $inc : { "gpa": 0.2 } } ) );
print("Els estudiants modificats");
printjson(db.students.find({gpa : { $gt : 4.0 } } ) );
print("Modifiquem el estudiants incrementant en 0.2 el gpa");
printjson(db.students.updateMany({ gpa : { $gt : 4.0 } },  { $inc : { "gpa": -0.1 } } ) );
print("Els estudiants modificats");
printjson(db.students.find({gpa : { $gt : 4.0 } } ) );
print("Estudiants per major amb la mitjana de Gpa");
printjson(db.students.aggregate( 
    [ {$group : 
        {_id : "$major", 
        "quants" : { $sum : 1 }, 
        "mitjanaGpa" : {$avg : "$gpa"} 
        } 
      }, 
      { $sort : { "quants" : -1} } 
    ] ) 
);
print("Elimnem el estudiants incrementant en 0.2 el gpa");
printjson(db.students.deleteMany({gpa : { $gt : 4.0 } } ) );



