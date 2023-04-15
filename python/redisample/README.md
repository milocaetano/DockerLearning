#


Executing command:

docker network create redis-net

docker run --name my-redis --network redis-net -d redis

docker exec -it my-redis redis-cli

