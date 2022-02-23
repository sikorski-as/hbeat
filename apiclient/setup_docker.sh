# install docker
apt-get update && sudo apt-get upgrade
curl -sSL https://get.docker.com | sh

# activate docker on system boot
systemctl enable docker

# start hbeat client as a docker container
docker-compose up