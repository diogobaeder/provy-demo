# -*- coding: utf-8 -*-

from provy.core import Role
from provy.more.debian import UserRole, AptitudeRole, DjangoRole


VM_IP = '192.168.1.11'


class SimpleServer(Role):
    def provision(self):
        with self.using(UserRole) as role:
            role.ensure_user('my-user', identified_by='my-pass', is_admin=True)

        with self.using(AptitudeRole) as role:
            role.ensure_package_installed('vim')

servers = {
    'frontend': {
        'address': VM_IP,
        'user': 'vagrant',
        'roles': [
            SimpleServer
        ]
    }
}