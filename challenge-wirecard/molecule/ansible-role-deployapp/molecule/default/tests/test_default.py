import os

import testinfra.utils.ansible_runner
import requests

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

#def test_hostname(host):
 #   assert 'instance' == host.check_output('hostname -s')

def test_request_response():
    # Send a request to the API server and store the response.
    response = requests.get('https://172.17.0.2', verify=False)
    assert response.status_code == 200
