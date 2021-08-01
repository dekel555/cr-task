#!/bin/bash

python3 ./DataToJson.py


docker-compose up -d

docker exec -i mongodb sh -c 'mongoimport -c <users> -d <cr-db> --drop' < ./users.json

docker exec mongodb sh -c 'mongoimport --db cr-db --collection users --drop --file /users.json --jsonArray'

docker exec mongodb sh -c 'mongoexport --db cr-db -c users --out exData.json --forceTableScan'

docker cp mongodb:/exData.json .

python3 ./app.py
