# -*- coding: utf-8 -*-

from fabric.api import cd
from provy.core import Role
from provy.more.debian import GitRole, PipRole


VM_IP = '192.168.1.11'
SITE_PATH = '/home/vagrant/provy-demo/demo/'


class SimpleServer(Role):
    def provision(self):
        with self.using(PipRole) as role:
            role.ensure_package_installed('django')
            role.ensure_package_installed('gunicorn')

        with self.using(GitRole) as role:
            role.ensure_repository('git://github.com/diogobaeder/provy-demo.git',
                                   '/home/vagrant/provy-demo')

        with cd(SITE_PATH):
            self.execute('gunicorn --daemon demo.wsgi:application')

servers = {
    'demo': {
        'address': VM_IP,
        'user': 'vagrant',
        'roles': [
            SimpleServer
        ]
    }
}