import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_rabbitmq_server_is_installed(host):
    rabbitmq = host.package('rabbitmq')

    assert rabbitmq.is_installed


def test_rabbitmq_is_running(host):
    rabbitmq = host.service('rabbitmq')

    assert rabbitmq.is_running
    assert rabbitmq.is_enabled
