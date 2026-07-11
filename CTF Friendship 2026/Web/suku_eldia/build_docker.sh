#!/bin/sh
docker rm -f suku_eldia
docker build -t suku_eldia .
docker run --name=suku_eldia --rm -p1337:1337 -it suku_eldia