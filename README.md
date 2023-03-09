# Scripts de Mongodb

Scripts fets al Curs de MongoDB del 2023. Professor _Jordi Ascensión_.

* [Accés a github web](https://nbuisac.github.io/mongodbScripts/)

* [Accés a github de codi personal](https://github.com/nbuisac/mongodbScripts)

Ara podem executar des del cmd

    mongosh 127.0.0.1/school CreateSchoolSchema.js
    mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school" --apiVersion 1 --username narcis CreateSchoolSchema.js

i també

    mongosh 127.0.0.1/school GetStudents.js
    mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school" --apiVersion 1 --username narcis GetStudents.js

## Execute Postman files via Newman

    newman run NttData-Student-Gencat.postman_collection.json -e NttData-Student-PRO.postman_environment.json

## Treballem amb postman via newman i generem scripts js

Generem un script js per a
 
* inserir un document

* actualitzar un document

* eliminar un document

* inserir varis documents

* actualitzar varis documents

* eliminar varis documents

l'script s'anomena `TreballantAmbSchool.js` i l'executarem de dues formes diferents

* contra el **servidor local** (127.0.0.1) amb la comanda

    ```
    mongosh mongodb://127.0.0.1/school TreballantAmbSchool.js
    ```

* contra el **servidor Atlas** amb la comanda

    ```
    mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school" --apiVersion 1 --username narcis treballantAmbSchool.js
    ```
Amb newman farem quelcom semblant creant unes APIs que realitzaran les següents accions:

Generem un script js per a
 
* cercar un document

* inserir un document

* modificar un document

* eliminar un document

* inserir varis documents

* cercar varis documents

* actualitzar varis documents incrementant el gpa

* actualitzar varis documents decrementant el gpa

* utilitzar el pipeline per saber quants *alumnes* tenim de cada *major*

* eliminar varis documents

La comanda per executar l'script js és

```
mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school" --apiVersion 1 --username narcis TreballantAmbSchool.js
```

per executar amb newman les consultes anteriors utilitzarem dos fitxers

* `MongoDBDataAPI.postman_school.json`: amb les comandes a realitzar

* `DataAPI.postman_environment_school.json`: amb les variables necessàries per executar les comandes (entorn)

La comanda per executar-ho tot és:

```
newman run MongoDBDataAPI.postman_school.json -e DataAPI.postman_environment_school.json -r htmlextra
```

Aquest darrer paràmetre `-r htmlextra` ens generarà el document `html`.

Amb el paràmeter `-r htmlextra` no genera res a la consola. Sense el paràmetre `-r htmlextra` la sortida esperada és:

```
newman run MongoDBDataAPI.postman_school.json -e DataAPI.postman_environment_school.json
newman

MongoDB Data API

→ Insert Document
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/insertOne [201 Created, 407B, 463ms]
  √  Status test
  √  Resposta correcta

→ Find Document
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/findOne [200 OK, 449B, 183ms]
  √  Status test
  √  Resposta correcta

→ Update Document
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/updateOne [200 OK, 389B, 206ms]
  √  Status test
  √  Resposta correcta

→ Delete Document
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/deleteOne [200 OK, 379B, 252ms]
  √  Status test
  √  Resposta correcta

→ Insert Multiple Documents
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/insertMany [201 Created, 418B, 212ms]
  √  Status test
  √  Resposta correcta

→ Find Multiple Documents
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/find [200 OK, 492B, 163ms]
  √  Status test
  √  Resposta correcta

→ Update Multiple Documents
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/updateMany [200 OK, 389B, 465ms]
  √  Status test
  √  Resposta correcta

→ Update Multiple Documents Decrement
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/updateMany [200 OK, 389B, 413ms]
  √  Status test
  √  Resposta correcta

→ Run Aggregation Pipeline
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/aggregate [200 OK, 429B, 199ms]
  √  Status test
  √  Resposta correcta

→ Delete Many Documents
  POST https://eu-west-2.aws.data.mongodb-api.com/app/data-coxma/endpoint/data/v1/action/deleteMany [200 OK, 379B, 240ms]
  √  Status test
  √  Resposta correcta

┌─────────────────────────┬─────────────────────┬────────────────────┐
│                         │            executed │             failed │
├─────────────────────────┼─────────────────────┼────────────────────┤
│              iterations │                   1 │                  0 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│                requests │                  10 │                  0 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│            test-scripts │                  20 │                  0 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│      prerequest-scripts │                  10 │                  0 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│              assertions │                  20 │                  0 │
├─────────────────────────┴─────────────────────┴────────────────────┤
│ total run duration: 3.8s                                           │
├────────────────────────────────────────────────────────────────────┤
│ total data received: 738B (approx)                                 │
├────────────────────────────────────────────────────────────────────┤
│ average response time: 279ms [min: 163ms, max: 465ms, s.d.: 112ms] │
└────────────────────────────────────────────────────────────────────┘
```

# 02/03/2023

Hem actualitzat les proves newman de `school` i hem afegit el fitxer `startup.bat` que executa els dos newman que hem generat fins ara.

## Python && MongoDB

Cal instal·lar `pymongo` via `pip`

```
python -m pip install pymongo
```

De deures cal fer el mateix que amb Postman però amb Python

Hem creat l'script de python `SchoolCRUD.py` que podem executar des del `CMD` o la `shell` amb la comanda

```
python SchoolCrud.py
```

Es connecta al `mongodb` del propi ordinador, `localhost` pel port per defecte `27017`.

He trobat documentació al respecte a:

* [https://pymongo.readthedocs.io/en/stable/index.html](https://pymongo.readthedocs.io/en/stable/index.html): Índex de la documentació de la libreria `pymongo`

* [https://pymongo.readthedocs.io/en/stable/api/pymongo/](https://pymongo.readthedocs.io/en/stable/api/pymongo/): llibreria `pymongo`

* [https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html](https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html): col·lecció `pymongo.collection`. Aquí trobem els mètodes per a treballar amb les col·leccions

* [https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult](https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.InsertOneResult): `pymongo.results` pel tractament dels resultats de les comandes `insert_one`, `update_one`, `delete_one`, `insert_many`, `update_many` i `delete_many`

Per treballar directament amb la API de MongoDB, trobarem informació a [https://pymongo.readthedocs.io/en/stable/api/pymongo/server_api.html](https://pymongo.readthedocs.io/en/stable/api/pymongo/server_api.html)

# 07/03/2023

Treballem amb `Environment Variables`. Crearem variables d'entorn en el sistema

* `MongoDBConnection`: de moment li posem `localhost`

Podem accedir a les variables d'entorn de la següent forma:

```python
import os

print(os.environ["PATH"])
print(os.environ["MongoDBConnection"])
```


Hem activat les `Github Pages` i ara tinc accés a:

* [https://nbuisac.github.io/mongodbScripts/](https://nbuisac.github.io/mongodbScripts/)

i als reports de newman

* [https://nbuisac.github.io/mongodbScripts/newman/MongoDB%20Data%20API-2023-02-28-09-36-28-708-0.html](https://nbuisac.github.io/mongodbScripts/newman/MongoDB%20Data%20API-2023-02-28-09-36-28-708-0.html)

* [https://nbuisac.github.io/mongodbScripts/newman/MongoDB%20Data%20API-2023-03-02-15-54-42-601-0.html](https://nbuisac.github.io/mongodbScripts/newman/MongoDB%20Data%20API-2023-03-02-15-54-42-601-0.html)

* [https://nbuisac.github.io/mongodbScripts/newman/NttData-Student-Gencat-2023-02-23-14-53-24-205-0.html](https://nbuisac.github.io/mongodbScripts/newman/NttData-Student-Gencat-2023-02-23-14-53-24-205-0.html)

* [https://nbuisac.github.io/mongodbScripts/newman/NttData-Student-Gencat-2023-03-02-15-54-40-564-0.html](https://nbuisac.github.io/mongodbScripts/newman/NttData-Student-Gencat-2023-03-02-15-54-40-564-0.html)

Per a treballar amb Python i connectar-nos segons variables d'entorn he creat el programa `SchoolCRUDEnv.py` que reauqreix la variable d'entorn `MongoDBConnection` i si es vol posar amb signes estranys, com ara ampersand &, podem posar tota la variable entre cometes dobles. Així, valors possibles són:

* `localhost`

* `"mongodb://localhost:27017/?readPreference=primary&ssl=false&directConnection=true"`

* `"mongodb+srv://narcis@cluster0.axngmv4.mongodb.net/test"`

Per executar:

```
python SchoolCRUDEnv.py
```

per assignar variables d'entorn en *Windows*, des del `CMD`, podem utilitzar:

```doscon
SET MongoDBConnection=localhost
SET MongoDBConnection="mongodb://localhost:27017/?readPreference=primary\&ssl=false\&directConnection=true"
SET MongoDBConnection="mongodb+srv://narcis@cluster0.axngmv4.mongodb.net/test"
```

He controlat l'error de connexió amb un `try` però, no es produeix la connexió fins que no fem el primer `find`.

Aquesta, per tant, és la instrucció que hem de posar dins el `try`.

# 09/03/2023

Avui és el darrer dia. Mirem com funcionen les `pipelines` (`aggregate`)

Després fem la *validació s'esquemes*.

Quan se’nsenya JSON també caldria ensenyar json-schema [https://json-schema.org/](https://json-schema.org/)

* [https://www.mongodb.com/docs/manual/core/schema-validation/](https://www.mongodb.com/docs/manual/core/schema-validation/) 

* [https://www.mongodb.com/docs/manual/core/schema-validation/specify-json-schema/#std-label-schema-validation-json](https://www.mongodb.com/docs/manual/core/schema-validation/specify-json-schema/#std-label-schema-validation-json) 

Creem dos scripts: `StudentsValidation.js` i `StudentsInsert.js`. Per executar-los:

```
mongosh 127.0.0.1/school StudentsValidation.js
mongosh 127.0.0.1/school StudentsInsert.js
```

Finalment veiem com fer referències entre col·leccions i la comanda/pipeline `lookup` a la pàgina [https://medium.com/@dcortes.net/relaciones-en-mongodb-edf2107a94ad](https://medium.com/@dcortes.net/relaciones-en-mongodb-edf2107a94ad)

Sintaxi **lookup**

```
{   
  $lookup: {       
    from: <collection to join>,     
    localField: <field from the input documents>,       
    foreignField: <field from "from" collection>,
    as: <output array field>     
  }
}
```