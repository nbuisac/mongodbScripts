# Scripts de Mongodb

Scripts fets al Curs de MongoDB del 2023. Professor _Jordi Ascensión_.

Ara podem executar des del cmd

    mongosh 127.0.0.1/school CreateSchoolSchema.js
    mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school"  --username narcis CreateSchoolSchema.js

i també

    mongosh 127.0.0.1/school GetStudents.js
    mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school"  --username narcis GetStudents.js

### Execute Postman files via Newman

    newman run NttData-Student-Gencat.postman_collection.json -e NttData-Student-PRO.postman_environment.json

### Treballem amb postman via newman i generem scripts js

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
    mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school"  --username narcis --password narcis treballantAmbSchool.js
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
mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school"  --username narcis --password narcis TreballantAmbSchool.js
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

## 02/03/2023

Hem actualitzat les proves newman de `school` i hem afegit el fitxer `startup.bat` que executa els dos newman que hem generat fins ara.

# Python && MongoDB

Cal instal·lar `pymongo` via `pip`

```
python -m pip install pymongo
```

De deures cal fer el mateix que amb Postman però amb Python

