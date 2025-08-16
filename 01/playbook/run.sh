#!/usr/bin/env bash
set -e

# --- Контейнеры ---
CENTOS=centos7
UBUNTU=ubuntu
FEDORA=fedora

# --- Поднять контейнеры ---
docker run -d --name $CENTOS centos:7 sleep infinity
docker run -d --name $UBUNTU ubuntu:22.04 sleep infinity
docker run -d --name $FEDORA pycontribs/fedora sleep infinity

# --- Установить Python на Ubuntu ---
docker exec -it ubuntu bash -lc 'apt-get update && apt-get -y install python3'

# --- Запустить playbook ---
ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass

# --- Остановить и удалить контейнеры ---
docker rm -f $CENTOS $UBUNTU $FEDORA
