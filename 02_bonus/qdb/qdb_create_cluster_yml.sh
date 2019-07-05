#!/bin/bash

FILE=docker-compose.yml

if [ -f $FILE ]; then
    echo "$FILE is already exist"
    exit
fi

if [ -z $1 ]; then
    echo "Usage: bash $0 [number of nodes]"
    exit
fi

if [ $1 -lt 1 ]; then
    echo "number of nodes should be more than 0"
    exit
fi

cat > $FILE << EOM
version: '3.7'
networks:
  qdb-cluster:
    name: qdb-cluster
services:
  node1:
    image: "bureau14/qdb"
    container_name: node1
    networks:
      - qdb-cluster
EOM

for (( i=2; i<=$1; i++ )); do
    cat >> $FILE << EOM
  node$i:
    image: "bureau14/qdb"
    container_name: node$i
    depends_on:
      - node1
    command:
      - "--peer node1:2836 --id $i/$1"
    networks:
      - qdb-cluster
EOM
done