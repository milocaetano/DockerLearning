#


Executing command:

docker network create redis-net

docker run --name my-redis --network redis-net -d redis

docker exec -it my-redis redis-cli

#Execute docker compose

This  for building a docker container each time you run a command

 docker-compose up --build 