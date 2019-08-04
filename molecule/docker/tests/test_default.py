import os

import testinfra.utils.ansible_runner

import logging

LOG = logging.getLogger("toto")

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_config_file(host):
    f = host.file('/etc/rabbitmq/rabbitmq.config')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_rabbitmq_server_is_installed(host):
    rabbitmq = host.package('rabbitmq-server')

    assert rabbitmq.is_installed


def test_rabbitmq_is_running(host):
    rabbitmq = host.service('rabbitmq-server')

    assert rabbitmq.is_running
    assert rabbitmq.is_enabled


def test_rabbitmq_is_listening(host):
    rabbitmq = host.socket('tcp://0.0.0.0:5672')

    assert rabbitmq.is_listening


def test_rabbitmq_status(host):
    cmd = host.run("rabbitmqctl status")

    assert "uptime" in cmd.stdout


def test_rabbitmq_cluster_status(host):
    cmd = host.run("rabbitmqctl cluster_status")

    for i in ['rabbitmq@node1']:
        assert i in cmd.stdout
