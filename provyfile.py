# -*- coding: utf-8 -*-

from provy.core import Role
from provy.more.debian import GitRole, PipRole


VM_IP = '192.168.1.11'


class SimpleServer(Role):
    def provision(self):
        with self.using(PipRole) as role:
            role.ensure_package_installed('django')

        with self.using(GitRole) as role:
            role.ensure_repository('git://github.com/diogobaeder/provy-demo.git',
                                   '/home/vagrant/provy-demo')

        self.execute('nohup python /home/vagrant/provy-demo/demo/manage.py runserver &')

servers = {
    'frontend': {
        'address': VM_IP,
        'user': 'vagrant',
        'roles': [
            SimpleServer
        ]
    }
}