use universidad
db.Contadores.insert({
    "_id":"productid",
    "sequence_value": 0
})
function getNextSequenceValue(sequenceName){
   var sequenceDocument = db.Contadores.findAndModify({
  	query:{_id: sequenceName },
  	update: {$inc:{sequence_value:1}},
  	new:true
   });
   return sequenceDocument.sequence_value;
}
db.Productos.insertOne({
   "_id":getNextSequenceValue("productid"),
   "nombre":"Apple iPhone",
   "categoría":"Teléfonos móviles"
})

db.Productos.insertOne({
   "_id":getNextSequenceValue("productid"),
   "nombre":"Samsung Galaxy",
   "categoría":"Teléfonos móviles"
})
db.Productos.insertOne({
    "_id":getNextSequenceValue("productid"),
    "nombre":"Xiaomi Redmi",
    "categoría":"Teléfonos móviles"
 })
 
 db.Productos.insertOne({
    "_id":getNextSequenceValue("productid"),
    "nombre":"Sony Xperia",
    "categoría":"Teléfonos móviles"
 })
 show dbs