Ansible Role: RabbitMQ
===

[![Build Status](https://travis-ci.org/mm0/ansible-role-rabbitmq.svg?branch=master)](https://travis-ci.org/mm0/ansible-role-rabbitmq)

An Ansible role that installs and configures RabbitMQ

Requirements
---

None 

Role Variables
---

Available variables are listed below:

```yml
rabbitmq_port: 5672
handshake_timeout: 10000
cookie: fakecookie
user: user
password: password
monitoring_user: haproxy
haproxy_monitoring_password: password
cluster_nodes: "'rabbit@dev.example.com'"
rabbitmq_hostname: 'dev.example.com'
rabbitmq_nodename: 'rabbitmq'
enable_cluster: false
use_longname: false
log_level: debug
cluster_partition_handling: 'autoheal' #'pause_minority' # default recommended for 3 node AZ EC2 cluster 
```

Dependencies
---

None 

Example Playbook
---

```yml
- hosts: node
  roles:
  - { role: mm0.rabbitmq }
```
Cluster
```yml
- hosts: nodes
  vars:
    - enable_cluster: true
    - cluster_partition_handling: true
    - rabbitmq_cookie: 213hiahsfkjashk
  roles:
  - { role: mm0.rabbitmq }
License
---------------

BSD-2

Author Information
------------------

[Matt Margolin](mailto:matt.margolin@gmail.com)

[mm0](https://github.com/mm0) on github
