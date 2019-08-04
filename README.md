Ansible Role: RabbitMQ
===

[![Build Status](https://travis-ci.org/mm0/ansible-role-rabbitmq.svg?branch=master)](https://travis-ci.org/mm0/ansible-role-rabbitmq)
[![Galaxy](https://img.shields.io/badge/galaxy-mm0.rabbitmq-blue.svg?style=flat)](https://galaxy.ansible.com/mm0/ansible-role-rabbitmq)

An Ansible role that installs and configures RabbitMQ

Requirements
---

None 

*The following variables must be configured:*

| Ansible Variable(s)  | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `rabbitmq_cookie` | `fakecookie` | Cluster cookie authentication value |
| `rabbitmq_user` | `user` | Change to set admin username |
| `rabbitmq_password` | `password` | Change to set admin password |




Role Variables
---

*All variables*

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `rabbitmq_port` | `5672` | Listening port|
| `enable_cluster` | `false` | Single node mode if false, cluster mode if true|
| `use_longname` | `false` | Set to true if using FQDN for node names/hostnames |
| `handshake_timeout` | `10000` | Cluster handshake timeout |
| `rabbitmq_cookie` | `fakecookie` | Cluster cookie authentication value |
| `rabbitmq_user` | `user` | Default admin username |
| `rabbitmq_password` | `password` | Default admin password |
| `rabbitmq_monitoring_user` | `haproxy` | Default monitorign username |
| `rabbitmq_monitoring_password` | `password` | Default monitoring password |
| `cluster_nodes` | `""` | This must be a string in the format "'rabbitmq@nodehostname','rabbitmq@node2hostname','rabbitmq@node3hostname'|
| `log_level` | `debug` | Adjust verbosity |
| `cluster_partition_handling` | `autoheal` | Set the cluster partioning handling setting of your choice |
| `rabbitmq_plugins` |
  - rabbitmq_shovel
  - rabbitmq_shovel_management
  - rabbitmq_management
  - rabbitmq_federation
  - rabbitmq_tracing
  | A list of plugins to install |


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
