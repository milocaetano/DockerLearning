#Docker networking cmds

docker network ls #list all networks
docker network prune #remove all networks

docker rm -f ubuntu1 #remove imagem ubuntu1

docker run -d -it --name ubuntu1 ubuntu bash #run ubuntu and execute bash, but -d deatach the bash command
docker run -it --name ubuntu1 ubuntu bash #run ubuntu and execute bash, but keep the bash command

docker ps | grep ubuntu  ##list all ubuntu containers 

docker network inspect bridge ## check all containers using the bridge


#attach to the container
docker attach ubuntu1 #attach to the container
docker attach ubuntu2 #attach to the container

#apt-get

sudo apt-get update
sudo apt-get install iproute2

#how to use the iproute2
ip addr show 



