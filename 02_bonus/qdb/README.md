# qdb_create_cluster_yml.sh
A script to create docker-compose yml file for QuasarDB cluster.

## How to use
* Create yml file
    ```
    bash qdb_create_cluster_yml.sh [number of nodes]
    ```
* Create cluster with docker-compose using yml file that we just created
    ```
    docker-compose up -d
    ```

## Testing
Let assume that we create at least 2 nodes with above instructions
* Use qdbsh to add a blob to node1
    ```
    docker run --network qdb-cluster bureau14/qdbsh qdb://node1:2836 -c "blob_put hello world"
    ```
* Use qdbsh to get a blob from node2
    ```
    docker run --network qdb-cluster bureau14/qdbsh qdb://node2:2836 -c "blob_get hello"
    ```

## Closing and clean up
```
docker compose down
```