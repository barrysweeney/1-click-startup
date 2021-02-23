#!/bin/bash

sudo docker-compose up

SERVER_IP_ADDRESS=$( sudo docker inspect --format '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-freeipa-container)

echo "$SERVER_IP_ADDRESS  ipa.xyz.test" | sudo tee -a /etc/hosts
