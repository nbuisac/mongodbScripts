printjson(
    db.runCommand({
        "collMod": "students",
        "validator": {
            $jsonSchema: {
                "bsonType": "object",
                "description": "Document describing a student",
                "required": ["name"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "Name must be a string and is required"
                    }
                },
            }
        }
    })
)