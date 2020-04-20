import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_installed_git(host):
    assert host.package("git").is_installed

def test_installed_python(host):
    assert host.package("python3").is_installed
    assert host.package("python3-pip").is_installed
