# DockerLearning

docker run hello-world #run hello world image

docker run -it ubuntu bash  #run docker ubuntu with bash 
docker ps
docker ps -a
docker run -it --rm ubuntu bash #run docker and remove container after finish

-rm  (remove container após execução concluída)

## working with network host

docker run --rm -d --name nginx --network host ngix