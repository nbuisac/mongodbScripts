# Scripts de Mongodb

Scripts fets al Curs de MongoDB del 2023. Professor _Jordi Ascensión_.

Ara podem executar des del cmd
```
mongosh 127.0.0.1/school CreateSchoolSchema.js
mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school"  --username narcis CreateSchoolSchema.js
```

i també

```
mongosh 127.0.0.1/school GetStudents.js
mongosh "mongodb+srv://cluster0.axngmv4.mongodb.net/school"  --username narcis GetStudents.js
```

### Execute Postman files via Newman
newman run NttData-Student-Gencat.postman_collection.json -e NttData-Student-PRO.postman_environment.json