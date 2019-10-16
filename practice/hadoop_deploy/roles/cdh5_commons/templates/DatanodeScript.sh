#!/bin/bash
# update /etc/hosts

sudo mkdir -p /data1/nn /data1/jn

for item in {1..5}; do
    sudo mkdir -p /data$item/dn
    sudo mkdir -p /data$item/yarn/local
    sudo mkdir -p /data$item/yarn/logs
    sudo chown -R  {{hadoop_user}}:{{hadoop_group}} /data$item
done

