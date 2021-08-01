#!/bin/bash

docker-compose up -d

python3 ./DataToJson.py

mongoimport --db cr-db --collection users --file users.json --jsonArray

mongoexport --db cr-db -c users --out exData.json --forceTableScan

python3 ./app.py