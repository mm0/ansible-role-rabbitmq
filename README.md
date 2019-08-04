Ansible Role: RabbitMQ
===

[![Build Status](https://travis-ci.org/mm0/ansible-role-rabbitmq.svg?branch=master)](https://travis-ci.org/mm0/ansible-role-rabbitmq)
[![Galaxy](https://img.shields.io/badge/galaxy-mm0.rabbitmq-blue.svg?style=flat)](https://galaxy.ansible.com/mm0/ansible-role-rabbitmq)

An Ansible role that installs and configures RabbitMQ as a Standalone node or as a Cluster.  Simple set a few parameters and you're set.  Admin panel will be available on port 15672.  Default credentials are set below. Currently only tested for Ubuntu and uses `apt`, however, both standalone and 3 node cluster is fully tested using `molecule` via `travis-ci` using docker or vagrant. If you'd like to contribute a Redhat compatibility PR that would be great! 

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
| `rabbitmq_plugins` | - rabbitmq_shovel<br/>- rabbitmq_shovel_management<br/>- rabbitmq_management<br/>- rabbitmq_federation<br/>- rabbitmq_tracing |  A list of plugins to install |


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
# Example Cluster Playbook

If you are using non-FQDN (myhostname), you must add these values + corresponding IP addresses to /etc/hosts.  
If you are using FQDN (myhostname.domain.com), set the `use_longname` variable to `true`
Don't forget to set the hostname on your system as a `pre_task` or separate playbook.  If your FQDN resolves to the right address and your servers are configured to resolve the correct DNS entry, then you just need to set `use_longname: true` and not worry about /etc/hosts.

```yml
- hosts: nodes
  vars:
    - enable_cluster: true
    - cluster_partition_handling: true
    - rabbitmq_cookie: 213hiahsfkjashk
    - cluster_nodes: 'rabbitmq@nodehostname','rabbitmq@node2hostname','rabbitmq@node3hostname'
  roles:
  - { role: mm0.rabbitmq }
License
---------------

BSD-2

Author Information
------------------

[Matt Margolin](mailto:matt.margolin@gmail.com)

[mm0](https://github.com/mm0) on github
